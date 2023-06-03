import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton,QLineEdit,QMessageBox
from PyQt6 import QtCore
from modifyWindow import ModifyWindow
from inventoryWindow import InventoryWindow

class loginWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Inicio de sesión")
        self.setGeometry(200, 200, 400, 300)

        self.login_label = QLabel("Inicio de sesión")
        self.login_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.username_label = QLabel("Usuario:")
        self.password_label = QLabel("Contraseña:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addStretch()

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            self.parent().login_successful()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de inicio de sesión")
            error_dialog.setText("Usuario o contraseña incorrectos.")
            error_dialog.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de almacenamiento")
        self.setGeometry(200, 200, 800, 600)

        self.label = QLabel("¿Qué desea hacer?")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")

        self.visualize_button = QPushButton("Visualizar productos")
        self.visualize_button.clicked.connect(self.open_inventory)
        self.visualize_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")
        self.visualize_button.setEnabled(False)

        self.modify_button = QPushButton("Añadir o eliminar productos")
        self.modify_button.clicked.connect(self.open_modify_window)
        self.modify_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")
        self.modify_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addSpacing(80)
        layout.addWidget(self.label)
        layout.addWidget(self.visualize_button)
        layout.addWidget(self.modify_button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.login_window = loginWindow(self)
        self.login_window.show()

        self.inventory_window = None
        self.modify_window = None

    def login_successful(self):
        self.login_window.hide()
        self.label.setText("¿Qué desea hacer?")
        self.visualize_button.setEnabled(True)
        self.modify_button.setEnabled(True)

    def open_inventory(self):
        if self.inventory_window is None:
            self.inventory_window = InventoryWindow(self)
            self.inventory_window.set_data("Información de visualización de productos")
        self.inventory_window.show()
        self.hide()

    def open_modify_window(self):
        if self.modify_window is None:
            self.modify_window = ModifyWindow(self)
            self.modify_window.set_data("Información para añadir o eliminar productos")
        self.modify_window.show()
        self.hide()

