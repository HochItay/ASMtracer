# a wraper for capstone instruction object
class Instruction:
    def __init__(self, i):
        self.address = i.address
        self.mnemonic = i.mnemonic
        self.parameters = i.op_str
        if self.mnemonic == 'ret':
            print('a')
        self.note = ''

    # set note on the instruction
    def set_note(self, note):
        self.note = note

    def __str__(self):
        return f'{hex(self.address)}:\t{self.mnemonic}\t{self.parameters} {self.note}'