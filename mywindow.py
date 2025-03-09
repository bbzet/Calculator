from calcuil import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

class CalculatorModel(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_input = ""
        self.full_expression = ""
        self.result = 0
        self.current_operator = ""

        self.btn_0.clicked.connect(lambda: self.digit_pressed("0"))
        self.btn_1.clicked.connect(lambda: self.digit_pressed("1"))
        self.btn_2.clicked.connect(lambda: self.digit_pressed("2"))
        self.btn_3.clicked.connect(lambda: self.digit_pressed("3"))
        self.bt_4.clicked.connect(lambda: self.digit_pressed("4"))
        self.btn_5.clicked.connect(lambda: self.digit_pressed("5"))
        self.btn_6.clicked.connect(lambda: self.digit_pressed("6"))
        self.btn_7.clicked.connect(lambda: self.digit_pressed("7"))
        self.btn_8.clicked.connect(lambda: self.digit_pressed("8"))
        self.btn_9.clicked.connect(lambda: self.digit_pressed("9"))
        self.btn_dot.clicked.connect(lambda: self.digit_pressed("."))
        self.btn_add.clicked.connect(lambda: self.binary_operator_pressed("+"))
        self.btn_sub.clicked.connect(lambda: self.binary_operator_pressed("-"))
        self.btn_mult.clicked.connect(lambda: self.binary_operator_pressed("*"))
        self.btn_div.clicked.connect(lambda: self.binary_operator_pressed("/"))
        self.btn_equal.clicked.connect(self.equal_pressed)
        self.btn_clear.clicked.connect(self.clear_pressed)
        self.btn_backspace.clicked.connect(self.back_pressed)

        self.update_display()

    def digit_pressed(self, digit):
        if digit == "." and "." in self.current_input:
            return
        self.current_input += digit
        self.update_display()

    def update_display(self):
        self.input1.setText(str(self.full_expression + " " + self.current_input))

    def binary_operator_pressed(self, operator):
        if self.current_operator:
            self.equal_pressed()
        self.result = float(self.current_input)
        self.current_operator = operator
        self.full_expression = f'{self.current_input} {self.current_operator}'
        self.current_input = ""
        self.update_display()

    def equal_pressed(self):
        if self.current_operator:
            try:
                result = eval(f"{self.result}{self.current_operator}{self.current_input}")
                self.full_expression = f"{self.full_expression} {self.current_input} = {result}"
                self.current_input = str(result)
                self.current_operator = ""
                self.full_expression = ""
                self.update_display()
            except Exception as e:
                self.full_expression = "Error"
                self.current_input = ""
                self.update_display()

    def clear_pressed(self):
        self.current_input = ""
        self.full_expression = ""
        self.result = 0
        self.current_operator = ""
        self.update_display()

    def back_pressed(self):
        self.current_input = self.current_input[:-1]
        self.update_display()