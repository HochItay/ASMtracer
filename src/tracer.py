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
        ptrace_cont(self.pid)
        os.waitpid(self.pid, 0)

    def single_step(self):
        rip = self.get_current_instruction()
        if rip in self.breakpoints and self.breakpoints[rip].is_enable:
            b = self.breakpoints[rip]
            b.disable()
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)
            b.enable()
        else:
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)

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

    # read a big chunk from the memory using the /proc/<pid>/mem file
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
        b = breakpoints.Breakpoint(self.pid, addr)
        b.enable()
        self.breakpoints[addr] = b

    # remove a breakpoint in a given address
    def remove_breakpoint(self, addr):
        del self.breakpoints[addr]

    # single step
    # if execution stopped by a breakpoint, jump over that breakpoint
    def step_over_breakpoint(self):
        # if we stopped at a breakpoint, the rip will point to one byte over the breakpointed instruction
        possible_breakpoint = self.get_current_instruction() - 1

        # check if breakpoint is exist and active
        if possible_breakpoint in self.breakpoints and self.breakpoints[possible_breakpoint].is_enable:
            b = self.breakpoints[possible_breakpoint]
            b.disable()
            self.dec_rip()
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)
            b.enable()

        else:
            ptrace_singlestep(self.pid)
            os.waitpid(self.pid, 0)