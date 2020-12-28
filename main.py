import yaml
from AW import AW
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import AW_GUI


class ExampleApp(QtWidgets.QMainWindow, AW_GUI.Ui_AWTool):

    # Initalisierung Programm (GUI)
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        #Initalisierung der Data class
        with open('Verrechnung.yaml', 'r') as f:
            data = yaml.load(f)
            self.data = AW(
                data["Verrechnung"]["MSR"], data["Verrechnung"]["ET"], data["Verrechnung"]["PLS"],
                data["Verrechnung"]["Mehrung"]
                )
        self.leer = ["---"]
        # Berechnungen für Listen.
        self.PLSkeys = self.data.getPLSkeys()
        self.MSRkeys = self.data.getMSRkeys()
        self.ETkeys = []
        self.ETinfo = []
        for key in self.data.getETkeys():
            self.ETkeys.append(str(key))
            self.ETinfo.append(self.data.getETinfo(key))
        self.ETkeys = self.leer + self.ETkeys
        self.ETinfo = self.leer + self.ETinfo
        menge = []
        for i in range(1, 100):
            menge.append(str(i))
        # GUI Funktionen Initalisieren
        self.setupUi(self)
        # Standart Anzeige
        self.comboBox_bereich_2.addItems(menge)
        self.comboBox_bereich.addItems(["---", "msr", "pls", "et"])
        self.comboBox_bereich.currentIndexChanged.connect(self.auswahl_cbbereich)
        self.comboBox_position.currentIndexChanged.connect(self.auswahl_cbposition)
        self.comboBox_bezeichner1.currentIndexChanged.connect(self.auswahl_cbbezeichner1)
        self.pushButton_hinzufgen.clicked.connect(lambda: self.push_hinzufügen())
        self.pushButton_loeschen.clicked.connect(lambda: self.push_löschen())
        self.pushButton_erstellen.clicked.connect(lambda: self.push_erstellen())
        self.pushButton_beenden.clicked.connect(lambda: self.exec_())
        self.comboBox_bezeichner1.setVisible(False)
        self.label_bezeichner1.setVisible(False)
        self.comboBox_bezeichner2.setVisible(False)
        self.label_bezeichner2.setVisible(False)
        self.comboBox_position.setVisible(False)
        self.label_position.setVisible(False)
        self.label.setVisible(False)
        self.textBrowser.setVisible(False)

    # Auswahl des Abrechnungsbereiches
    def auswahl_cbbereich(self):
        self.comboBox_position.setVisible(True)
        self.label_position.setVisible(True)
        if self.comboBox_bereich.currentText() == "msr":
            self.comboBox_position.clear()
            self.comboBox_position.addItems(self.leer + self.MSRkeys)
            self.comboBox_position.setCurrentIndex(0)
            self.comboBox_bezeichner1.setVisible(False)
            self.label_bezeichner1.setVisible(False)
            self.comboBox_bezeichner1.clear()
            self.comboBox_bezeichner2.setVisible(False)
            self.label_bezeichner2.setVisible(False)
            self.comboBox_bezeichner2.clear()
        elif self.comboBox_bereich.currentText() == "et":
            self.comboBox_position.clear()
            self.comboBox_position.addItems(self.ETkeys)
            self.comboBox_position.setCurrentIndex(0)
            self.comboBox_bezeichner1.clear()
            self.comboBox_bezeichner2.setVisible(False)
            self.label_bezeichner2.setVisible(False)
            self.comboBox_bezeichner2.clear()
            self.comboBox_bezeichner1.setVisible(True)
            self.label_bezeichner1.setVisible(True)
            self.label_bezeichner1.setText("information: ")
            self.comboBox_bezeichner1.addItems(self.ETinfo)
        elif self.comboBox_bereich.currentText() == "pls":
            self.comboBox_position.clear()
            self.comboBox_position.addItems(self.leer + self.PLSkeys)
            self.comboBox_position.setCurrentIndex(0)
            self.comboBox_bezeichner1.setVisible(False)
            self.label_bezeichner1.setVisible(False)
            self.comboBox_bezeichner1.clear()
            self.comboBox_bezeichner2.setVisible(False)
            self.label_bezeichner2.setVisible(False)
            self.comboBox_bezeichner2.clear()
        else:
            self.comboBox_position.clear()
            self.comboBox_position.setVisible(False)
            self.label_position.setVisible(False)
            self.comboBox_bezeichner1.setVisible(False)
            self.label_bezeichner1.setVisible(False)
            self.comboBox_bezeichner1.clear()
            self.comboBox_bezeichner2.setVisible(False)
            self.label_bezeichner2.setVisible(False)
            self.comboBox_bezeichner2.clear()
            self.label.setVisible(False)
            self.textBrowser.setVisible(False)

    # Auswahl der Positionen im bereich
    def auswahl_cbposition(self):
        text_cb = self.comboBox_position.currentText()
        if text_cb in self.MSRkeys:
            first, second = self.data.getMSRposition(text_cb)
            if text_cb == "vor Ort":
                self.comboBox_bezeichner1.clear()
                self.comboBox_bezeichner1.setVisible(True)
                self.label_bezeichner1.setVisible(True)
                self.label_bezeichner1.setText("Auswahl: ")
                self.comboBox_bezeichner1.addItems(self.leer + first)
            elif text_cb == "Leitstand":
                self.comboBox_bezeichner1.clear()
                self.comboBox_bezeichner1.setVisible(True)
                self.label_bezeichner1.setVisible(True)
                self.label_bezeichner1.setText("Erstestelle: ")
                self.comboBox_bezeichner1.addItems(self.leer + first)
                self.comboBox_bezeichner2.clear()
                self.comboBox_bezeichner2.setVisible(True)
                self.label_bezeichner2.setVisible(True)
                self.label_bezeichner2.setText("Zweitestelle: ")
                self.comboBox_bezeichner2.addItems(self.leer + second)
            elif text_cb == "weitere":
                self.comboBox_bezeichner1.clear()
                self.comboBox_bezeichner1.setVisible(True)
                self.label_bezeichner1.setVisible(True)
                self.label_bezeichner1.setText("Auswahl: ")
                self.comboBox_bezeichner1.addItems(self.leer + first)
            else:
                self.comboBox_bezeichner1.setVisible(False)
                self.label_bezeichner1.setVisible(False)
                self.comboBox_bezeichner2.setVisible(False)
                self.label_bezeichner2.setVisible(False)
        elif text_cb in self.ETkeys:
            try:
                item = int(self.comboBox_position.currentText())
                self.comboBox_bezeichner1.setCurrentIndex(item)
                self.label.setVisible(True)
                self.textBrowser.setVisible(True)
                self.textBrowser.setText(self.data.getETbemerkung(item))
            except ValueError:
                pass
        elif text_cb in self.PLSkeys:
            pls_txt = self.data.getPLSposition(text_cb)
            self.comboBox_bezeichner1.clear()
            self.comboBox_bezeichner1.setVisible(True)
            self.label_bezeichner1.setVisible(True)
            self.label_bezeichner1.setText("Auswahl: ")
            self.comboBox_bezeichner1.addItems(self.leer + pls_txt)
        else:
            self.label.setVisible(False)
            self.textBrowser.setVisible(False)

    def auswahl_cbbezeichner1(self):
        text_cb = self.comboBox_position.currentText()
        text_cb1 = self.comboBox_bezeichner1.currentText()
        if text_cb in self.ETkeys:
            try:
                item = self.comboBox_bezeichner1.currentIndex()
                self.comboBox_position.setCurrentIndex(item)
            except ValueError:
                pass
        elif text_cb in self.PLSkeys and text_cb1 in self.data.getPLSposition(text_cb):
            self.label.setVisible(True)
            self.textBrowser.setVisible(True)
            self.textBrowser.setText(self.data.getPLSinfo(text_cb, text_cb1))

    def push_hinzufügen(self):
        print("hinz")

    def push_löschen(self):
        print("delete")

    def push_erstellen(self):
        print("prot")


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
