from tracer import Tracer

import elfReader
import disas
import os
import instruction

# list of known compiler defined functions
COMPILER_FUNCS = ['frame_dummy', 'register_tm_clones', 'deregister_tm_clones']

# A class for combining tracer, disassembler and ELFReader to
# one debugger for ELF files
class Debugger(Tracer):
    def __init__(self, file):
        Tracer.__init__(self, file)
        self.disas = disas.Disassembler()
        self.reader = elfReader.ELFReader(file)

        self.functions = self.reader.functions_address()
        self.function_by_name = {} # dictionary that maps function name to its information
        self.function_by_addr = {} # dictionary that maps function address to its information

        self.load_address, self.code = self.get_mem_by_region(os.path.abspath(file))
        self.init_functions()

    # initialize all information about all functions, inclue assembly code
    def init_functions(self):
        for name, addr in self.functions:
            if not (name.startswith('_') or name in COMPILER_FUNCS):
                func = self.disas.disassemble_func(name, self.load_address + addr, self.code[addr:], [self.load_address + func[1] for func in self.functions])
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

    # find the function that contains a given address and return it
    # or None if no such function exists
    def find_function_with_address(self, address):
        for func in self.function_by_name.values():
            if func.start_addr <= address <= func.end_addr:
                return func

        return None

    # single step, but skip call commands
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

        while self.get_current_instruction() != next_instruction_address:
            self.continue_execution()

        if should_remove_bp:
            self.remove_breakpoint(next_instruction_address)
