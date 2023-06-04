import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
import csv

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
        titulos = ["Nombre","ID","Habitacion","Vida Util","Stock"]
        data = []
        with open("materiales.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)

    def show_tabla_insumos(self):
        titulos = ["Nombre","ID","Vida Util","Stock"]
        data = []
        with open("insumos.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, vida_util, stock])

        self.show_table_data(titulos, data)

    def show_tabla_herramientas(self):
        titulos = ["Nombre","ID","Habitacion","Vida Util","Stock"]
        data = []
        with open("herramientas.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)

    def show_tabla_muebles(self):
        titulos = ["Nombre","Habitacion","Vida Util","Stock"]
        data = []
        with open("muebles.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)


    def show_tabla_vehiculos(self):
        titulos = ["Nombre","ID","Vida Util","Stock","Encargado","Reparaciones","Cargas de combustible","Revisiones tecnicas","Pagos de permisos de circulacion"]
        data = []
        with open("vehiculos.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                encargado = row["Encargado"]
                reparaciones = row["Reparaciones"]
                cargas = row["Cargas de combustible"]
                revisiones =row["Revisiones tecnicas"]
                pagos = row["Pagos de permisos de circulacion"]
                data.append([nombre, id, vida_util, stock, encargado, reparaciones, cargas, revisiones, pagos])

        self.show_table_data(titulos, data)

    def show_table_data(self, titulos, data):
        self.table.clearContents()  
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(titulos))

        self.table.setHorizontalHeaderLabels(titulos)
        self.table.resizeColumnsToContents()

        for row, rowData in enumerate(data):
            for column, item in enumerate(rowData):
                self.table.setItem(row, column, QTableWidgetItem(str(item)))
