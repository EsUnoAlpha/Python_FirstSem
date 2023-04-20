import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
import Client_socket

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')


        self.display = QLineEdit(f'{Client_socket.messages}')
        self.sec_display = QLineEdit('Тут вводить')
        self.display.setReadOnly(True)



        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 30, 30)
        grid.addWidget((self.sec_display))

        self.setLayout(grid)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
