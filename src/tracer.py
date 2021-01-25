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
            self.breakpoints = []
            # wait for signal from child
            os.waitpid(self.pid, 0)

    # contincue execution of the tracee until next breakpoint
    def continue_execution(self):
        ptrace_cont(self.pid)
        os.waitpid(self.pid, 0)

    def single_step(self):
        ptrace_singlestep(self.pid)
        os.waitpid(self.pid, 0)

    # return the address of the current instruction (value of rip)
    def get_current_instruction(self):
        return ptrace_getregs(self.pid).rip

    # return registers value
    def get_registers(self):
        return ptrace_getregs(self.pid)
    
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
