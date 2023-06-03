import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow
from inventoryWindow import InventoryWindow
from modifyWindow import ModifyWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
