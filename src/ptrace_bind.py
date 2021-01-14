from ctypes import *

PTRACE_TRACEME = 0
PTRACE_PEEKTEXT = 1
PTRACE_PEEKDATA = 2
PTRACE_PEEKUSER = 3
PTRACE_POKETEXT = 4
PTRACE_POKEDATA = 5
PTRACE_POKEUSER = 6
PTRACE_CONT = 7
PTRACE_KILL = 8
PTRACE_SINGLESTEP = 9
PTRACE_GETREGS = 12
PTRACE_SETREGS = 13
PTRACE_GETFPREGS = 14
PTRACE_SETFPREGS = 15
PTRACE_ATTACH = 16
PTRACE_DETACH = 17
PTRACE_GETFPXREGS = 18
PTRACE_SETFPXREGS = 19
PTRACE_SYSCALL = 24

ADDR_NO_RANDOMIZE = 0x0040000

# struct of all registers
class Regs(Structure):
    _fields_ = [
        ("r15", c_ulong),
        ("r14", c_ulong),
        ("r13", c_ulong),
        ("r12", c_ulong),
        ("rbp", c_ulong),
        ("rbx", c_ulong),
        ("r11", c_ulong),
        ("r10", c_ulong),
        ("r9", c_ulong),
        ("r8", c_ulong),
        ("rax" , c_ulong),
        ("rcx" , c_ulong),
        ("rdx" , c_ulong),
        ("rsi" , c_ulong),
        ("rdi" , c_ulong),
        ("orig_rax" , c_ulong),
        ("rip" , c_ulong),
        ("cs" , c_ulong),
        ("eflags" , c_ulong),
        ("rsp" , c_ulong),
        ("ss" , c_ulong),
        ("fs_base" , c_ulong),
        ("gs_base" , c_ulong),
        ("ds" , c_ulong),
        ("es" , c_ulong),
        ("fs" , c_ulong),
        ("gs" , c_ulong)
        ]

libc = CDLL('libc.so.6')
ptrace = libc.ptrace

class Ptrace_exception(Exception):
    pass

get_errno_loc = libc.__errno_location
get_errno_loc.restype = POINTER(c_int)

def personality():
    libc.personality(ADDR_NO_RANDOMIZE)

# start tracing after current process
def traceme():
    libc.personality(ADDR_NO_RANDOMIZE)
    status = ptrace(PTRACE_TRACEME, 0, None, None)

    if status < 0:
        raise Ptrace_exception()

# continue executaion of stopped process
def continue_executaion(pid):
    status = ptrace(PTRACE_CONT, pid, None, None)

    if status < 0:
        raise Ptrace_exception()

# get registers of a process
def get_regs(pid):
    regs = Regs()
    status = ptrace(PTRACE_GETREGS, pid, None, byref(regs))

    if status < 0:
        raise Ptrace_exception()
    return regs

# read data from the process at address addr
def read_data(pid, addr):
    return ptrace(PTRACE_PEEKDATA, pid, addr, None)


# write data to the process at address addr
def write_data(pid, addr, data):
    status = ptrace(PTRACE_POKEDATA, pid, addr, data)

    if status < 0:
        e = get_errno_loc()[0]
        print(e)
        raise OSError(e)
        #raise Ptrace_exception()

# perform one instruction
def single_step(pid):
    status = ptrace(PTRACE_SINGLESTEP, pid, None, None)

    if status < 0:
        raise Ptrace_exception()