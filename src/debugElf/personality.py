from ctypes import *

ADDR_NO_RANDOMIZE = 0x0040000

libc = CDLL('libc.so.6')

# disable address randomizations
def disable_addr_rand():
    libc.personality(ADDR_NO_RANDOMIZE)

