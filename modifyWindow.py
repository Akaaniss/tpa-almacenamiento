from PyQt6.QtWidgets import QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton, QLineEdit
import csv
import os


# Se crea una clase la cual servira para agregar productos a los archivos csv
class ModifyWindow(QWidget):
    # Constructor: se defiene el tamaño de la ventana y sus componentes
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Añadir o eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        # Se crea un botón para volver y se conecta a la función go_back
        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.data_label = QLabel()

        # Se crea una ComboBox con los diferentes productos del inventario
        self.file_label = QLabel("Archivo:")
        self.file_combo = QComboBox()
        self.file_combo.addItem("Insumos")
        self.file_combo.addItem("Materiales")
        self.file_combo.addItem("Herramientas")
        self.file_combo.addItem("Muebles")
        self.file_combo.addItem("Vehiculos")
        self.file_combo.currentIndexChanged.connect(self.file_combo_currentIndexChanged)

        # Se crean labels con los diferentes parametros y además se agregan campos de entrada de texto para cada uno
        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()

        self.expiry_label = QLabel("Fecha de vencimiento:")
        self.expiry_input = QLineEdit()

        self.id_label = QLabel("ID:")
        self.id_input = QLineEdit()

        self.habitacion_label = QLabel("Habitación:")
        self.habitacion_input = QLineEdit()

        self.vida_util_label = QLabel("Vida útil:")
        self.vida_util_input = QLineEdit()

        self.stock_label = QLabel("Stock:")
        self.stock_input = QLineEdit()

        self.encargado_label = QLabel("Encargado:")
        self.encargado_input = QLineEdit()

        self.reparaciones_label = QLabel("Reparaciones:")
        self.reparaciones_input = QLineEdit()

        self.cargas_combustible_label = QLabel("Cargas de combustible:")
        self.cargas_combustible_input = QLineEdit()

        self.revisiones_tecnicas_label = QLabel("Revisiones técnicas:")
        self.revisiones_tecnicas_input = QLineEdit()

        self.pagos_permisos_label = QLabel("Pagos de permisos de circulación:")
        self.pagos_permisos_input = QLineEdit()

        # Se crea un botón de actualizar y se conecta a la función add_product
        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.add_product)

        # Se agregan todos los componentes a un Layout Vertical 
        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_combo)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.habitacion_label)
        layout.addWidget(self.habitacion_input)
        layout.addWidget(self.vida_util_label)
        layout.addWidget(self.vida_util_input)
        layout.addWidget(self.stock_label)
        layout.addWidget(self.stock_input)
        layout.addWidget(self.encargado_label)
        layout.addWidget(self.encargado_input)
        layout.addWidget(self.reparaciones_label)
        layout.addWidget(self.reparaciones_input)
        layout.addWidget(self.cargas_combustible_label)
        layout.addWidget(self.cargas_combustible_input)
        layout.addWidget(self.revisiones_tecnicas_label)
        layout.addWidget(self.revisiones_tecnicas_input)
        layout.addWidget(self.pagos_permisos_label)
        layout.addWidget(self.pagos_permisos_input)
        layout.addWidget(self.update_button)
        layout.addWidget(self.back_button)

        # Se incorpora el Layout en el Widget Central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data)

    # Metodo para ocultar la ventana actual y mostrar las ventana principal
    def go_back(self):
        self.main_window.show()
        self.hide()    

    def add_product(self):
        # Se obtiene la selección de la ComboBox
        selected_file = self.file_combo.currentText()

        # Se almacena en una variable el texto ingresado en nombre
        name = self.name_input.text()

        # Se verifica que el campo de nombre no esté vacio
        if not name:
            self.data_label.setText("El campo de nombre es obligatorio.")
            return
        if not id:
            self.id_label.setText("El campo de nombre es obligatorio.")
            return

        # Se inicializan las variables csv_file y required_fields
        csv_file = ""
        required_fields = []

        # Se utilizan condicionales para determinar los campos necesarios segun el archivo csv
        # Dependiendo de la opcion seleccionada se le asigna un archivo csv y los parametros requeridos
        if selected_file == "Insumos":
            csv_file = "insumos.csv"
            required_fields = ["Nombre", "ID", "Vida Util", "Stock"]
        elif selected_file == "Materiales":
            csv_file = "materiales.csv"
            required_fields = ["Nombre", "ID", "Habitacion", "Vida Util", "Stock"]
        elif selected_file == "Herramientas":
            csv_file = "herramientas.csv"
            required_fields = ["Nombre", "ID", "Habitacion", "Vida Util", "Stock"]
        elif selected_file == "Muebles":
            csv_file = "muebles.csv"
            required_fields = ["Nombre", "Habitacion", "Vida Util", "Stock"]
        elif selected_file == "Vehiculos":
            csv_file = "vehiculos.csv"
            required_fields = [
                "Nombre", "ID", "Vida Util", "Stock", "Encargado",
                "Reparaciones", "Cargas de combustible", "Revisiones tecnicas",
                "Pagos de permisos de circulacion"
            ]
        else:
            self.data_label.setText("Archivo seleccionado no válido.")
            return

        # Se crea un diccionario para almacenar los valores de los campos
        field_values = {}
        # Se utiliza un bucle para cada opcion dentro de required_fields
        for field in required_fields:
            # Se obtiene lo ingresado en el campo
            field_input = self.get_input_for_field(field)
            # Si el campo esta vacio se muestra un mensaje 
            if not field_input:
                self.data_label.setText(f"El campo '{field}' es obligatorio.")
                return
            # Si lo ingresado en el campo es valido, se agrega al diccionario
            field_values[field] = field_input

        # Se crea una lista con los valores en orden
        new_row = [field_values[field] for field in required_fields]

        # Se abre el archivo csv en modo de lectura
        with open(csv_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        new_row = [field_values[field] for field in required_fields]
        
        # Se agrega new_row a rows
        # Esto representa una nueva fila de datos para ser agregada al archivo csv
        rows.append(new_row)

        # Se obtiene la ruta del archivo csv
        csv_path = os.path.abspath(csv_file)

        # Se abre el archivo en modo escritura y se escriben las filas en rows dentro del archivo csv
        with open(csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        # Se muestra mensaje al agregar el producto
        self.data_label.setText("Producto agregado")

        # Se limpian los campos despues de agregar un producto
        self.name_input.setText('')
        self.expiry_input.setText('')
        self.id_input.setText('')
        self.vida_util_input.setText('')
        self.stock_input.setText('')

    # Este metodo se encarga de obtener el valor ingresado en un campo
    def get_input_for_field(self, field):

        # Se mapea el nombre del campo con el metodo text
        input_mapping = {
            "Nombre": self.name_input.text,
            "ID": self.id_input.text,
            "Habitacion": self.habitacion_input.text,
            "Vida Util": self.vida_util_input.text,
            "Stock": self.stock_input.text,
            "Encargado": self.encargado_input.text,
            "Reparaciones": self.reparaciones_input.text,
            "Cargas de combustible": self.cargas_combustible_input.text,
            "Revisiones tecnicas": self.revisiones_tecnicas_input.text,
            "Pagos de permisos de circulacion": self.pagos_permisos_input.text
        }
        return input_mapping[field]()

    # Se crea un metodo que muestra o oculta diferentes campos segun la opcion seleccionada en la ComboBox
    def file_combo_currentIndexChanged(self, index):
        # Se obtiene la opcion seleccionada en la ComboBox 
        selected_file = self.file_combo.currentText()

        # Se utilizan condicionales para mostrar u ocultar campos de entrada
        self.id_label.setVisible(selected_file != "Muebles")
        self.id_input.setVisible(selected_file != "Muebles")

        self.habitacion_label.setVisible(selected_file in ["Materiales", "Herramientas", "Muebles"])
        self.habitacion_input.setVisible(selected_file in ["Materiales", "Herramientas", "Muebles"])

        self.encargado_label.setVisible(selected_file == "Vehiculos")
        self.encargado_input.setVisible(selected_file == "Vehiculos")

        self.reparaciones_label.setVisible(selected_file == "Vehiculos")
        self.reparaciones_input.setVisible(selected_file == "Vehiculos")

        self.cargas_combustible_label.setVisible(selected_file == "Vehiculos")
        self.cargas_combustible_input.setVisible(selected_file == "Vehiculos")

        self.revisiones_tecnicas_label.setVisible(selected_file == "Vehiculos")
        self.revisiones_tecnicas_input.setVisible(selected_file == "Vehiculos")

        self.pagos_permisos_label.setVisible(selected_file == "Vehiculos")
        self.pagos_permisos_input.setVisible(selected_file == "Vehiculos")
