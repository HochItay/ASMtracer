from elftools.elf.elffile import ELFFile

SYMBOL_SECTION = '.symtab'
CODE_SECTION = '.text'

# a class for parsing ELF files
class ELFReader:
    def __init__(self, elf_file):
        self.__file = open(elf_file, 'rb')
        self.__elf_file = ELFFile(self.__file)
        if self.__elf_file.has_dwarf_info():
            self.__dwarf = self.__elf_file.get_dwarf_info()

    # look at the symbol table for all functions name and adresses
    # return: a list of tuples, each contain a function name and address
    def functions_address(self):
        functions = []

        # look at the symbol table
        symb_tbl = self.__elf_file.get_section_by_name(SYMBOL_SECTION)
        for symbol in symb_tbl.iter_symbols():
            # take only functions symbols in the text section(so functions from shared library not include)
            if type(symbol['st_shndx']) is int:
                if symbol['st_info']['type'] == 'STT_FUNC' and self.__elf_file.get_section(symbol['st_shndx']).name == CODE_SECTION:
                    functions.append((symbol.name, symbol['st_value']))

        return functions

    # return data of a segment by its name
    def get_section_data(self, section):
        return self.__elf_file.get_section_by_name(section).data()

    # return starting address of a segment by its name
    def get_section_address(self, section):
        return self.__elf_file.get_section_by_name(section)['sh_addr']

    