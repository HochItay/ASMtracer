from .tracer import Tracer

from . import elfReader
from . import disas
from . import tracer
import os
from . import instruction
from . import funcEntry
import re

# list of known compiler defined functions
COMPILER_FUNCS = ['frame_dummy', 'register_tm_clones', 'deregister_tm_clones']

# A class for combining tracer, disassembler and ELFReader to
# one debugger for ELF files
class Debugger(Tracer):
    def __init__(self, file):
        Tracer.__init__(self, file)
        self.__disas = disas.Disassembler()
        self.__reader = elfReader.ELFReader(file)

        self.functions = self.__reader.functions_address()
        self.function_by_name = {} # dictionary that maps function name to its information
        self.function_by_addr = {} # dictionary that maps function address to its information

        # addresses of all the user defined breakpints
        self.__user_defined_breakpoints = []
        self.__non_user_defined_breakpoints = []

        # if file is executale, the load address is 0
        if self.__reader.is_exec():
            self.load_address = 0
            self.code = self.read_from_memory(self.__reader.get_section_address(elfReader.CODE_SECTION), self.__reader.get_section_size(elfReader.CODE_SECTION))
        else:
            self.load_address, self.code = self.get_mem_by_region(os.path.abspath(file))

        self.__init_functions()

        # execute until main
        self.place_breakpoint(self.get_function('main').start_addr)
        self.continue_execution()
        self.clear_breakpoint(self.get_function('main').start_addr)

        # save the frame start of main
        self.__main_frame_start = self.get_registers().rsp

    # initialize all information about all functions, inclue assembly code
    def __init_functions(self):
        for name, addr in self.functions:
            if not (name.startswith('_') or name in COMPILER_FUNCS):
                func = self.__disas.disassemble_func(name, self.load_address + addr, self.code[addr:], [self.load_address + func[1] for func in self.functions])
                self.function_by_name[name] = func
                self.function_by_addr[self.load_address + addr] = func

                for i in func.instructions:
                    self.add_note_on_instruction(i)

    # add a note on instruction
    # currrent aviable notes:
    # 1. add function name to call instructions
    def add_note_on_instruction(self, instruction):
        # support mapping call instruction to the called function
        if instruction.mnemonic == 'call':
                try:
                    call_addr = int(instruction.parameters, 0)
                    called_func = next((func for func in self.functions if func[1] + self.load_address == call_addr), None)
                    if called_func != None:
                        instruction.set_note(called_func[0])
                except:
                    pass
        # parse experssions in the form of [rip + 0xXXX]
        find = re.search('\[rip \+ .+\]', instruction.parameters)
        if find:
            pos = find.span()
            str_part = find.string[pos[0]: pos[1]]
            addr = instruction.address + int(str_part[7:-1] ,16) + instruction.size
            instruction.set_note(hex(addr))
        

    # return list of function names in the ELF file
    def get_function_names(self):
        return list(self.function_by_name.keys())

    # get function by its name
    def get_function(self, name):
        return self.function_by_name[name]


    # place a breakpoint at the given address
    def place_breakpoint(self, addr):
        self.__user_defined_breakpoints.append(addr)
        if addr not in self.__non_user_defined_breakpoints:
            self.add_breakpoint(addr)

    # clear a breakpoint
    def clear_breakpoint(self, addr):
        self.__user_defined_breakpoints.remove(addr)
        if addr not in self.__non_user_defined_breakpoints:
            self.remove_breakpoint(addr)
    
    # find the function that contains a given address and return it
    # or None if no such function exists
    def find_function_with_address(self, address):
        for func in self.function_by_name.values():
            if func.start_addr <= address <= func.end_addr:
                return func

        return None

    # get an instruction by its address
    def get_instruction_by_address(self, address):
        func = self.find_function_with_address(address)
        index = func.get_instruction_index_by_address(address)
        return func.instructions[index]


    # overide single step
    def single_step(self):
        # get current instruction
        rip = self.get_current_instruction()
        func = self.find_function_with_address(rip)
        index = func.get_instruction_index_by_address(rip)
        current_instruction = func.instructions[index]

        # if external function, step over
        if current_instruction.mnemonic == 'call' and int(current_instruction.parameters, 16) not in self.function_by_addr:
            self.step_over()
        else:
            super().single_step()
        
        
    # continue the execution until a user defined breakpoint is hitted
    def continue_execution(self):
        # skip one instruction if current instruction have breakpoint
        if self.get_current_instruction() in self.__user_defined_breakpoints:
            self.single_step()

        super().continue_execution()

    # step until out of the current function
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

        # we stop on breakpoint if it is located at the return address
        # since we might reach to the return address before finishing
        # the current function (with recursion), we will also check the
        # stack is smaller than the size when the function was called
        while self.get_current_instruction() != return_address or self.get_registers().rsp < base_pointer:
            self.continue_execution()

        if should_remove_bp:
            self.remove_breakpoint(return_address)

    # single step, but step over 'call' commands
    def step_over(self):
        # find the current instruction
        rip = self.get_current_instruction()
        func = self.find_function_with_address(rip)
        index = func.get_instruction_index_by_address(rip)
        current_instruction = func.instructions[index]

        # if current instruction is not call, step regulary
        if current_instruction.mnemonic != 'call':
            self.single_step()
            return

        # if current instruction is call, place temporary breakpoint on next instruction
        next_instruction_address = func.instructions[index+1].address
        
        should_remove_bp = False
        # place breakpoint at the next instruction address
        if next_instruction_address not in self.breakpoints:
            self.place_breakpoint(next_instruction_address)
            should_remove_bp = True

        stack_pointer = self.get_registers().rsp
        # to avoid cases where we reach to the next command on another frame
        # because of recursion, we will make sure the stack size is the same
        while self.get_current_instruction() != next_instruction_address or stack_pointer > self.get_registers().rsp:
            self.continue_execution()

        if should_remove_bp:
            self.remove_breakpoint(next_instruction_address)

    # get the call stack
    def call_stack(self):
        stack = []
        regs = self.get_registers()
        curr_func = self.find_function_with_address(regs.rip)
        bp = regs.rbp

        if curr_func.name == 'main':
            stack.insert(0, funcEntry.FuncEntry(curr_func, None, self.__main_frame_start))
            return stack

        addr = self.read_word_from_memory(bp + 8)
        stack.append(funcEntry.FuncEntry(curr_func, addr, bp + 8))
        while curr_func.name != 'main':
            curr_func = self.find_function_with_address(addr)
            if curr_func.name == 'main':
                stack.insert(0, funcEntry.FuncEntry(curr_func, None, self.__main_frame_start))

        return stack

