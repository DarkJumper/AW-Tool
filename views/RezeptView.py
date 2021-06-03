from PySide6 import QtWidgets

from .windows.RezeptWidget import Ui_Rezept


class RezeptWindow(QtWidgets.QWidget, Ui_Rezept):

    def __init__(self):
        super(RezeptWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_beenden.clicked.connect(self.push_beenden)

    def push_beenden(self, checked):
        self.close()
