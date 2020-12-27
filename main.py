import yaml
from AW import AW
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import AW_GUI


class ExampleApp(QtWidgets.QMainWindow, AW_GUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        #Initalisierung der Data class
        self.data = self.getDatafromYaml()
        # GUI Funktionen Initalisieren
        self.setupUi(self)
        self.comboBox_bereich.addItems(["", "msr", "pls", "et"])
        self.comboBox_bereich.currentIndexChanged.connect(self.auswahl_cbbereich)
        self.comboBox_position.currentIndexChanged.connect(self.auswahl_cb3)
        self.comboBox_bezeichner1.setVisible(False)
        self.label_bezeichner1.setVisible(False)
        self.comboBox_bezeichner2.setVisible(False)
        self.label_bezeichner2.setVisible(False)
        self.comboBox_position.setVisible(False)
        self.label_position.setVisible(False)

    def getDatafromYaml(self):
        with open('Verrechnung.yaml', 'r') as f:
            data = yaml.load(f)
            test = AW(
                data["Verrechnung"]["MSR"], data["Verrechnung"]["ET"], data["Verrechnung"]["PLS"],
                data["Verrechnung"]["Mehrung"]
                )
            return test

    def auswahl_cbbereich(self):
        self.comboBox_position.setVisible(True)
        self.label_position.setVisible(True)
        if self.comboBox_bereich.currentText() == "msr":
            self.comboBox_position.clear()
            self.comboBox_position.addItems(self.data.getMSRkeys())
        elif self.comboBox_bereich.currentText() == "et":
            self.comboBox_position.clear()
            trylist = []
            for i in self.data.getETkeys():
                trylist.append(str(i) + ": " + self.data.getETinfo(i))
            self.comboBox_position.addItems(trylist)
        elif self.comboBox_bereich.currentText() == "pls":
            self.comboBox_position.clear()
            self.comboBox_position.addItems(self.data.getPLSkeys())
        else:
            self.comboBox_position.clear()
            self.comboBox_position.setVisible(False)
            self.label_position.setVisible(False)

    def auswahl_cb3(self):
        pass
        #print(self.data.getMSRfunktion(self.comboBox_3.currentText()))


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
