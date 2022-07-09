import sys
from PyQt6.QtWidgets import QApplication

from src.gui.MainWidget import MainWidget


class Application:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = MainWidget()
        self.widget.resize(250, 250)

    def run(self):
        self.widget.show()
        self.app.exec()
