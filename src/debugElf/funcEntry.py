# one entry in the calling stack
class FuncEntry:
    def __init__(self, func, return_addr, frame_start):
        self.func = func # the function itself
        self.return_addr = return_addr # address where the function was called from
        self.frame_start = frame_start # starting address of the frame (points to return address)