from ptrace.binding import *

INT3 = 0xcc

# a brekpoint is activated by placing a special unstruction (int 3)
class Breakpoint:
    # initate a disabled breakpoint
    # get the pid and address of instruction
    def __init__(self, pid, addr):
        self.pid = pid
        self.addr = addr
        self.is_enable = False
        self.saved_data = 0x0

    def enable(self):
        data = ptrace_peektext(self.pid, self.addr)

        # saved data is the data that was in the process
        # before we replaced it by the trap, therefore
        # it is the buttom bye of the data we read
        self.saved_data = data & 0xff
        data_to_write = (data & ~0xff) | INT3
        ptrace_poketext(self.pid, self.addr, data_to_write)

        self.is_enable = True

    def disable(self):
        data = ptrace_peektext(self.pid, self.addr)
        restored_data = (data & ~0xff) | self.saved_data
        ptrace_poketext(self.pid, self.addr, restored_data)

        self.is_enable = False