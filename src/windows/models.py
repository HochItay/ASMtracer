from PySide2.QtCore import Qt, QAbstractTableModel, QAbstractListModel
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# a model for showing registers value
class RegistersModel(QAbstractTableModel):
    
    def __init__(self, regs, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.headers = ['general', 'parameters', 'flags']
        self.regs = []
        self.prev_regs = []
        self.set_regs(regs)

    # set the registers table
    def set_regs(self, regs):
        self.layoutChanged.emit()
        self.prev_regs = self.regs
        self.regs = [
            [('rax', regs.rax), ('rbx', regs.rbx), ('rbp', regs.rbp), ('rip', regs.rip), ('rsp', regs.rsp)],
            [('rdi', regs.rdi), ('rsi', regs.rsi), ('rdx', regs.rbp), ('rcx', regs.rcx), ('r8', regs.r8), ('r9', regs.r9)] 
        ]
        self.layoutChanged.emit()

    def rowCount(self, parent):
        return 7
    
    
    def columnCount(self, parent):
        return 2


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
            column = index.column()
            if column < len(self.regs) and row < len(self.regs[column]):
                if self.regs[column][row] != self.prev_regs[column][row]:
                    return QColor('#ffff00')

                else:
                    return QColor('#ffffff')
              
        # value of the register
        if role == Qt.DisplayRole:    
            row = index.row()
            column = index.column()
            if column < len(self.regs) and row < len(self.regs[column]):
                register = self.regs[column][row]
                value = '{:016x}'.format(register[1])
                return f'{register[0]} {value}'

    def headerData(self, section, orientation, role):
        
        if role == Qt.DisplayRole:
            
            if orientation == Qt.Horizontal:
                
                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"

# a model for frame of a funcion stack
class StackFrameModel(QAbstractListModel):
    
    def __init__(self,parent = None):
        QAbstractListModel.__init__(self, parent)
        self.__frame = []

    # set the 
    def set_frame(self, frame):
        self.layoutChanged.emit()
        self.__frame = frame

    def rowCount(self, parent):
        return len(self.__frame)


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

        if role == Qt.BackgroundRole:
            pass
              
        # value of the register
        if role == Qt.DisplayRole:
            if index.row() < len(self.__frame):
                return '{:016x}'.format(self.__frame[index.row()])

    def headerData(self, section, orientation, role):
        
        if role == Qt.DisplayRole:
            
            if orientation == Qt.Horizontal:
                
                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"