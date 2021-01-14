import os
from ptrace.binding import *
import breakpoints
import personality


class Debugger:
    def __init__(self, exe):
        # open child process
        self.pid = os.fork()
        
        if (self.pid == 0):
            # allow tracing of child process, then execute the program
            personality.disable_addr_rand()
            ptrace_traceme()
            os.execl(exe, exe)
        else:
            self.run()

    def run(self):
        print(self.pid)
        print(os.waitpid(self.pid, 0))

Debugger('a.out')