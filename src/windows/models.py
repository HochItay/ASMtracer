from PySide2.QtCore import Qt, QAbstractTableModel, QAbstractListModel
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# a model for showing registers value
class RegistersModel(QAbstractListModel):
    
    # get a function that sets the registers list
    # also get dictionary with explenations about the registers
    def __init__(self, set_regs_func, explenations, parent = None):
        QAbstractListModel.__init__(self, parent)
        self.regs = []
        self.prev_regs = []
        self.set_regs_func = set_regs_func
        self.explenations = explenations

    # set the registers table
    def set_regs(self, regs):
        self.prev_regs = self.regs
        self.regs = self.set_regs_func(regs)
        self.layoutChanged.emit()

    def rowCount(self, parent):
        return len(self.regs)

    def flags(self, index):
        return  Qt.ItemIsEnabled

    def data(self, index, role):
        # tooltip for the registers is the explenation about the register
        if role == Qt.ToolTipRole:
            row = index.row()
            if row < len(self.regs):
                register = self.regs[row][0]

            if register in self.explenations:
                return self.explenations[register]

        # yellow backround if register value changed from last time
        #otherwise white
        if role == Qt.BackgroundRole:
            row = index.row()
            if row < len(self.regs):
                if self.regs[row] != self.prev_regs[row]:
                    return QColor('#D9ED92')

                else:
                    return QColor('#ffffff')
              
        # value of the register
        if role == Qt.DisplayRole:    
            row = index.row()
            if row < len(self.regs):
                register = self.regs[row]
                value = '{:0x}'.format(register[1])

                
                # add spacing
                value_str = ''
                space = 1
                for c in value:
                    value_str += c
                    if space % 4 == 0:
                        value_str += ' '
                    space += 1


                return f'{register[0]} {value_str}'


# functions that set registers
# -----------------------------------------------------------------------------
def parameters_set_regs(regs):
    return [('rdi', regs.rdi), ('rsi', regs.rsi), ('rdx', regs.rbp), ('rcx', regs.rcx), ('r8 ', regs.r8), ('r9 ', regs.r9)]

def caller_set_regs(regs):
    return [('rax', regs.rax), ('r10', regs.r10), ('r11', regs.r11)]

def callee_set_regs(regs):
    return [('rbx', regs.rbx), ('r12', regs.r12), ('r13', regs.r13), ('r14', regs.r14), ('r15', regs.r15)]

def special_set_regs(regs):
    return [('rip', regs.rip), ('rsp', regs.rsp), ('rbp', regs.rbp)]

def flags_set_regs(regs):
    flags = [('CF', regs.eflags & 0b1), ('ZF', regs.eflags & 0b1000000), ('SF', regs.eflags & 0b10000000), ('OF', regs.eflags & 0b100000000000)]
    res = []
    for name, value in flags:
        if value == 0:
            res.append((name, 0))
        else:
            res.append((name, 1))

    return res
# --------------------------------------------------------------------------------


# a model for frame of a funcion stack
class StackFrameModel(QAbstractListModel):
    
    def __init__(self,parent = None):
        QAbstractListModel.__init__(self, parent)
        self.__frame = []
        self.__return_address_index = 0
        self.__rbp_index = 1
        self.__size = 8

    # set the frame
    # also gets the index of the return address and the rbp in the frame
    def set_frame(self, frame, return_address, rbp):
        self.__frame = frame
        self.__return_address_index = return_address
        self.__rbp_index = rbp
        self.layoutChanged.emit()

    # set the frame size
    def set_size(self, size):
        self.__size = size
        self.layoutChanged.emit()

    def rowCount(self, parent):
        return len(self.__frame)


    def flags(self, index):
        return  Qt.ItemIsEnabled


    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        # tooltip that indicates the address relative to rbp
        if role == Qt.ToolTipRole:
            row = index.row()
            if row == 0:
                return 'return address'
            if row == 1:
                return 'rbp'

            if row < (len(self.__frame) - 16)/ self.__size + 2:
                row -= 1
                return f'rbp - {hex(self.__size * row)}'
                

        if role == Qt.BackgroundRole:
            row = index.row()

            if row == 0:
                # green for return address
                return QColor('#76C893')
            elif row == 1:
                # yellow for rbp
                return QColor('#D9ED92')

            elif row < (len(self.__frame) - 16)/ self.__size + 2:
                    # blue for the rest
                    return QColor('#34A0A4')
              
        # value of the stack
        if role == Qt.DisplayRole:
            row = index.row()

            if row < (len(self.__frame) - 16)/ self.__size + 2:
                if row == 0 or row == 1:
                    idx = int(len(self.__frame) / 8) - (row + 1)
                    value = int.from_bytes(self.__frame[idx * 8: (idx + 1) * 8], byteorder='little', signed=False)
                else:
                    if self.__size == 4:
                        row +=2
                    if self.__size == 2:
                        row +=4
                    # normalize index since the stack is upside down
                    idx = int(len(self.__frame) / self.__size) - (row + 1)
                    value = int.from_bytes(self.__frame[idx * self.__size: (idx + 1) * self.__size], byteorder='little', signed=False)

                # determine format
                if row == 0 or row == 1:
                    value = '{:016x}'.format(value)
                else:
                    if self.__size == 8:
                        value = '{:016x}'.format(value)
                    elif self.__size == 4:
                        value = '{:08x}'.format(value)
                    elif self.__size == 2:
                        value = '{:04x}'.format(value)

                # add spacing
                value_str = ''
                space = 1
                for c in value:
                    value_str += c
                    if space % 4 == 0:
                        value_str += ' '
                    space += 1

                return value_str
                    