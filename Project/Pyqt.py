import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout

class LoginWindow(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle('Login Window')
        self.setGeometry(100, 100, 400, 300)

        # Create login and registration buttons
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.show_login_fields)
        register_button = QPushButton('Register')
        register_button.clicked.connect(self.show_register_fields)

        # Add buttons to vertical layout
        layout = QVBoxLayout()
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        # Set layout for window
        self.setLayout(layout)

    def show_login_fields(self):
        # Remove existing widgets from layout
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)

        # Create login label and line edit
        login_label = QLabel('Login:')
        self.login_edit = QLineEdit()

        # Create password label and line edit
        password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # Create login button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.login)

        # Add widgets to vertical layout
        layout = QVBoxLayout()
        layout.addWidget(login_label)
        layout.addWidget(self.login_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(login_button)

        # Set layout for window
        self.setLayout(layout)

    def show_register_fields(self):
        # Remove existing widgets from layout
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)

        # Create login label and line edit
        login_label = QLabel('Come up with a login:')
        self.login_edit = QLineEdit()

        # Create password label and line edit
        password_label = QLabel('Come up with a password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # Create name label and line edit
        name_label = QLabel('Enter a name:')
        self.name_edit = QLineEdit()

        # Create register button
        register_button = QPushButton('Register')
        register_button.clicked.connect(self.register)

        # Add widgets to vertical layout
        layout = QVBoxLayout()
        layout.addWidget(login_label)
        layout.addWidget(self.login_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(register_button)

        # Set layout for window
        self.setLayout(layout)

    def login(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        print(f'Logging in with login: {login} and password: {password}')

    def register(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        name = self.name_edit.text()
        print(f'Registering with login: {login}, password: {password}, and name: {name}')

if name == 'main':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())