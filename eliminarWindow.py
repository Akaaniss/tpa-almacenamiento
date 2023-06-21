from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
import csv # Se importa el modulo csv para posteriormente trabajar con este tipo de archivos

# En esta clase se crea la ventana para eliminar productos del inventario
class EliminarWindow(QWidget):

    # Constructor: se define el tamaño de la ventana y los componentes que va tener
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        # Se crea una ComboBox con los diferentes productos, para posteriormente conectarlos a los archivos csv
        self.delete_label = QLabel("Seleccione el producto a eliminar:")
        self.delete_combo = QComboBox()
        self.delete_combo.addItem("Insumos")
        self.delete_combo.addItem("Materiales")
        self.delete_combo.addItem("Herramientas")
        self.delete_combo.addItem("Muebles")
        self.delete_combo.addItem("Vehiculos")
        self.delete_combo.currentTextChanged.connect(self.mostrar_productos)

        # Se crea una tabla de dos filas, una con el nombre del producto y otra para eliminar
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nombre", "Eliminar"])

        # Se agregan todos los componentes al Layout Vertical
        layout = QVBoxLayout()
        layout.addWidget(self.delete_label)
        layout.addWidget(self.delete_combo)
        layout.addWidget(self.table)
        layout.addWidget(self.back_button)

        # Se crea un widget para establecerlo como widget principal y se establece el 
        # layout creado anteriormente como componente del widget principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    # Se crea una función para ocultar la ventana actual y mostrar la ventana principal
    def go_back(self):
        self.main_window.show()
        self.hide()

    # Se crea la función que se llama al seleccionar una opción de la ComboBox
    def mostrar_productos(self):

        # Conecta la opcion selecciona en la ComboBox con el archivo csv correspondiente
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

        # Elimina las filas de la tabla
        self.table.setRowCount(0)  

        # Abre el archivo csv según la opción seleccionada en la ComboBox y recorre sus filas con csv.reader(file)
        with open(csv_filename, newline="") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row:  
                    # Se coloca una nueva fila en la tabla
                    self.table.insertRow(self.table.rowCount())

                    # Se agrega el nombre del producto en la primera columna 
                    name_item = QTableWidgetItem(row[0])
                    self.table.setItem(self.table.rowCount() - 1, 0, name_item)

                    # Se coloca el boton de eliminar en la segunda columna, se conecta a la funcion delete_product
                    delete_button = QPushButton("Eliminar")
                    delete_button.clicked.connect(self.delete_product)
                    self.table.setCellWidget(self.table.rowCount() - 1, 1, delete_button)

    def delete_product(self):
        # Se ve qué botón emitió la señal conectada a la función
        button = self.sender()
        if button:
            # Se obtiene la fila y el nombre del producto seleccionado
            row = self.table.indexAt(button.pos()).row()
            product_name = self.table.item(row, 0).text()

            #Ventana de confirmacion antes de eliminar el producto
            confirmacion = QMessageBox.question(self, "Confirmación", f"¿Está seguro de eliminar el producto {product_name}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Verificar la respuesta del usuario
            if confirmacion == QMessageBox.StandardButton.Si:
                # Se obtiene la opción seleccionada en la ComboBox
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

                # Se leen todas las filas del csv
                with open(csv_filename, "r") as file:
                    rows = list(csv.reader(file))

                # Se escriben las filas en el archivo csv excepto la fila del producto eliminado
                with open(csv_filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    for r in rows:
                        if len(r) > 0 and r[0] != product_name:
                            writer.writerow(r)

                # Se actualiza la tabla luego de eliminar el producto
                self.mostrar_productos()
