from UI.ui_traceWindow import Ui_TraceWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QLabel, QMessageBox, QFileDialog
from PySide2.QtCore import QFile
from PySide2.QtGui import QFont, QIcon, Qt
from .custom_widgets import QInstruction, QStackFunction
from . import models

from debugElf.debugger import Debugger

import sys
import os

class TraceWindow(QMainWindow):
    def __init__(self, file):
        super(TraceWindow, self).__init__()
        
        self.file = file
        self.debugger = Debugger(file)
        self.ui = Ui_TraceWindow()
        self.ui.setupUi(self)
        self.ui.func_combo.addItems(self.debugger.get_function_names())

        self.setWindowTitle(f'tracing {file}')
        
        self.__init_connections()

        self.instructions_by_func = {}
        self.init_instructions()
        self.current_instruction = None
        self.functions = self.debugger.get_function_names()
        self.__is_relative = False

        self.__init_models()

        self.update_display()


    # initialize all connections to  buttons
    def __init_connections(self):
        self.ui.func_combo.currentIndexChanged.connect(lambda: self.show_function(self.ui.func_combo.currentText()))
        self.ui.frame_combo.currentIndexChanged.connect(self.update_frame)
        self.ui.step_btn.clicked.connect(self.single_step)
        self.ui.cont_btn.clicked.connect(self.continue_execution)
        self.ui.step_out_btn.clicked.connect(self.step_out)
        self.ui.step_over_btn.clicked.connect(self.step_over)
        self.ui.get_data_btn.clicked.connect(self.get_data)
        self.ui.relative_address_btn.clicked.connect(self.change_relative_address_mode)
        self.ui.radio_16bit.toggled.connect(lambda: self.frame_model.set_size(2))
        self.ui.radio_32bit.toggled.connect(lambda: self.frame_model.set_size(4))
        self.ui.radio_64bit.toggled.connect(lambda: self.frame_model.set_size(8))
        self.ui.restart_btn.clicked.connect(self.restart)
        self.ui.font_size_spin.valueChanged.connect(self.set_code_size)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.open_file_btn.clicked.connect(self.run_exe)

    # initialize models for views
    def __init_models(self):
        # initialize a dictionary that maps register to its explenation file
        self.regs_explenation = {}
        for filename in os.listdir('resources/registers'):
            with open('resources/registers/' + filename, 'r') as f:
                self.regs_explenation[filename] = f.read()

        regs = self.debugger.get_registers()
        # registers list
        self.regs1_model = models.RegistersModel(models.parameters_set_regs, self.regs_explenation)
        self.ui.regs1_view.setModel(self.regs1_model)

        self.regs2_model = models.RegistersModel(models.caller_set_regs, self.regs_explenation)
        self.ui.regs2_view.setModel(self.regs2_model)

        self.regs3_model = models.RegistersModel(models.callee_set_regs, self.regs_explenation)
        self.ui.regs3_view.setModel(self.regs3_model)

        self.regs4_model = models.RegistersModel(models.special_set_regs, self.regs_explenation)
        self.ui.regs4_view.setModel(self.regs4_model)

        self.regs5_model = models.RegistersModel(models.flags_set_regs, self.regs_explenation)
        self.ui.regs5_view.setModel(self.regs5_model)

        self.regs1_model.set_regs(regs)
        self.regs2_model.set_regs(regs)
        self.regs3_model.set_regs(regs)
        self.regs4_model.set_regs(regs)
        self.regs5_model.set_regs(regs)

        # frame content
        self.frame_model = models.StackFrameModel()
        self.ui.stack_frame.setModel(self.frame_model)

        # tooltips
        with open('resources/explanations/registers', 'r') as f:
                self.ui.label_3.setToolTip(f.read())
        with open('resources/explanations/call_stack', 'r') as f:
                self.ui.label_13.setToolTip(f.read())
        with open('resources/explanations/data_area', 'r') as f:
                self.ui.label_14.setToolTip(f.read())
        with open('resources/explanations/stack_content', 'r') as f:
                self.ui.label_15.setToolTip(f.read())
        with open('resources/explanations/stack_size', 'r') as f:
                self.ui.label_16.setToolTip(f.read())

    # initialize instructions_by_func which maps function name to list of Qinstructions
    def init_instructions(self):
        # initialize a dictionary that maps instruction to its explenation file
        self.explenation_dic = {}
        for filename in os.listdir('resources/instructions'):
            with open('resources/instructions/' + filename, 'r') as f:
                self.explenation_dic[filename] = f.read()

        for func in self.debugger.get_function_names():
            self.instructions_by_func[func] = [QInstruction(i, self.debugger, self.debugger.load_address, self.explenation_dic, self) for i in self.debugger.get_function(func).instructions]

            instruction_list = QListWidget()
            # create a new list widget for that function
            for i in self.instructions_by_func[func]:
                # Create QListWidgetItem
                list_widget = QListWidgetItem()
                # Set size hint
                list_widget.setSizeHint(i.sizeHint())
                list_widget.setFlags(list_widget.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
                instruction_list.addItem(list_widget)
                instruction_list.setItemWidget(list_widget, i)

            self.ui.func_stack.addWidget(instruction_list)

    # set the address mode
    def change_relative_address_mode(self):
        self.__is_relative = not self.__is_relative
        for func_instructions in self.instructions_by_func.values():
            for i in func_instructions:
                i.set_relative_mode(self.__is_relative)

    # set color of instruction at address addr
    def set_color_of_instruction(self, addr, color):
        # search the instruction widget, only in current function
        current_function = self.ui.func_combo.currentText()
        instruction = next((i for i in self.instructions_by_func[current_function] if i.instruction.address == addr), None)

        # highlight current instruction, only if it exists in the original file
        if instruction is not None:
            instruction.set_description_color(color)

    # change the font size of the code
    def set_code_size(self, size):
        for func in self.instructions_by_func:
            for i in self.instructions_by_func[func]:
                i.set_font_size(size)

    # show current instruction
    def show_current_instruction(self):
        self.show_instruction(self.debugger.get_registers().rip)

    # update the call stack
    def update_call_stack(self):
        try:
            # clear the stack
            self.ui.calling_stack.clear()

            call_satck = self.debugger.call_stack()
            for i, func in enumerate(call_satck):
                if i != len(call_satck) - 1:
                    func_in_stack = QStackFunction(func.func, call_satck[i+1].return_addr, self)
                else:
                    func_in_stack = QStackFunction(func.func, self.debugger.get_current_instruction(), self)

                # Create QListWidgetItem
                list_widget = QListWidgetItem()
                # Set size hint
                list_widget.setSizeHint(func_in_stack.sizeHint())
                self.ui.calling_stack.addItem(list_widget)
                self.ui.calling_stack.setItemWidget(list_widget, func_in_stack)
        except:
            pass
    
    # update the content of the current frame
    def update_frame(self):
        try:
            idx = self.ui.frame_combo.currentText().split('-')[0]
            idx = int(idx)

            call_stack = self.debugger.call_stack()

            # look for the start of the frame
            frame_pointer = call_stack[idx].frame_start
            if len(call_stack) == idx + 1:
                stack_pointer = self.debugger.get_registers().rsp

                # add 16 bytes because of the red zone
                content = self.debugger.read_from_memory(stack_pointer - 24, frame_pointer - stack_pointer + 32)
            else:
                stack_pointer = call_stack[idx+1].frame_start
                content = self.debugger.read_from_memory(stack_pointer, frame_pointer - stack_pointer + 8)

            # convert bytes to int list
            frame = content
            self.frame_model.set_frame(frame, 0, 1)
        except Exception as e:
            pass

    # show a certain function on the window
    def show_function(self, func):
        self.ui.func_stack.setCurrentIndex(self.functions.index(func))

    # show a certain instruction on the window and highlight it
    def show_instruction(self, addr):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return
            
        if self.current_instruction is not None:
            self.current_instruction.unlight()

        # search the instruction widget
        current_function = self.debugger.find_function_with_address(addr)
        if current_function.name in self.functions:
            self.ui.func_combo.setCurrentIndex(self.ui.func_combo.findText(current_function.name))
        self.current_instruction = next((i for i in self.instructions_by_func[current_function.name] if i.instruction.address == addr), None)

        # highlight current instruction, only if it exists in the original file
        if self.current_instruction is not None:
            self.current_instruction.highlight()
    
    # step exactly one instruction
    def single_step(self):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return

        self.debugger.single_step()
        self.update_display()
    
    # continue the execution
    def continue_execution(self):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return

        self.debugger.continue_execution()
        self.update_display()

    # update the display to match current program state
    def update_display(self):
        # do nothing if execution is complete
        if not self.debugger.is_running:
            return

        call_stack = self.debugger.call_stack()
        # update the function combo box above the frame
        self.ui.frame_combo.clear()
        frame_functions = [f'{i} - {func.func.name}' for i, func in enumerate(call_stack)]
        self.ui.frame_combo.addItems(frame_functions)

        self.update_frame()

        current_address = self.debugger.get_current_instruction()

        self.show_instruction(current_address)

        # set the function on the stack content to be the current one
        self.ui.frame_combo.setCurrentIndex(self.ui.frame_combo.count() - 1)

        # update models
        regs = self.debugger.get_registers()
        self.regs1_model.set_regs(regs)
        self.regs2_model.set_regs(regs)
        self.regs3_model.set_regs(regs)
        self.regs4_model.set_regs(regs)
        self.regs5_model.set_regs(regs)
        self.update_call_stack()

    # step out of current function
    def step_out(self):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return

        self.debugger.step_out()
        self.update_display()

    # step out of current function
    def step_over(self):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return

        self.debugger.step_over()
        self.update_display()

    # get data from certain address
    def get_data(self):
        # check if execution ended
        if not self.debugger.is_running:
            self.execution_ended_dialog()
            return

        self.ui.data_area.clear()

        # get number of bytes to read
        num_bytes_str = self.ui.num_bytes_line_edit.text()
        try:
            num_bytes = int(num_bytes_str)
        except:
            self.ui.data_area.setText(f"{num_bytes_str} is not a number")
            return
        
        # get address to read from
        address_str = self.ui.address_line_edit.text()
        try:
            address = int(address_str, 16)
        except:
            self.ui.data_area.setText(f"{address_str} is not an hexadecimal number")
            return

        # read the data itself
        try:
            if self.__is_relative:
                data = self.debugger.read_from_memory(address + self.debugger.load_address, num_bytes)
            else:
                data = self.debugger.read_from_memory(address, num_bytes)
            self.show_data(data)

        except Exception as e:
            print(e)
            self.ui.data_area.setText(f"{address_str} is not a valid address")
            return
    
    # show data on the data area
    def show_data(self, data):
        text = ''
        for i in range(0, len(data) - (len(data) % 8), 8):
            ascii_data = ''
            hex_data = ''
            # convert 8 bytes to ascii
            for j in range(8):
                if 0 < data[i + j] < 128:
                    ascii_data += chr(data[i + j])
                else:
                    ascii_data += '.'
                c = hex(data[i + j])[2:]
                if len(c) < 2:
                    c += ' '
                hex_data += c + ' '

            text += hex_data + '\t' + ascii_data + '\n'

        ascii_data = ''
        hex_data = ''
        i = len(data) - (len(data) % 8)
        # convert 8 bytes to ascii
        for j in range(len(data) % 8):
            if 0 < data[i + j] < 128 and 1==0:
                ascii_data += chr(data[i + j])
            else:
                ascii_data += '.'
            c = hex(data[i + j])[2:]
            if len(c) < 2:
                c += ' '
            hex_data += c + ' '

        text += hex_data + '\t' + ascii_data + '\n'
            
        self.ui.data_area.setText(text)

    # open a message box that notify the execution has ended
    def execution_ended_dialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("ASMtracer")
        msg.setText("The execution has ended!")
        x = msg.exec_()

    # restart the program
    def restart(self):
        del self.debugger
        self.window = TraceWindow(self.file)
        self.window.show()
        self.close()

    # open file dialog to choose a file
    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'open executable file', r'\\')
        return file_name

    # start the execution of the executable
    def run_exe(self):
        filename = self.choose_file()

        # check if file exist
        if not os.path.isfile(filename):
            #self.ui.warning_lbl.setText('file not exist')
            return

        # check file is really ELF by reading the magic
        with open(filename, 'rb') as f:
            magic = f.read(4)
            # ELF magic is '0x7f 0x45 0x4c 0x46'
            if magic != b'\x7f\x45\x4c\x46':
                msg = QMessageBox()
                msg.setWindowTitle("ASMtracer")
                msg.setText('only 64-bit ELF format is supported')
                x = msg.exec_()
                return

        self.window = TraceWindow(filename)
        self.window.show()
        self.close()
