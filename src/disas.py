import sys
from elftools.elf.elffile import ELFFile
import capstone

CPU_ARCH = capstone.CS_ARCH_X86
CPU_MODE = capstone.CS_MODE_64

# class for disassembling ELF file
class Disassembler:
    def __init__(self, file):
        self.file = open(file, 'rb')
        self.elf_file = ELFFile(self.file)
        self.functions = self.init_functions_address()
        self.disas_cache = {}

        code_section = self.elf_file.get_section_by_name('.text')
        self.code = code_section.data() # opcodes of the text section instructions
        self.start_addr = code_section['sh_addr'] # address of the code section
        self.disassembler = capstone.Cs(CPU_ARCH, CPU_MODE) # init capstone disassembler

    # look at the symbol table for all functions name and adresses
    # return: a dictionary that maps function name to its virtual address
    def init_functions_address(self):
        functions = {}

        # look at the symbol table
        symb_tbl = self.elf_file.get_section_by_name('.symtab')
        for symbol in symb_tbl.iter_symbols():
            # take only functions symbols
            if symbol['st_info']['type'] == 'STT_FUNC':
                functions[symbol.name] = symbol['st_value']

        return functions

    # parse an instruction and return a textual representation of it
    def parse_instruction(self, instruction):
        # support mapping call instruction to the called function
        if instruction.mnemonic == 'call':
                try:
                    call_addr = int(instruction.op_str, 0)
                    if call_addr in self.functions.values():
                        called_func = list(self.functions.keys())[list(self.functions.values()).index(call_addr)]
                        return "0x%x:\t%s\t%s (%s)\n" %(instruction.address, instruction.mnemonic, instruction.op_str, called_func)
                except:
                    pass

        return "0x%x:\t%s\t%s\n" %(instruction.address, instruction.mnemonic, instruction.op_str)

    # disassemble one function, return a list of strings that represents instructions
    def disassemble_func(self, func):
        # look for assembly code in the cache
        if func in self.disas_cache:
            return self.disas_cache[func]

        if not func in self.functions:
            raise Exception('function ' + func + ' does not exist')
        
        disassembled_code = []
        func_addr = self.functions[func]
        disas_generator = self.disassembler.disasm(self.code[func_addr - self.start_addr:], func_addr)

        i = next(disas_generator, None)
        while i != None and i.mnemonic != 'ret': # disassemble until ret command reached
            
            disassembled_code.append(self.parse_instruction(i))
            i = next(disas_generator, None)

        if i != None:
            disassembled_code.append(self.parse_instruction(i))

        self.disas_cache[func] = disassembled_code
        return disassembled_code

    # return list of all functions
    def get_functions(self):
        return self.functions.keys()

    def __del__(self):
        self.file.close()
