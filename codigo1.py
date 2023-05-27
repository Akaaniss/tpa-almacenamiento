import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton,QComboBox,QTableWidget
from PyQt6 import QtCore, QtGui


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


class InventoryWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Inventario")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.data_label = QLabel("Seleccione una categoria:")
        self.category_combobox = QComboBox()
        self.category_combobox.addItem("Materiales")
        self.category_combobox.addItem("Herramientas")
        self.category_combobox.addItem("Insumos")
        self.category_combobox.addItem("Muebles")
        self.category_combobox.addItem("Vehículos")

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(7)

        column_labels = ["Nombre de producto", "ID", "Cantidad", "Fecha de vencimiento", "Habitación", "Actualizar stock"]
        self.table.setHorizontalHeaderLabels(column_labels)

        self.add_button = QPushButton("Agregar producto")
        self.add_button.clicked.connect(self.add_product)

        self.update_button = QPushButton("Actualizar producto")
        self.update_button.clicked.connect(self.update_product)

        self.delete_button = QPushButton("Eliminar producto")
        self.delete_button.clicked.connect(self.delete_product)
    

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.category_combobox)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data) 

    def go_back(self):
        self.main_window.show()
        self.hide()
    def add_product(self):
        pass

    def update_product(self):
        pass

    def delete_product(self):
        pass


class ModifyWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Añadir o eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.data_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data)

    def go_back(self):
        self.main_window.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())