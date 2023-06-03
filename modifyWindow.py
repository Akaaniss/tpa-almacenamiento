import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
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