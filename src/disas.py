import sys
import capstone
import elfReader
import function_info
import instruction

CPU_ARCH = capstone.CS_ARCH_X86
CPU_MODE = capstone.CS_MODE_64

# class for disassembling ELF file
class Disassembler:
    def __init__(self):
        self.disassembler = capstone.Cs(CPU_ARCH, CPU_MODE) # init capstone disassembler
        
    # disassemble one function, and return a functionInfo object
    def disassemble_func(self, func_name, func_addr, code):
        disassembled_code = []
        disas_generator = self.disassembler.disasm(code, func_addr)

        end_addr = func_addr
        i = next(disas_generator, None)
        while i != None and i.mnemonic != 'ret': # disassemble until ret command reached
            
            disassembled_code.append(instruction.Instruction(i))
            end_addr = i.address
            i = next(disas_generator, None)

        end_addr = None
        if i != None:
            disassembled_code.append(i)
            end_addr = i.address

        func = function_info.FunctionInfo(func_name, func_addr, end_addr, disassembled_code)
        return func