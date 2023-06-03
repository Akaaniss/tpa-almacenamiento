import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6 import QtCore
from modifyWindow import ModifyWindow
from inventoryWindow import InventoryWindow

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

        self.modify_button = QPushButton("Añadir o eliminar productos")
        self.modify_button.clicked.connect(self.open_modify_window)
        self.modify_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.visualize_button)
        layout.addWidget(self.modify_button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.inventory_window = None
        self.modify_window = None

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