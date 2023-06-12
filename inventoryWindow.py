import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
import csv

#clase para el inventario 
class InventoryWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Inventario")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)#evento para el boton de regreso al menu principal

        self.data_label = QLabel()

        self.view_label = QLabel("Seleccione una opción:")
        self.view_combo = QComboBox()
        self.view_combo.addItem("Materiales")
        self.view_combo.addItem("Insumos")
        self.view_combo.addItem("Herramientas")
        self.view_combo.addItem("Muebles")
        self.view_combo.addItem("Vehiculos")
        self.view_combo.currentIndexChanged.connect(self.show_table)#evento para los cambios de tablas por tipo

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

    #funcion para regresar al menu princiapl
    def go_back(self):
        self.main_window.show()
        self.hide()

    #funcion para registrar los cambios de "tipó" en las tablas
    # y ejecutar sus 'tablas' con sus productos especificos
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

    #funcion que organiza los productos  especificos de los 
    # productos de tipo 'materiales' con sus respectivos 'atributos' y/o 'etiquetas'
    def show_tabla_materiales(self):
        titulos = ["Nombre","ID","Habitacion","Vida Util","Stock"]
        data = []
        with open("materiales.csv", newline="", encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)

    #funcion que organiza los productos  especificos de los 
    # productos de tipo 'insumos' con sus respectivos 'atributos' y/o 'etiquetas'
    def show_tabla_insumos(self):
        titulos = ["Nombre","ID","Vida Util","Stock"]
        data = []
        with open("insumos.csv", newline="", encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, vida_util, stock])

        self.show_table_data(titulos, data)

    #funcion que organiza los productos  especificos de los 
    # productos de tipo 'herramientas' con sus respectivos 'atributos' y/o 'etiquetas'
    def show_tabla_herramientas(self):
        titulos = ["Nombre","ID","Habitacion","Vida Util","Stock"]
        data = []
        with open("herramientas.csv", newline="", encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                id = row["ID"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, id, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)

    #funcion que organiza los productos  especificos de los 
    # productos de tipo 'muebles' con sus respectivos 'atributos' y/o 'etiquetas'
    def show_tabla_muebles(self):
        titulos = ["Nombre","Habitacion","Vida Util","Stock"]
        data = []
        with open("muebles.csv", newline="", encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row["Nombre"]
                habitacion = row["Habitacion"]
                vida_util = row["Vida Util"]
                stock = row["Stock"]
                data.append([nombre, habitacion, vida_util, stock])

        self.show_table_data(titulos, data)

    #funcion que organiza los productos  especificos de los 
    # productos de tipo 'Vehiculo' con sus respectivos 'atributos' y/o 'etiquetas'
    def show_tabla_vehiculos(self):
        titulos = ["Nombre","ID","Vida Util","Stock","Encargado","Reparaciones","Cargas de combustible","Revisiones tecnicas","Pagos de permisos de circulacion"]
        data = []
        with open("vehiculos.csv", newline="", encoding='utf-8-sig') as csvfile:
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

    #funcion que permite mostrar una tabla ordenada previa la
    # organizacion de sus 'etiquetas' y/o 'atributos' de los productos
    def show_table_data(self, titulos, data):
        self.table.clearContents()  
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(titulos))

        self.table.setHorizontalHeaderLabels(titulos)
        self.table.resizeColumnsToContents()

        for row, rowData in enumerate(data):
            for column, item in enumerate(rowData):
                self.table.setItem(row, column, QTableWidgetItem(str(item)))
