import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de almacenamiento")
        self.setGeometry(200,200,800,600)

        self.inventory_button = QPushButton("Inventario")
        self.inventory_button.clicked.connect(self.open_inventory)

        layout = QVBoxLayout()
        layout.addWidget(self.inventory_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        self.show()
    def open_inventory(self):
        inventory_window = InventoryWindow()
        inventory_window.show()
        self.hide()


class InventoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventario")
        self.setGeometry(200,200,600,400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def go_back(self):
        main_window = MainWindow()
        main_window.show()
        self.hide()


if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec())
