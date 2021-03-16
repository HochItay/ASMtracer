from tracer import Tracer

import elfReader
import disas
import os
import instruction
import funcEntry

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

        self.load_address, self.code = self.get_mem_by_region(os.path.abspath(file))
        self.__init_functions()
        self.__init_breakpoints()
        self.__calling_stack = []

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
                        instruction.set_note(f'({called_func[0]})')
                except:
                    pass

    # return list of function names in the ELF file
    def get_function_names(self):
        return list(self.function_by_name.keys())

    # get function by its name
    def get_function(self, name):
        return self.function_by_name[name]

    # initialize breakpoints at all call/ret commands
    def __init_breakpoints(self):
        for func in self.function_by_name.values():
            for instruction in func.instructions:
                if instruction.mnemonic == 'call' or instruction.mnemonic == 'ret':
                    self.add_breakpoint(instruction.address)
                    self.__non_user_defined_breakpoints.append(instruction.address)

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

    # this is called after the child process is stopped
    # this function checks what caused the signal
    # and update the calling stack
    def process_event(self):
        try:
            #find current instruction
            rip = self.get_current_instruction()
            instruction = self.get_instruction_by_address(rip)

            # pop the function if current instruction is ret
            if instruction.mnemonic == 'ret':
                self.__calling_stack.pop()

            # push the function if instruction is call
            if instruction.mnemonic == 'call':
                self.__calling_stack.append(funcEntry.FuncEntry(self.find_function_with_address(int(instruction.parameters, 16)), rip))
        except:
            pass

    # overide single step
    def single_step(self):
        self.process_event()
        super().single_step()
        for func in self.__calling_stack:
            print(func.func.name, end=', ')
        print()
        
        
    # continue the execution until a user defined breakpoint is hitted
    def continue_execution(self):
        # skip one instruction if current instruction have breakpoint
        if self.get_current_instruction() in self.__user_defined_breakpoints:
            self.single_step()

        while self.get_current_instruction() not in self.__user_defined_breakpoints:
            self.process_event()
            super().continue_execution()

    # step until out of the current function
    def step_out(self):
        stack_length = len(self.__calling_stack)
        while len(self.__calling_stack) >= stack_length:
            super().continue_execution()
            self.process_event()
