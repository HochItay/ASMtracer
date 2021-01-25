from tracer import Tracer

import elfReader
import disas
import os
import instruction

# A class for combining tracer, disassembler and ELFReader to
# one debugger for ELF files
class Debugger(Tracer):
    def __init__(self, file):
        Tracer.__init__(self, file)
        self.disas = disas.Disassembler()
        self.reader = elfReader.ELFReader(file)

        self.functions = self.reader.functions_address()
        self.function_by_name = {} # dictionary that maps function name to its information
        self.functions_by_addr = {} # dictionary that maps function address to its information

        self.load_address, self.code = self.get_mem_by_region(os.path.abspath(file))
        self.init_functions()

    # initialize all information about all functions, inclue assembly code
    def init_functions(self):
        for name, addr in self.functions:
            func = self.disas.disassemble_func(name, self.load_address + addr, self.code[addr:])
            self.function_by_name[name] = func
            self.functions_by_addr[self.load_address + addr] = func

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
                        instruction.set_note(f'({called_func})')
                except:
                    pass

    # return list of function names in the ELF file
    def get_function_names(self):
        return self.function_by_name.keys()

    # get function by its name
    def get_function(self, name):
        return self.function_by_name[name]