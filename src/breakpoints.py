from ptrace.binding import *

INT3 = 0xcc
ALIGNMENT = 8

# a brekpoint is activated by placing a special unstruction (int 3)
class Breakpoint:
    # initate a disabled breakpoint
    # get the pid and address of instruction
    def __init__(self, pid, addr):
        self.pid = pid
        self.addr = addr
        self.is_enable = False
        self.saved_data = 0x0

        # address can be read only at aligned addresses
        self.align_address = addr - (addr % ALIGNMENT)
        # a mask for getting the wanted address out of the aligned one
        self.address_from_align_mask = 0xff << ((addr % ALIGNMENT) * 8)

    def enable(self):
        data = ptrace_peektext(self.pid, self.align_address)

        # saved data is the data that was in the process
        # before we replaced it by the trap, therefore
        # it is the buttom bye of the data we read
        self.saved_data = data & self.address_from_align_mask
        data_to_write = (data & ~self.address_from_align_mask) | (INT3 << ((self.addr % ALIGNMENT) * 8))
        ptrace_poketext(self.pid, self.align_address, data_to_write)

        self.is_enable = True

    def disable(self):
        data = ptrace_peektext(self.pid, self.align_address)
        restored_data = (data & ~self.address_from_align_mask) | self.saved_data
        ptrace_poketext(self.pid, self.align_address, restored_data)

        self.is_enable = False