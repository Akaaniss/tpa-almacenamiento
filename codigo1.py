import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6 import QtCore, QtGui


class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Sistema de almacenamiento")
        self.setGeometry(200, 200, 800, 600)

        self.label = QLabel("¿Qué desea hacer?")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.visualize_button = QPushButton("Visualizar productos")
        self.visualize_button.clicked.connect(self.open_inventory)

        self.modify_button = QPushButton("Añadir o eliminar productos")
        self.modify_button.clicked.connect(self.open_modify_window)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.visualize_button)
        layout.addWidget(self.modify_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_inventory(self):
        inventory_window = InventoryWindow()
        inventory_window.show()
        self.hide()

    def open_modify_window(self):
        modify_window = ModifyWindow()
        modify_window.show()
        self.hide()


class InventoryWindow(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Inventario")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def go_back(self):
        main_window = MainWindow()
        main_window.show()
        self.hide()


class ModifyWindow(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Añadir o eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def go_back(self):
        main_window = MainWindow()
        main_window.show()
        self.hide()


if __name__ == '_main_':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())