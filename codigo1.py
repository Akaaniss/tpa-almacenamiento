import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem,QLineEdit
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

        self.data_label = QLabel()

        self.view_label = QLabel("Seleccione una opción:")
        self.view_combo = QComboBox()
        self.view_combo.addItem("Materiales")
        self.view_combo.addItem("Insumos")
        self.view_combo.addItem("Herramientas")
        self.view_combo.addItem("Muebles")
        self.view_combo.addItem("Vehiculos")
        self.view_combo.currentIndexChanged.connect(self.show_table) 

        self.table = QTableWidget() 
        self.table.setRowCount(6)  
        self.table.setColumnCount(10) 

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.view_label)  
        layout.addWidget(self.view_combo)
        layout.addWidget(self.table)  
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data) 

    def go_back(self):
        self.main_window.show()
        self.hide()

    def show_table(self):
        selected_option = self.view_combo.currentText()
        if selected_option == "Materiales":
            self.show_tabla_materiales()
        elif selected_option == "Insumos":
            self.show_tabla_insumos()
        elif selected_option == "Herramientas":
            self.show_tabla_herramientas()
        elif selected_option == "Muebles":
            self.show_tabla_muebles()
        elif selected_option == "Vehiculos":
            self.show_tabla_vehiculos()

    def show_tabla_materiales(self):
        titulos = ["Nombre", "ID", "Cantidad", "Vida Util", "Habitacion", "Stock"]
        data = [
            ["Material 1", "00", "100", "1 año", "1", "100"],
            ["Material 2", "01", "200", "2 años", "2", "200"],
            ["Material 3", "02", "300", "3 años", "3", "300"],
        ]
        self.show_table_data(titulos, data)

    def show_tabla_insumos(self):
        titulos = ["Nombre", "ID", "Cantidad", "Vida Util", "Habitacion", "Stock"]
        data = [
            ["Insumo 1", "00", "100", "1 año", "1", "100"],
            ["Insumo 2", "01", "200", "2 años", "2", "200"],
            ["Insumo 3", "02", "300", "3 años", "3", "300"],
        ]
        self.show_table_data(titulos, data)

    def show_tabla_herramientas(self):
        titulos = ["Nombre", "ID", "Cantidad", "Vida Util", "Habitacion", "Stock"]
        data = [
            ["Herramienta 1", "00", "100", "1 año", "1", "100"],
            ["Herramienta 2", "01", "200", "2 años", "2", "200"],
            ["Herramienta 3", "02", "300", "3 años", "3", "300"],
        ]
        self.show_table_data(titulos, data)

    def show_tabla_muebles(self):
        titulos = ["Nombre", "ID", "Cantidad", "Vida Util", "Habitacion", "Stock"]
        data = [
            ["Mueble 1", "00", "100", "1 año", "1", "100"],
            ["Mueble 2", "01", "200", "2 años", "2", "200"],
            ["Mueble 3", "02", "300", "3 años", "3", "300"],
        ]
        self.show_table_data(titulos, data)

    def show_tabla_vehiculos(self):
        titulos = ["Nombre", "ID", "Cantidad", "Vida Util", "Habitacion", "Stock"]
        data = [
            ["Vehiculo 1", "00", "100", "1 año", "1", "100"],
            ["Vehiculo 2", "01", "200", "2 años", "2", "200"],
            ["Vehiculo 3", "02", "300", "3 años", "3", "300"],
        ]
        self.show_table_data(titulos, data)

    def show_table_data(self, titulos, data):
        self.table.clearContents()  
        self.table.setRowCount(len(data))  

        self.table.setHorizontalHeaderLabels(titulos)

        for row, rowData in enumerate(data):
            for column, item in enumerate(rowData):
                self.table.setItem(row, column, QTableWidgetItem(item))

class ModifyWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Añadir o eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.data_label = QLabel()

        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()

        self.quantity_label = QLabel("Cantidad:")
        self.quantity_input = QLineEdit()

        self.expiry_label = QLabel("Fecha de vencimiento:")
        self.expiry_input = QLineEdit()

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.update_product)

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.expiry_label)
        layout.addWidget(self.expiry_input)
        layout.addWidget(self.update_button)
        layout.addWidget(self.back_button)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data)

    def go_back(self):
        self.main_window.show()
        self.hide()    

    def update_product(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()
        expiry = self.expiry_input.text()
        print('hola')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
