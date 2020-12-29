import yaml
from AW import AW
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys
import AW_GUI


class AWApp(QtWidgets.QMainWindow, AW_GUI.Ui_AWTool):
    # Standart Variablen im GUI
    __version = "Beta 0.1"
    _bereich = ["---", "msr", "pls", "et"]
    _leistung = ["basic", "detail", "montage", "material"]
    _msr_header = [
        "Bereich", "Bezeichnung 1", "Bezeichnung 2", "Position", "Leistung", "Menge", "Faktor", "Wert", "Kommentar"
        ]
    _et_header = [
        "Bereich", "Bezeichnung 1", "information", "Position", "Leistung", "Menge", "Faktor", "Wert", "Kommentar"
        ]
    _pls_header = ["Bereich", "Bezeichnung", "Position", "Menge", "Faktor", "Wert", "Kommentar"]
    leer = [""]

    # Initalisierung Programm (GUI)
    def __init__(self, parent=None):
        super(AWApp, self).__init__(parent)
        #Initalisierung der Data class
        with open('Verrechnung.yaml', 'r') as f:
            data = yaml.load(f)
            self.data = AW(
                data["Verrechnung"]["MSR"], data["Verrechnung"]["ET"], data["Verrechnung"]["PLS"],
                data["Verrechnung"]["Mehrung"]
                )
        # Berechnungen für Listen.
        self.PLSkeys = self.data.getPLSkeys()
        self.MSRkeys = self.data.getMSRkeys()
        self.ETkeys = []
        self.ETinfo = []
        for key in self.data.getETkeys():
            self.ETkeys.append(str(key))
            self.ETinfo.append(self.data.getETinfo(key))
        self.menge = []
        for i in range(1, 100):
            self.menge.append(str(i))
        # GUI Funktionen Initalisieren
        self.setupUi(self)
        # Version anzeige
        self.label_version.setText(self.__version)
        # Anzeigen Initalisieren
        self.combobox_menge(False, "Menge", *self.menge)
        self.combobox_leistung(False, "Leistung", *self._leistung)
        self.combobox_position(False, "", *self.leer)
        self.combobox_bezeichner1(False, "", *self.leer)
        self.combobox_bezeichner2(False, "", *self.leer)
        self.textbox_bemerkung(False, "", "")
        self.label_ew(True, 0.0, 0.0)
        # Funktionen zuweisen.
        self.comboBox_bereich.addItems(self._bereich)
        self.comboBox_bereich.currentIndexChanged.connect(self.auswahl_cbbereich)
        self.comboBox_position.currentIndexChanged.connect(self.auswahl_cbposition)
        self.comboBox_bezeichner1.currentIndexChanged.connect(self.auswahl_cbbezeichner1)
        self.pushButton_hinzufgen.clicked.connect(lambda: self.push_hinzufügen())
        self.pushButton_loeschen.clicked.connect(lambda: self.push_löschen())
        self.pushButton_erstellen.clicked.connect(lambda: self.push_erstellen())
        self.pushButton_beenden.clicked.connect(lambda: self.exec_())

# Definieren aller genutzten einstellungen der Elemente
# einstellungen Combobox position

    def combobox_position(self, vis, txt, *args):
        self.comboBox_position.clear()
        self.comboBox_position.addItems(self.leer + list(args))
        self.comboBox_position.setCurrentIndex(0)
        self.comboBox_position.setVisible(vis)
        self.label_position.setVisible(vis)
        self.label_position.setText(txt)

    # einstellungen Combobox bezeichner1
    def combobox_bezeichner1(self, vis, txt, *args):
        self.comboBox_bezeichner1.clear()
        self.comboBox_bezeichner1.addItems(self.leer + list(args))
        self.comboBox_bezeichner1.setCurrentIndex(0)
        self.comboBox_bezeichner1.setVisible(vis)
        self.label_bezeichner1.setVisible(vis)
        self.label_bezeichner1.setText(txt)

    # einstellungen Combobox bezeichner2
    def combobox_bezeichner2(self, vis, txt, *args):
        self.comboBox_bezeichner2.clear()
        self.comboBox_bezeichner2.addItems(self.leer + list(args))
        self.comboBox_bezeichner2.setCurrentIndex(0)
        self.comboBox_bezeichner2.setVisible(vis)
        self.label_bezeichner2.setVisible(vis)
        self.label_bezeichner2.setText(txt)

    # einstellungen Combobox menge
    def combobox_menge(self, vis, txt, *args):
        self.comboBox_menge.clear()
        self.comboBox_menge.addItems(list(args))
        self.comboBox_menge.setCurrentIndex(0)
        self.comboBox_menge.setVisible(vis)
        self.label_menge.setVisible(vis)
        self.label_menge.setText(txt)

    # einstellungen Combobox leistung
    def combobox_leistung(self, vis, txt, *args):
        self.comboBox_Leistung.clear()
        self.comboBox_Leistung.addItems(list(args))
        self.comboBox_menge.setCurrentIndex(0)
        self.comboBox_Leistung.setVisible(vis)
        self.label_leistung.setVisible(vis)
        self.label_leistung.setText(txt)

    # Textbox beschreiben
    def textbox_bemerkung(self, vis, txt, str):
        self.textBrowser.setText(str)
        self.textBrowser.setVisible(vis)
        self.label.setText(txt)
        self.label.setVisible(vis)

    # Summe Berechnen
    def label_ew(self, vis, faktor, wert):
        self.label_sum.setVisible(vis)
        self.label_sum.setText("%.2f €" % (wert))
        self.label_faktor.setVisible(vis)
        self.label_faktor.setText("mit Verrechnet : %.1f " % (faktor))


# Events der Button und Comboboxen etc.
# Auswahl des Abrechnungsbereiches

    def auswahl_cbbereich(self):
        if self.comboBox_bereich.currentText() == "msr":
            self.combobox_position(True, "Position", *self.MSRkeys)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung)
            self.defineTableWidget(self._msr_header)
        elif self.comboBox_bereich.currentText() == "et":
            self.combobox_position(True, "Position", *self.ETkeys)
            self.combobox_bezeichner1(True, "information: ", *self.ETinfo)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung)
            self.defineTableWidget(self._et_header)
        elif self.comboBox_bereich.currentText() == "pls":
            self.combobox_position(True, "Position", *self.PLSkeys)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung)
            self.defineTableWidget(self._pls_header)
        else:
            self.combobox_position(False, "", *self.leer)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung)
            self.textbox_bemerkung(False, "", "")
            self.defineTableWidget()

    # Auswahl der Positionen im bereich
    def auswahl_cbposition(self):
        text_cb = self.comboBox_position.currentText()
        first, second = self.data.getMSRposition(self.comboBox_position.currentText())
        if text_cb in self.MSRkeys:
            self.combobox_menge(True, "Menge", *self.menge)
            self.combobox_leistung(True, "Leistung", *self._leistung)
            if text_cb == "vor Ort":
                self.combobox_bezeichner1(True, "Auswahl:", *first)
                self.combobox_bezeichner2(False, "", *self.leer)
            elif text_cb == "Leitstand":
                self.combobox_bezeichner1(True, "Erstestelle:", *first)
                self.combobox_bezeichner2(True, "Zweitestelle:", *second)
            elif text_cb == "weitere":
                self.combobox_bezeichner1(True, "Auswahl:", *first)
                self.combobox_bezeichner2(False, "", *self.leer)
            else:
                self.combobox_bezeichner1(False, "", *self.leer)
                self.combobox_bezeichner2(False, "", *self.leer)
        elif text_cb in self.ETkeys:
            self.combobox_menge(True, "Menge", *self.menge)
            self.combobox_leistung(True, "Leistung", *self._leistung)
            try:
                item = int(self.comboBox_position.currentText())
                self.comboBox_bezeichner1.setCurrentIndex(item)
                self.textbox_bemerkung(True, "Bemerkung: ", self.data.getETbemerkung(item))
            except ValueError:
                pass
        elif text_cb in self.PLSkeys:
            pls_txt = self.data.getPLSposition(self.comboBox_position.currentText())
            self.combobox_bezeichner1(True, "Auswahl: ", *pls_txt)
            self.combobox_menge(True, "Menge", *self.menge)
            self.combobox_leistung(True, "Leistung", *self._leistung)
        else:
            self.textbox_bemerkung(False, "", "")

    # Checkbox bezeichner 1 funktionen
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
            self.textbox_bemerkung(True, "Bemerkung: ", self.data.getPLSinfo(text_cb, text_cb1))

    # Nach größe der Liste wird das Table Widget angepasst
    def defineTableWidget(self, list=[]):
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(len(list))
        self.tableWidget.setHorizontalHeaderLabels(list)

    # daten in Tabelle eintragen
    def setTabeleWidget(self):
        if self.comboBox_bereich.currentText() == "---":
            pass
        elif self.comboBox_bereich.currentText() == "msr":
            self.label_ew(False, 0.0, 0.0)
            self.set_table_cells()
            faktor, summe = self.calc_sum(7)
            self.label_ew(True, faktor, summe)
        elif self.comboBox_bereich.currentText() == "et":
            print("et")
        elif self.comboBox_bereich.currentText() == "pls":
            print("pls")

    # errechnen gesammtwert der AW
    def calc_sum(self, row):
        colmn = self.tableWidget.rowCount() - 1
        res = 0.0
        men = 0
        for col in range(0, colmn):
            res = res + float(self.tableWidget.item(col, row).text())
            men = men + int(self.tableWidget.item(col, row - 2).text())
        kleinste = list(self.data.getFaktorkeys())[0]
        for faktor in reversed(self.data.getFaktorkeys()):
            if men >= int(faktor):
                faktor = self.data.getFaktorkeys()[int(faktor)]["faktor"]
                return faktor, res * faktor
            elif men < kleinste:
                faktor = self.data.getFaktorkeys()[kleinste]["faktor"]
                return faktor, res * faktor
            else:
                pass

    # Cellen beschreiben.
    def set_table_cells(self):
        colmn = self.tableWidget.rowCount()
        for count, cell in enumerate(self.get_data_msr()):
            self.tableWidget.setItem(colmn - 1, count, QTableWidgetItem(cell))
        self.tableWidget.setRowCount(colmn + 1)

    # daten sammel für msr
    def get_data_msr(self):
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        bez1 = self.comboBox_bezeichner1.currentText()
        bez2 = self.comboBox_bezeichner2.currentText()
        leist = self.comboBox_Leistung.currentText()
        men = self.comboBox_menge.currentText()
        fak = self.data.getMSRfaktor(pos, bez1, bez2, leist)
        wert = 10.0
        komi = self.lineEdit_kommentar.displayText()
        return [ber, bez1, bez2, pos, leist, men, str(fak), "%.2f " % (fak * (wert * int(men))), komi]

    def push_hinzufügen(self):
        self.setTabeleWidget()
        print("hinz")

    # Löschen der Ausgewählten Zeile!
    def push_löschen(self):
        if self.comboBox_bereich.currentText() == "---":
            pass
        else:
            indexes = self.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())

    def push_erstellen(self):
        print("prot")


def main():
    app = QApplication(sys.argv)
    form = AWApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
