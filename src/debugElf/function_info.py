# a basic class that store information about functions in the tracee
class FunctionInfo:
    # parameters:
    # name: name of the function
    # start_addr: address of the first instruction in the function
    # end_addr: address of the last instruction in the function
    # instructions: list of instructions
    # text(optimal): list of strings representing the instructions
    def __init__(self, name, start_addr, end_addr, instructions, text=None):
        self.name = name
        self.start_addr = start_addr
        self.end_addr = end_addr
        self.instructions = instructions

    def set_text(self, text):
        self.text = text

    # return the index of an instruction by its address
    def get_instruction_index_by_address(self, address):
        for i, instruction in enumerate(self.instructions):
            if instruction.address == address:
                return i