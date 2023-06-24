import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')


        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setMaxLength(25)

        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_dot = QPushButton('.')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_clear = QPushButton('C')
        self.button_equal = QPushButton('=')
        self.button_power = QPushButton('x^2')

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)
        grid.addWidget(self.button_clear, 1, 0, 1, 2)
        grid.addWidget(self.button_divide, 1, 3)
        grid.addWidget(self.button_multiply, 2, 3)
        grid.addWidget(self.button_minus, 3, 3)
        grid.addWidget(self.button_equal, 5, 3)
        grid.addWidget(self.button_plus, 4, 3)
        grid.addWidget(self.button_power, 1, 2)
        grid.addWidget(self.button_7, 2, 0)
        grid.addWidget(self.button_8, 2, 1)
        grid.addWidget(self.button_9, 2, 2)
        grid.addWidget(self.button_4, 3, 0)
        grid.addWidget(self.button_5, 3, 1)
        grid.addWidget(self.button_6, 3, 2)
        grid.addWidget(self.button_1, 4, 0)
        grid.addWidget(self.button_2, 4, 1)
        grid.addWidget(self.button_3, 4, 2)
        grid.addWidget(self.button_0, 5, 0, 1, 2)
        grid.addWidget(self.button_dot, 5, 2)

        self.setLayout(grid)

        self.button_0.clicked.connect(lambda: self.digit_clicked('0'))
        self.button_1.clicked.connect(lambda: self.digit_clicked('1'))
        self.button_2.clicked.connect(lambda: self.digit_clicked('2'))
        self.button_3.clicked.connect(lambda: self.digit_clicked('3'))
        self.button_4.clicked.connect(lambda: self.digit_clicked('4'))
        self.button_5.clicked.connect(lambda: self.digit_clicked('5'))
        self.button_6.clicked.connect(lambda: self.digit_clicked('6'))
        self.button_7.clicked.connect(lambda: self.digit_clicked('7'))
        self.button_8.clicked.connect(lambda: self.digit_clicked('8'))
        self.button_9.clicked.connect(lambda: self.digit_clicked('9'))
        self.button_dot.clicked.connect(lambda: self.digit_clicked('.'))
        self.button_plus.clicked.connect(lambda: self.operation_clicked('+'))
        self.button_minus.clicked.connect(lambda: self.operation_clicked('-'))
        self.button_multiply.clicked.connect(lambda: self.operation_clicked('*'))
        self.button_divide.clicked.connect(lambda: self.operation_clicked('/'))
        # self.button_divide.clicked.connect(lambda: self.operation_power('x^2'))
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_equal.clicked.connect(lambda: self.equals())

        self.digit1 = None
        self.digit2 = None
        self.operation = None
        self.result = None


    def digit_clicked(self, digit):
        current_text = self.display.text()
        if current_text == '0' or current_text == '+' or current_text == '-' or current_text == '/' or current_text == '*':
            self.display.setText(digit)
        else:
            self.display.setText(current_text + digit)

    def operation_clicked(self, operation):
        self.digit1 = float(self.display.text())
        self.display.setText(operation)
        self.operation = operation

    # def operation_power(self, operation):
    #     self.digit1 = float(self.display.text())
    #     self.result = self.digit1 * self.digit1
    #     self.display.setText(str(self.result))
    #     self.digit1 = self.result

    def clear(self):
        self.operand1 = None
        self.digit2 = None
        self.operation = None
        self.result = None
        self.display.setText('0')

    def equals(self):
        self.digit2 = float(self.display.text())
        if self.operation == '+':
            self.result = self.digit1 + self.digit2
        elif self.operation == '-':
            self.result = self.digit2 - self.digit2
        elif self.operation == '*':
            self.result = self.digit1 * self.digit2
        elif self.operation == '/':
            self.result = self.digit1 / self.digit2
        self.display.setText(str(self.result))
        self.digit1 = self.result



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
