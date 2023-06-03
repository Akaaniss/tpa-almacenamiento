from PyQt6.QtWidgets import QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton, QLineEdit
import csv
import os

class ModifyWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Añadir o eliminar productos")
        self.setGeometry(200, 200, 600, 400)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.go_back)

        self.data_label = QLabel()

        self.file_label = QLabel("Archivo:")
        self.file_combo = QComboBox()
        self.file_combo.addItem("Insumos")
        self.file_combo.addItem("Materiales")
        self.file_combo.addItem("Herramientas")
        self.file_combo.addItem("Muebles")
        self.file_combo.addItem("Vehiculos")
        self.file_combo.currentIndexChanged.connect(self.file_combo_currentIndexChanged)


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

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.add_product)

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

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setLayout(layout)

    def set_data(self, data):
        self.data_label.setText(data)

    def go_back(self):
        self.main_window.show()
        self.hide()    

    def add_product(self):
        selected_file = self.file_combo.currentText()
        name = self.name_input.text()

        if not name:
            self.data_label.setText("El campo de nombre es obligatorio.")
            return

        csv_file = ""
        required_fields = []
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


        field_values = {}
        for field in required_fields:
            field_input = self.get_input_for_field(field)
            if not field_input:
                self.data_label.setText(f"El campo '{field}' es obligatorio.")
                return
            field_values[field] = field_input

        new_row = [field_values[field] for field in required_fields]

        with open(csv_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        new_row = [field_values[field] for field in required_fields]

        rows.append(new_row)

        csv_path = os.path.abspath(csv_file)

        with open(csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        self.data_label.setText("Producto agregado")

        self.data_label.setText("Producto agregado")

        self.name_input.setText('')
        self.expiry_input.setText('')
        self.id_input.setText('')
        self.vida_util_input.setText('')
        self.stock_input.setText('')

    def get_input_for_field(self, field):
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

    def file_combo_currentIndexChanged(self, index):
        selected_file = self.file_combo.currentText()

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
