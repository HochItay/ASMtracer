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

    # disassemble one function
    def disassemble_func(self, func):
        if not func in self.functions:
            raise Exception('function ' + func + ' does not exist')
        
        disassembled_code = ''
        func_addr = self.functions[func]
        disas_generator = self.disassembler.disasm(self.code[func_addr - self.start_addr:], func_addr)

        i = next(disas_generator, None)
        while i != None and i.mnemonic != 'ret': # disassemble until ret command reached
            disassembled_code += "0x%x:\t%s\t%s\n" %(i.address, i.mnemonic, i.op_str)
            i = next(disas_generator, None)

        if i != None:
            disassembled_code += "0x%x:\t%s\t%s\n" %(i.address, i.mnemonic, i.op_str)

        return disassembled_code

    # return list of all functions
    def get_functions(self):
        return self.functions.keys()

    def __del__(self):
        self.file.close()

        
if __name__ == '__main__':
    d = Disassembler('a.out')
    print(d.disassemble_func('main'))