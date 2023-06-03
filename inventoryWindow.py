import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem

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
