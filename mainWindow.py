import sys
import csv
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QMainWindow, QApplication, QFormLayout, QDateEdit
from PyQt6.QtCore import Qt, QDate
from modifyWindow import ModifyWindow
from inventoryWindow import InventoryWindow
from eliminarWindow import EliminarWindow

class RegisterWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.setWindowTitle("Registro")
        self.setGeometry(200, 200, 400, 300)

        self.login_window = login_window

        self.register_label = QLabel("Registro")
        self.register_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.username_label = QLabel("Usuario:")
        self.password_label = QLabel("Contraseña:")
        self.birthdate_label = QLabel("Fecha de nacimiento:")
        self.occupation_label = QLabel("Ocupación:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.birthdate_input = QDateEdit()
        self.occupation_input = QLineEdit()

        self.register_button = QPushButton("Registrarse")
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.back)
        self.back_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)
        self.form_layout.addRow(self.birthdate_label, self.birthdate_input)
        self.form_layout.addRow(self.occupation_label, self.occupation_input)
        self.form_layout.addRow(self.register_button, self.back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.register_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(self.form_layout)
        layout.addStretch()

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        birthdate = self.birthdate_input.date().toString(Qt.DateFormat.ISODate)
        occupation = self.occupation_input.text()

        if len(password) > 8:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("La contraseña no puede tener más de 8 caracteres.")
            error_dialog.exec()
            return

        if username and password and birthdate and occupation:
            try:
                with open('registro_de_cuentas.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password, birthdate, occupation])
            except OSError as e:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de registro")
                error_dialog.setText("Error al escribir en el archivo CSV.")
                error_dialog.exec()
                print(f"Error al escribir en el archivo CSV: {e}")
                return

            print("Registro exitoso")
            self.close()
            self.login_window.show()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("Por favor, ingresa todos los campos requeridos.")
            error_dialog.exec()

    def back(self):
        self.close()
        self.login_window.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
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

        self.register_button = QPushButton("Registrarse")
        self.register_button.clicked.connect(self.open_register_window)
        self.register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addStretch()

        self.setLayout(layout)

        self.register_window = None
        self.main_window = None

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        with open('registro_de_cuentas.csv',newline='') as cuentas:
                reader = csv.DictReader(cuentas)
                for row in reader:
                    if username == row['Usuario'] and password == row['Contrasenha']:
                        print("Inicio de sesión exitoso")
                        self.login_successful()
                        break
                else:
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Icon.Critical)
                    error_dialog.setWindowTitle("Error de inicio de sesión")
                    error_dialog.setText("Usuario o contraseña incorrectos.")
                    print("Inicio de sesión fallido")
                    error_dialog.exec()

    def login_successful(self):
        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

    def open_register_window(self):
        self.register_window = RegisterWindow(self)
        self.hide()
        self.register_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de almacenamiento")
        self.setGeometry(200, 200, 800, 600)

        self.label = QLabel("¿Qué desea hacer?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")

        self.visualize_button = QPushButton("Visualizar productos")
        self.visualize_button.clicked.connect(self.open_inventory)
        self.visualize_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.modify_button = QPushButton("Añadir productos")
        self.modify_button.clicked.connect(self.open_modify_window)
        self.modify_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.eliminar_button = QPushButton("Eliminar productos")
        self.eliminar_button.clicked.connect(self.open_eliminar_window)
        self.eliminar_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addSpacing(80)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.visualize_button)
        layout.addWidget(self.modify_button)
        layout.addWidget(self.eliminar_button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.inventory_window = None
        self.modify_window = None
        self.eliminar_window = None

    def login_successful(self):
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

    def open_eliminar_window(self):
        if self.eliminar_window is None:
            self.eliminar_window = EliminarWindow(self)
        self.eliminar_window.show()
        self.hide()
