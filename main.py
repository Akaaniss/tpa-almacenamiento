import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow,LoginWindow
from inventoryWindow import InventoryWindow
from modifyWindow import ModifyWindow
from eliminarWindow import EliminarWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
