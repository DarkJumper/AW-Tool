import sys

from PySide6 import QtWidgets

from model.TableModel import TableModel
from views.RezeptView import RezeptWindow
from views.windows.MainWindow import Ui_AWTool


class MainWindow(QtWidgets.QMainWindow, Ui_AWTool):

    __version = "1.1"

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.tabel_model = TableModel()
        self.setupUi(self)
        self.show()
        self.rezept_window = RezeptWindow()
        self.pushButton_hinzufgen.clicked.connect(self.push_hinzufügen)
        self.pushButton_loeschen.clicked.connect(self.push_löschen)
        self.pushButton_erstellen.clicked.connect(self.push_erstellen)
        self.pushButton_beenden.clicked.connect(self.push_beenden)

    def push_hinzufügen(self, checked):
        self.rezept_window.show()

    def push_löschen(self, checked):
        pass

    def push_erstellen(self, checked):
        pass

    def push_beenden(self, checked):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()