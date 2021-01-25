# a wraper for capstone instruction object
class Instruction:
    def __init__(self, i):
        self.address = i.address
        self.mnemonic = i.mnemonic
        self.parameters = i.op_str
        self.note = ''

    # set note on the instruction
    def set_note(self, note):
        self.note = note

    def __str__(self):
        return "0x%x:\t%s\t%s %s\n" %(self.address, self.mnemonic, self.parameters, self.note)