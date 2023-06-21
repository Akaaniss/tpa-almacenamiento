from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
import csv

class EliminarWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.delete_label = QLabel("Seleccione el producto a eliminar:")
        self.delete_combo = QComboBox()
        self.delete_combo.addItem("Insumos")
        self.delete_combo.addItem("Materiales")
        self.delete_combo.addItem("Herramientas")
        self.delete_combo.addItem("Muebles")
        self.delete_combo.addItem("Vehiculos")
        self.delete_combo.currentTextChanged.connect(self.mostrar_productos)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nombre", "Eliminar"])

        layout = QVBoxLayout()
        layout.addWidget(self.delete_label)
        layout.addWidget(self.delete_combo)
        layout.addWidget(self.table)
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def go_back(self):
        self.main_window.show()
        self.hide()

    def mostrar_productos(self):
        selected_option = self.delete_combo.currentText()

        if selected_option == "Insumos":
            csv_filename = "insumos.csv"
        elif selected_option == "Materiales":
            csv_filename = "materiales.csv"
        elif selected_option == "Herramientas":
            csv_filename = "herramientas.csv"
        elif selected_option == "Muebles":
            csv_filename = "muebles.csv"
        elif selected_option == "Vehiculos":
            csv_filename = "vehiculos.csv"
        else:
            csv_filename = ""

        self.table.setRowCount(0)

        with open(csv_filename, newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    self.table.insertRow(self.table.rowCount())
                    name_item = QTableWidgetItem(row[0])
                    self.table.setItem(self.table.rowCount() - 1, 0, name_item)

                    delete_button = QPushButton("Eliminar")
                    delete_button.clicked.connect(self.delete_product)
                    self.table.setCellWidget(self.table.rowCount() - 1, 1, delete_button)

    def delete_product(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            product_name = self.table.item(row, 0).text()

        confirmacion = QMessageBox.question(self, "Confirmación", f"¿Está seguro de eliminar el producto {product_name}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmacion == QMessageBox.StandardButton.Yes:
            print("El producto se eliminó")
            selected_option = self.delete_combo.currentText()
            if selected_option == "Insumos":
                csv_filename = "insumos.csv"
            elif selected_option == "Materiales":
                csv_filename = "materiales.csv"
            elif selected_option == "Herramientas":
                csv_filename = "herramientas.csv"
            elif selected_option == "Muebles":
                csv_filename = "muebles.csv"
            elif selected_option == "Vehiculos":
                csv_filename = "vehiculos.csv"
            else:
                csv_filename = ""

            with open(csv_filename, "r") as file:
                rows = list(csv.reader(file))

            with open(csv_filename, "w", newline="") as file:
                writer = csv.writer(file)
                for r in rows:
                    if len(r) > 0 and r[0] != product_name:
                        writer.writerow(r)

            self.mostrar_productos()
        elif confirmacion == QMessageBox.StandardButton.No:
            print("No se eliminó el producto")
