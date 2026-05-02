from PySide6 import QtWidgets, QtUiTools
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon
import sys

class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.loader = QtUiTools.QUiLoader()
        ui_file = QFile("frontend/ui/main_window.ui")

        self.ui = self.loader.load(ui_file)
        self.ui.setWindowTitle("Factory Management System")
        self.ui.setWindowIcon(QIcon("frontend/assets/building-non_black.png"))


    def setup(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()
    sys.exit(app.exec())
