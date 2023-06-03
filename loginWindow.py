import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt6 import QtCore

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setGeometry(200,200,300,200)

        self.username_label = QLabel("Usuario")
        self.password_label = QLabel("Contraseña")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button= QPushButton("Iniciar sesión")
        self.register_button = QPushButton("Registrarse")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username= self.username_input.text()
        password= self.password_input.text()

        if username =="admin" and password =="admin":
            self.parent().show_main_window()
            self.close()
        else:
            error_dialog=QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de inicio de sesión")
            error_dialog.setText("Usuario o contraseña incorrectos.")
            error_dialog.exec()
        
    def register(self):
        info_dialog=QMessageBox()
        info_dialog.setIcon(QMessageBox.Icon.Information)
        info_dialog.setWindowTitle("Registro")
        info_dialog.setText("Función no implementada")
        info_dialog.exec()

