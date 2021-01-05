import yaml
from AW import AW
from createCsv import createExcel
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import AW_GUI


class AWApp(QtWidgets.QMainWindow, AW_GUI.Ui_AWTool):
    # Standart Variablen im GUI
    __version = "Beta 1.0a"
    _bereich = ["---", "msr", "pls", "et"]
    _leistung_msr = ["basic", "detail", "montage", "material"]
    _leistung_et = ["detail", "montage", "material"]
    _msr_header = [
        "Bereich", "Bezeichnung 1", "Bezeichnung 2", "Position", "Leistung", "Menge", "Faktor", "Wert", "Kommentar"
        ]
    _et_header = ["Bereich", "Bezeichnung 1", "information", "Leistung", "Menge", "Faktor", "Wert", "Kommentar"]
    _pls_header = ["Bereich", "Bezeichnung", "Position", "Menge", "Faktor", "Wert", "Kommentar"]
    leer = [""]

    # Initalisierung Programm (GUI)
    def __init__(self, parent=None):
        super(AWApp, self).__init__(parent)
        #Initalisierung der Data class
        # größe der Tabelle erfassen
        self.text = []
        self.rowCountTable = 0
        self.usedHeader = []
        self.faktor = 0.0
        self.summe = 0.0
        with open('Verrechnung.yaml', 'r') as f:
            data = yaml.load(f)
            self.data = AW(
                data["Verrechnung"]["MSR"], data["Verrechnung"]["ET"], data["Verrechnung"]["PLS"],
                data["Verrechnung"]["Mehrung"], data["LF"]
                )
        # Berechnungen für Listen.
        self.PLSkeys = self.data.getPLSkeys()
        self.MSRkeys = self.data.getMSRkeys()
        self.ETkeys = []
        for key in self.data.getETkeys():
            self.ETkeys.append(str(key) + ":" + self.data.getETinfo(key))
        self.menge = []
        for i in range(1, 100):
            self.menge.append(str(i))
        # GUI Funktionen Initalisieren
        self.setupUi(self)
        # Version anzeige
        self.label_version.setText(self.__version)
        # Anzeigen Initalisieren
        self.combobox_menge(False, "Menge", *self.menge)
        self.combobox_leistung(False, "Leistung")
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

    def get_line_auftraggeber(self):
        return self.label_Auftraggeber.text(), self.lineEdit_Auftraggeber.text()

    def get_line_auftrag_intern(self):
        return self.label_intern.text(), self.lineEdit_intern.text()

    def get_line_auftrag_extern(self):
        return self.label_Extern.text(), self.lineEdit_Extern.text()

    def get_line_bearbeiter(self):
        return self.label_bearbeiter.text(), self.lineEdit_bearbeiter.text()


# Events der Button und Comboboxen etc.
# Auswahl des Abrechnungsbereiches

    def auswahl_cbbereich(self):
        if self.comboBox_bereich.currentText() == "msr":
            self.combobox_position(True, "Position", *self.MSRkeys)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung_msr)
            self.defineTableWidget(0, self._msr_header)
            self.defineTableWidget(1, self._msr_header)
            self.usedHeader = self._msr_header
        elif self.comboBox_bereich.currentText() == "et":
            self.combobox_position(True, "Position", *self.ETkeys)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung", *self._leistung_et)
            self.defineTableWidget(0, self._et_header)
            self.defineTableWidget(1, self._et_header)
            self.usedHeader = self._et_header
        elif self.comboBox_bereich.currentText() == "pls":
            self.combobox_position(True, "Position", *self.PLSkeys)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung")
            self.defineTableWidget(0, self._pls_header)
            self.defineTableWidget(1, self._pls_header)
            self.usedHeader = self._pls_header
        else:
            self.combobox_position(False, "", *self.leer)
            self.combobox_bezeichner1(False, "", *self.leer)
            self.combobox_bezeichner2(False, "", *self.leer)
            self.combobox_menge(False, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung")
            self.textbox_bemerkung(False, "", "")
            self.defineTableWidget()
            self.usedHeader = []

    # Auswahl der Positionen im bereich
    def auswahl_cbposition(self):
        text_cb = self.comboBox_position.currentText()
        first, second = self.data.getMSRposition(self.comboBox_position.currentText())
        if text_cb in self.MSRkeys:
            self.combobox_menge(True, "Menge", *self.menge)
            self.combobox_leistung(True, "Leistung", *self._leistung_msr)
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
            self.combobox_leistung(True, "Leistung", *self._leistung_et)
            item = int(self.comboBox_position.currentIndex())
            self.textbox_bemerkung(True, "Bemerkung: ", self.data.getETbemerkung(item))
        elif text_cb in self.PLSkeys:
            pls_txt = self.data.getPLSposition(self.comboBox_position.currentText())
            self.combobox_bezeichner1(True, "Auswahl: ", *pls_txt)
            self.combobox_menge(True, "Menge", *self.menge)
            self.combobox_leistung(False, "Leistung")
        else:
            if self.comboBox_position.currentText() == self.leer:
                item = 0
            else:
                item = int(self.comboBox_position.currentIndex())
            self.combobox_bezeichner1(False, "", *self.leer)
            self.comboBox_bezeichner1.setCurrentIndex(item)
            self.textbox_bemerkung(False, "", "")

    # Checkbox bezeichner 1 funktionen
    def auswahl_cbbezeichner1(self):
        text_cb = self.comboBox_position.currentText()
        text_cb1 = self.comboBox_bezeichner1.currentText()
        if text_cb in self.PLSkeys and text_cb1 in self.data.getPLSposition(text_cb):
            self.textbox_bemerkung(True, "Bemerkung: ", self.data.getPLSinfo(text_cb, text_cb1))

    # Nach größe der Liste wird das Table Widget angepasst
    def defineTableWidget(self, begin=0, list=[]):
        self.tableWidget.setRowCount(begin)
        self.tableWidget.setColumnCount(len(list))
        self.tableWidget.setHorizontalHeaderLabels(list)

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

    # Cellen beschreiben
    def set_table_cells(self, data):
        colmn = self.tableWidget.rowCount()
        for count, cell in enumerate(data):
            self.tableWidget.setItem(colmn - 1, count, QTableWidgetItem(cell))
        self.tableWidget.setRowCount(colmn + 1)

    # Daten aus Tablewidget holen
    def get_table_data(self):
        f_colmn = []
        f_row = []
        for row in range(self.rowCountTable):
            for column in range(self.tableWidget.columnCount()):
                inhalt = self.tableWidget.item(row, column)
                f_colmn.append(str(inhalt.text()))
            f_row.append(f_colmn)
            f_colmn = []
        return f_row

    # daten sammel für msr
    def get_data_msr(self):
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        bez1 = self.comboBox_bezeichner1.currentText()
        bez2 = self.comboBox_bezeichner2.currentText()
        leist = self.comboBox_Leistung.currentText()
        men = self.comboBox_menge.currentText()
        fak = self.data.getMSRfaktor(pos, bez1, bez2, leist)
        wert = self.data.getMSRlf(leist)
        komi = self.lineEdit_kommentar.displayText()
        if fak == None or wert == None:
            fak = 0
            wert = 0
            ber = "ERROR!"
            komi = "Leistung nicht vorhanden!"
        return [ber, bez1, bez2, pos, leist, men, str(fak), "%.2f " % (fak * (wert * int(men))), komi]

    # daten sammel für et
    def get_data_et(self):
        ber = self.comboBox_bereich.currentText()
        temp = self.comboBox_position.currentText()
        temp = temp.split(":")
        pos = temp[0]
        bez1 = temp[1]
        leist = self.comboBox_Leistung.currentText()
        men = self.comboBox_menge.currentText()
        fak = self.data.getETfaktor(pos, leist)
        wert = self.data.getETlf(leist)
        komi = self.lineEdit_kommentar.displayText()
        if fak == None or wert == None:
            fak = 0
            wert = 0
            ber = "ERROR!"
            komi = "Leistung nicht vorhanden!"
        return [ber, pos, bez1, leist, men, str(fak), "%.2f " % (fak * (wert * int(men))), komi]

    # daten sammel für pls
    def get_data_pls(self):
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        bez1 = self.comboBox_bezeichner1.currentText()
        men = self.comboBox_menge.currentText()
        fak = self.data.getPLSfaktor(pos, bez1)
        wert = self.data.getPLSlf()
        komi = self.lineEdit_kommentar.displayText()
        if fak == None or wert == None:
            fak = 0
            wert = 0
            ber = "ERROR!"
            komi = "Leistung nicht vorhanden!"
        return [ber, bez1, pos, men, str(fak), "%.2f " % (fak * (wert * int(men))), komi]

    # funktion von hinzufügen button
    def push_hinzufügen(self):
        if self.comboBox_bereich.currentText() == "---":
            pass
        elif self.comboBox_bereich.currentText() == "msr":
            self.rowCountTable = self.rowCountTable + 1
            self.label_ew(False, 0.0, 0.0)
            self.set_table_cells(self.get_data_msr())
            self.faktor, self.summe = self.calc_sum(7)
            self.label_ew(True, self.faktor, self.summe)
        elif self.comboBox_bereich.currentText() == "et":
            self.rowCountTable = self.rowCountTable + 1
            self.label_ew(False, 0.0, 0.0)
            self.set_table_cells(self.get_data_et())
            self.faktor, self.summe = self.calc_sum(6)
            self.label_ew(True, self.faktor, self.summe)
        elif self.comboBox_bereich.currentText() == "pls":
            self.rowCountTable = self.rowCountTable + 1
            self.label_ew(False, 0.0, 0.0)
            self.set_table_cells(self.get_data_pls())
            self.faktor, self.summe = self.calc_sum(5)
            self.label_ew(True, self.faktor, self.summe)
        else:
            pass

    # Löschen der Ausgewählten Zeile!
    def push_löschen(self):
        if self.comboBox_bereich.currentText() == "---":
            pass
        else:
            indexes = self.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())
            if self.comboBox_bereich.currentText() == "msr":
                self.rowCountTable = self.rowCountTable - 1
                self.label_ew(False, 0.0, 0.0)
                self.faktor, self.summe = self.calc_sum(7)
                self.label_ew(True, self.faktor, self.summe)
            elif self.comboBox_bereich.currentText() == "et":
                self.rowCountTable = self.rowCountTable - 1
                self.label_ew(False, 0.0, 0.0)
                self.faktor, self.summe = self.calc_sum(6)
                self.label_ew(True, self.faktor, self.summe)
            elif self.comboBox_bereich.currentText() == "pls":
                self.rowCountTable = self.rowCountTable - 1
                self.label_ew(False, 0.0, 0.0)
                self.faktor, self.summe = self.calc_sum(5)
                self.label_ew(True, self.faktor, self.summe)

    # Protokoll wird erstellt nur wenn ein Inhalt in der Liste vorhanden ist.
    def push_erstellen(self):
        try:
            txt_geber, geber = self.get_line_auftraggeber()
            txt_intern, intern = self.get_line_auftrag_intern()
            txt_extern, extern = self.get_line_auftrag_extern()
            txt_bearb, bearb = self.get_line_bearbeiter()
            data = self.get_table_data()
            self.create = createExcel(extern)
            self.create.file_properties(bearb)
            self.create.writeString(
                1,
                [
                    [txt_geber, geber, "", "", "Kiel Engineering GmbH"],
                    [txt_intern, intern, "", "", "Niederlassung Wesseling"],
                    [txt_extern, extern, "", "", "Kölner Straße 65"], [txt_bearb, bearb, "", "", "50389 Wesseling"]
                    ],
                )
            self.create.writeString(0, [self.usedHeader])
            self.create.get_width([self.usedHeader])
            self.create.writeString(0, data)
            self.create.get_width(data)
            end_off_data = [["Mehrung von: ", self.faktor, "Gesammtbetrag: %.2f €" % (self.summe)]]
            self.create.writeString(len(self.usedHeader) - 3, end_off_data)
            self.create.get_width(end_off_data)
            self.create.set_width()
            self.create.close()
        except AttributeError:
            pass


def main():
    app = QApplication(sys.argv)
    form = AWApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
