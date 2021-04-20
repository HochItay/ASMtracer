from PySide2.QtCore import Qt, QAbstractTableModel, QAbstractListModel
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# a model for showing registers value
class RegistersModel(QAbstractListModel):
    
    # get a function that sets the registers list
    def __init__(self, set_regs_func, parent = None):
        QAbstractListModel.__init__(self, parent)
        self.regs = []
        self.prev_regs = []
        self.set_regs_func = set_regs_func

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
        # tooltip for the registers
        if role == Qt.ToolTipRole:
            row = index.row()
            column = index.column()

            if column == 0 and row == 3:
                return 'rip holds the address of the current instruction'
            return 'a tooltip'

        # yellow backround if register value changed from last time
        #otherwise white
        if role == Qt.BackgroundRole:
            row = index.row()
            if row < len(self.regs):
                if self.regs[row] != self.prev_regs[row]:
                    return QColor('#ffff00')

                else:
                    return QColor('#ffffff')
              
        # value of the register
        if role == Qt.DisplayRole:    
            row = index.row()
            if row < len(self.regs):
                register = self.regs[row]
                value = '{:0x}'.format(register[1])
                return f'{register[0]} {value}'


# functions that set registers
# -----------------------------------------------------------------------------
def parameters_set_regs(regs):
    return [('rdi', regs.rdi), ('rsi', regs.rsi), ('rdx', regs.rbp), ('rcx', regs.rcx), ('r8', regs.r8), ('r9', regs.r9)]

def caller_set_regs(regs):
    return [('rax', regs.rax), ('r10', regs.r10), ('r11', regs.r11)]

def callee_set_regs(regs):
    return [('rbx', regs.rbx), ('r12', regs.r12), ('r13', regs.r13), ('r14', regs.r14), ('r15', regs.r15)]

def special_set_regs(regs):
    return [('rip', regs.rip), ('rsp', regs.rsp), ('rbp', regs.rbp)]

def flags_set_regs(regs):
    return [('rdi', regs.rdi), ('rsi', regs.rsi), ('rdx', regs.rbp), ('rcx', regs.rcx), ('r8', regs.r8), ('r9', regs.r9)]
# --------------------------------------------------------------------------------


# a model for frame of a funcion stack
class StackFrameModel(QAbstractListModel):
    
    def __init__(self,parent = None):
        QAbstractListModel.__init__(self, parent)
        self.__frame = []
        self.__size = 8

    # set the frame
    def set_frame(self, frame):
        self.__frame = frame
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
        if role == Qt.ToolTipRole:
            pass

        if role == Qt.BackgroundRole:
            if index.row() < len(self.__frame) / self.__size:
                return QColor('#1DC913')
              
        # value of the register
        if role == Qt.DisplayRole:
            if self.__size == 8:
                if index.row() < len(self.__frame) / 8:
                    value = int.from_bytes(self.__frame[index.row() * 8: (index.row() + 1) * 8], byteorder='little', signed=False)
                    return '{:016x}'.format(value)

            if self.__size == 4:
                if index.row() < len(self.__frame) / 4:
                    value = int.from_bytes(self.__frame[index.row() * 4: (index.row() + 1) * 4], byteorder='little', signed=False)
                    return '{:08x}'.format(value)

            if self.__size == 2:
                if index.row() < len(self.__frame) / 2:
                    value = int.from_bytes(self.__frame[index.row() * 2: (index.row() + 1) * 2], byteorder='little', signed=False)
                    return '{:04x}'.format(value)

    def headerData(self, section, orientation, role):
        
        if role == Qt.DisplayRole:
            
            if orientation == Qt.Horizontal:
                
                if index.row() < len(self.__frame) / self.__size:
                    return self.headers[section]
                else:
                    return "not implemented"