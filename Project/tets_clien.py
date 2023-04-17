import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Window')
        self.setGeometry(100, 100, 400, 300)

        # Create login label and line edit
        login_label = QLabel('Login:')
        self.login_edit = QLineEdit()

        # Create password label and line edit
        password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # Create name label and line edit
        name_label = QLabel('Name:')
        self.name_edit = QLineEdit()

        # Create login and registration buttons
        login_button = QPushButton('Login')
        register_button = QPushButton('Registration')

        # Add widgets to vertical layout
        layout = QVBoxLayout()
        layout.addWidget(login_label)
        layout.addWidget(self.login_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        # Set layout for window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())