import os
from ptrace.binding import *
import breakpoints
import personality


class Tracer:
    def __init__(self, exe):
        # open child process
        self.pid = os.fork()
        
        if (self.pid == 0):
            # allow tracing of child process, then execute the program
            personality.disable_addr_rand()
            ptrace_traceme()
            os.execl(exe, exe)
        else:
            self.breakpoints = {} # maps address to breakpoint
            # wait for signal from child
            os.waitpid(self.pid, 0)

    # contincue execution of the tracee until next breakpoint
    def continue_execution(self):
        self.step_over_breakpoint()
        ptrace_cont(self.pid)
        os.waitpid(self.pid, 0)

        # if stopped by breakpoint 
        possible_bp = self.get_current_instruction() - 1
        if possible_bp in self.breakpoints and self.breakpoints[possible_bp].is_enable:
            self.dec_rip()

    def single_step(self):
        self.step_over_breakpoint()

    # return the address of the current instruction (value of rip)
    def get_current_instruction(self):
        return ptrace_getregs(self.pid).rip

    # return registers value
    def get_registers(self):
        return ptrace_getregs(self.pid)
    
    # set registers value
    def set_registers(self, regs):
        ptrace_setregs(self.pid, regs)

    # read memory from the child process of the whole region
    # using the /proc/<pid>/maps file and /proc/<pid>/mem file
    # return the base address of the region, and its content
    def get_mem_by_region(self, region):
        mem = b''
        base_addr = None

        with open('/proc/' + str(self.pid) + '/maps', 'r') as maps:
            # structure of line in maps file is:
            # address perms offset  dev   inode   pathname
            for line in maps.readlines():
                splited = line.split()
                if len(splited) != 6:
                    continue

                address, perms, offset, _, _, pathname = splited
                offset = int(offset, 16) # convert hex string to int

                if pathname == region and offset == len(mem) and 'r' in perms:
                    start_addr, end_addr = address.split('-')
                    start_addr = int(start_addr, 16)
                    end_addr = int(end_addr, 16)
                    size = end_addr - start_addr

                    if offset == 0:
                        base_addr = start_addr

                    mem += self.read_from_memory(start_addr, size)

        if base_addr == None:
            raise Exception('region ' + region + ' not found')
        
        return base_addr, mem

    # read one word (8 bytes) from memory
    # return an int
    def read_word_from_memory(self, addr):
        return ptrace_peektext(self.pid, addr)

    # read a big chunk from the memory using the /proc/<pid>/mem file
    # return a binary string
    def read_from_memory(self, addr, size):
        with open('/proc/' + str(self.pid) + '/mem', 'rb') as mem:
            mem.seek(addr)
            return mem.read(size)

    # decrease rip by one
    def dec_rip(self):
        regs = self.get_registers()
        regs.rip -= 1
        self.set_registers(regs)

    # place a breakpoint in a given address
    def place_breakpoint(self, addr):
        if addr not in self.breakpoints:
            b = breakpoints.Breakpoint(self.pid, addr)
            b.enable()
            self.breakpoints[addr] = b

    # remove a breakpoint in a given address
    def remove_breakpoint(self, addr):
        if self.breakpoints[addr].is_enable:
            self.breakpoints[addr].disable()
        del self.breakpoints[addr]

    # single step, ignoring breakpoints
    def step_over_breakpoint(self):
        rip = self.get_current_instruction()

        # check if breakpoint is exist and active
        if rip in self.breakpoints and self.breakpoints[rip].is_enable:
            b = self.breakpoints[rip]
            b.disable()
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)
            b.enable()

        else:
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)

    # step out of the current function
    def step_out(self):
        # if convetions are followed, each function starts with:
        # push rbp
        # mov rbp, rsp
        # therefore, the return address of the function is located
        # 1 word above rbp
        base_pointer = self.get_registers().rbp
        return_address = self.read_word_from_memory(base_pointer + 8)

        should_remove_bp = False

        # place breakpoint at the return address
        if return_address not in self.breakpoints:
            self.place_breakpoint(return_address)
            should_remove_bp = True

        while self.get_current_instruction() != return_address:
            self.continue_execution()

        if should_remove_bp:
            self.remove_breakpoint(return_address)