import yaml
import sys
import AW_GUI

from AW import ET, MSR, PLS
from createCsv import createExcel
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox, QTableWidget
from datetime import date


class AWApp(QtWidgets.QMainWindow, AW_GUI.Ui_AWTool):
    # Standart Variablen im GUI
    __version = "1.1"
    _dashes = ["---"]
    blank = [""]

    # Initalisierung Programm (GUI)
    def __init__(self, parent=None):
        super(AWApp, self).__init__(parent)
        self.text = []
        self.lookup = dict()
        self.rowCountTable = 1
        self.faktor = 0.0
        self.summe = 0.0
        self.prozent = 100.0
        self.clicked = True
        file = 'Verrechnung.yaml'
        try:
            with open(file, 'r') as f:
                data = yaml.load(f)
                self.et = ET(data)
                self.msr = MSR(data)
                self.pls = PLS(data)
        except FileNotFoundError:
            self.show_popup_warning("Verrechnung.yaml konnte nicht gefunden werden!!")
            self.exec_()
        self.current_func = self.msr
        self.amount = [str(x) for x in range(1, 50)]
        self.setupUi(self)
        self.label_version.setText(self.__version)
        self.init_objects()
        self.init_comboBoxes()
        self.init_buttons()

    def init_objects(self):
        self.combobox_menge(True, "Menge", *self.amount)
        self.combobox_leistung(True, "Leistung")
        self.combobox_position(False, "")
        self.combobox_bezeichner1(False, "", *self.blank)
        self.combobox_bezeichner2(False, "", *self.blank)
        self.textbox_bemerkung(False, "", "")
        self.label_ew(True, 0.0, 0.0)

    def init_buttons(self):
        self.pushButton_hinzufgen.clicked.connect(lambda: self.push_hinzufügen())
        self.pushButton_loeschen.clicked.connect(lambda: self.push_löschen())
        self.pushButton_erstellen.clicked.connect(lambda: self.push_erstellen())
        self.pushButton_beenden.clicked.connect(lambda: self.exec_())

    def init_comboBoxes(self):
        self.comboBox_bereich.addItems(self._dashes + self.msr.services)
        self.comboBox_bereich.currentIndexChanged.connect(self.auswahl_cbbereich)
        self.comboBox_position.currentIndexChanged.connect(self.auswahl_cbposition)
        self.comboBox_bezeichner1.currentIndexChanged.connect(self.auswahl_cbbezeichner1)
        #self.comboBox_bezeichner2.currentIndexChanged.connect(self.auswahl_cbbezeichner2)

# Definieren aller genutzten einstellungen der Elemente
# einstellungen Combobox position

    def combobox_position(self, vis, txt, *args):
        self.comboBox_position.clear()
        self.comboBox_position.addItems(self._dashes + list(args))
        self.comboBox_position.setCurrentIndex(0)
        self.comboBox_position.setVisible(vis)
        self.label_position.setVisible(vis)
        self.label_position.setText(txt)

    # einstellungen Combobox bezeichner1
    def combobox_bezeichner1(self, vis, txt, *args):
        self.comboBox_bezeichner1.clear()
        self.comboBox_bezeichner1.addItems(self._dashes + list(args))
        self.comboBox_bezeichner1.setCurrentIndex(0)
        self.comboBox_bezeichner1.setVisible(vis)
        self.label_bezeichner1.setVisible(vis)
        self.label_bezeichner1.setText(txt)

    # einstellungen Combobox bezeichner2
    def combobox_bezeichner2(self, vis, txt, *args):
        self.comboBox_bezeichner2.clear()
        self.comboBox_bezeichner2.addItems(self._dashes + list(args))
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
        self.comboBox_Leistung.addItems(self._dashes + list(args))
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

    def show_popup_info(self, string):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(string)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def show_popup_warning(self, string):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(string)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


# Events der Button und Comboboxen etc.
# Auswahl des Abrechnungsbereiches

    def auswahl_cbbereich(self):
        cb_text = self.comboBox_bereich.currentText()
        if cb_text == self._dashes[0]:
            self.combobox_position(False, "")
            self.combobox_bezeichner1(False, "")
            self.combobox_bezeichner2(False, "")
            self.combobox_menge(False, "Menge")
            self.combobox_leistung(False, "Leistung")
            self.textbox_bemerkung(False, "", "")
            self.defineTableWidget()
            self.usedHeader = []
            self.lookup = dict()
        else:
            if cb_text == "MSR":
                self.current_func = self.msr
                self.lookup = dict()
            if cb_text == "ET":
                self.current_func = self.et
                self.lookup = dict()
            if cb_text == "PLS":
                self.current_func = self.pls
                self.lookup = dict()
            self.combobox_position(True, "Position", *self.current_func.position)
            self.combobox_menge(True, "Menge", *self.amount)
            self.combobox_bezeichner1(False, "")
            self.combobox_bezeichner2(False, "")
            self.combobox_leistung(True, "Leistung")
            self.defineTableWidget(0, self.current_func.table_header)
            self.defineTableWidget(1, self.current_func.table_header)

    # Auswahl der Positionen im bereich
    def auswahl_cbposition(self):
        cb_text_position = self.comboBox_position.currentText()
        if cb_text_position == self._dashes[0] or cb_text_position == "":
            pass
        else:
            self.combobox_bezeichner1(False, "")
            self.combobox_bezeichner2(False, "")
            self.textbox_bemerkung(False, "", "")
            self.combobox_leistung(True, "Leistung")
            self.current_func.bez1 = cb_text_position
            self.current_func.bez2 = cb_text_position
            self.current_func.note = cb_text_position
            self.current_func.service_spec = cb_text_position
            if self.current_func.bez1 != None:
                self.combobox_bezeichner1(True, "Leistung", *self.current_func.bez1)
                self.combobox_bezeichner2(False, "Leistung")
            if self.current_func.bez2 != None:
                self.combobox_bezeichner2(True, "Leistung", *self.current_func.bez2)
            if self.current_func.note != None:
                self.textbox_bemerkung(True, "Bemerkung", self.current_func.note)
                self.combobox_leistung(True, "Leistung", *self.current_func.service_spec)

    # Checkbox bezeichner 1 funktionen
    def auswahl_cbbezeichner1(self):
        cb1_text = self.comboBox_bezeichner1.currentText()
        self.current_func.note = cb1_text
        self.current_func.service_spec = cb1_text
        if self.current_func.note != None:
            self.textbox_bemerkung(True, "Bemerkung", self.current_func.note)
        if self.current_func.service_spec != None:
            self.combobox_leistung(True, "Leistung", *self.current_func.service_spec)

    # Checkbox bezeichner 2 funktionen
    def auswahl_cbbezeichner2(self):
        cb2_text = self.comboBox_bezeichner2.currentText()
        self.current_func.note = cb2_text
        self.current_func.service_spec = cb2_text
        if self.current_func.note != None:
            self.textbox_bemerkung(True, "Bemerkung", self.current_func.note)
        if self.current_func.service_spec != None:
            self.combobox_leistung(True, "Leistung", *self.current_func.service_spec)

    # Nach größe der Liste wird das Table Widget angepasst
    def defineTableWidget(self, begin=0, list=[]):
        self.tableWidget.setRowCount(begin)
        self.tableWidget.setColumnCount(len(list))
        self.tableWidget.setHorizontalHeaderLabels(list)
        self.tableWidget.itemChanged.connect(self.changed_data)
        self.tableWidget.itemClicked.connect(self.cell_clicked)

    # errechnen gesammtwert der AW
    def calc_sum(self, row):
        colmn = self.tableWidget.rowCount() - 1
        price = 0.0
        men = 0
        for col in range(0, colmn):
            price = price + float(self.tableWidget.item(col, row - 1).text())
            men = men + int(self.tableWidget.item(col, row - 4).text())
        kleinste = list(self.current_func.increase)[0]
        if men < kleinste:
            faktor = self.current_func.increase[int(kleinste)]["faktor"]
            return faktor, faktor * price
        else:
            for faktor in reversed(self.current_func.increase):
                if men >= int(faktor):
                    faktor = self.current_func.increase[int(faktor)]["faktor"]
                    return faktor, faktor * price

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
        for row in range(self.rowCountTable - 2):
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
        self.current_func.effortprice = leist
        fak1 = 0.0
        if bez1 != self._dashes[0]:
            self.current_func.bez1 = pos
            self.current_func.service_spec = bez1
            self.current_func.service_price = leist
            fak1 = float(self.current_func.service_price)
        fak2 = 0.0
        if bez2 != self._dashes[0]:
            self.current_func.bez2 = pos
            self.current_func.service_spec = bez2
            self.current_func.service_price = leist
            fak2 = float(self.current_func.service_price)
        wert = self.current_func.effortprice
        komi = self.lineEdit_kommentar.displayText()
        if fak1 == None or wert == None:
            komi = "Leistung nicht vorhanden!"
            self.show_popup_info(komi)
            return None
        return [
            komi, ber, bez1, bez2, pos, leist, men,
            "%.1f" % (fak1+fak2),
            str(self.prozent),
            "%.2f " % ((fak1+fak2) * (self.prozent / 100.0) * (wert * int(men)))
            ]

    # daten sammel für et
    def get_data_et(self):
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        leist = self.comboBox_Leistung.currentText()
        men = self.comboBox_menge.currentText()
        self.current_func.service_price = leist
        self.current_func.effortprice = leist
        fak = self.current_func.service_price
        wert = self.current_func.effortprice
        komi = self.lineEdit_kommentar.displayText()
        if fak == None or wert == None:
            komi = "Leistung nicht vorhanden!"
            self.show_popup_info(komi)
            return None
        return [
            komi, ber, pos, leist, men,
            str(fak),
            str(self.prozent),
            "%.2f " % (fak * (self.prozent / 100) * (wert * int(men)))
            ]

    # daten sammel für pls
    def get_data_pls(self):
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        bez1 = self.comboBox_bezeichner1.currentText()
        men = self.comboBox_menge.currentText()
        self.current_func.service_price = "programmierung"
        fak = self.current_func.service_price
        wert = self.current_func.effortprice
        komi = self.lineEdit_kommentar.displayText()
        if fak == None or wert == None:
            self.show_popup_info("Leistung ist nicht vorhanden!")
            return None
        return [
            komi, ber, bez1, pos, men,
            str(fak),
            str(self.prozent),
            "%.2f " % (fak * (self.prozent / 100) * (wert * int(men)))
            ]

    def cell_clicked(self):
        self.clicked = True

    # Daten änderungen in Table
    def changed_data(self, item):
        row = item.row()
        col = item.column()
        if col == self.tableWidget.columnCount() - 2 and self.clicked == True:
            #faktor = float(self.lookup[row + 1][0])
            price = float(self.lookup[row + 1][1])
            pro = float(self.tableWidget.item(row, self.tableWidget.columnCount() - 2).text()) / 100.0
            self.tableWidget.setItem(row, col + 1, QTableWidgetItem("%.2f " % (price*pro)))
            self.faktor, self.summe = self.calc_sum(len(self.current_func.table_header))
            self.label_ew(True, self.faktor, self.summe)
            self.clicked = False

    # funktion von hinzufügen button
    def push_hinzufügen(self):
        try:
            self.tableWidget.blockSignals(True)
            if self.comboBox_bereich.currentText() == "MSR":
                self.label_ew(False, 0.0, 0.0)
                msr_data = self.get_data_msr()
                self.set_table_cells([str(self.rowCountTable)] + msr_data.copy())
                self.faktor, self.summe = self.calc_sum(len(self.current_func.table_header))
                self.lookup[self.rowCountTable] = [msr_data[-3], msr_data[-1]]
                self.label_ew(True, self.faktor, self.summe)
                self.rowCountTable = self.rowCountTable + 1
                self.tableWidget.blockSignals(False)
            elif self.comboBox_bereich.currentText() == "ET":
                self.label_ew(False, 0.0, 0.0)
                if self.get_data_et() == None:
                    pass
                else:
                    self.set_table_cells([str(self.rowCountTable)] + self.get_data_et())
                    self.faktor, self.summe = self.calc_sum(len(self.current_func.table_header))
                    self.lookup[self.rowCountTable] = [self.get_data_et()[-3], self.get_data_et()[-1]]
                    self.label_ew(True, self.faktor, self.summe)
                    self.rowCountTable = self.rowCountTable + 1
                    self.tableWidget.blockSignals(False)
            elif self.comboBox_bereich.currentText() == "PLS":
                self.label_ew(False, 0.0, 0.0)
                if self.get_data_pls() == None:
                    pass
                else:
                    self.set_table_cells([str(self.rowCountTable)] + self.get_data_pls())
                    self.faktor, self.summe = self.calc_sum(len(self.current_func.table_header))
                    self.lookup[self.rowCountTable] = [self.get_data_pls()[-3], self.get_data_pls()[-1]]
                    self.label_ew(True, self.faktor, self.summe)
                    self.rowCountTable = self.rowCountTable + 1
                    self.tableWidget.blockSignals(False)
            else:
                pass
        except KeyError:
            self.show_popup_info("Eingabe sind nicht Vollständig/Fehlerhaft!")
            pass

    # Löschen der Ausgewählten Zeile!
    def push_löschen(self):
        if self.comboBox_bereich.currentText() == "---":
            pass
        else:
            indexes = self.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())
                self.new_lookup(int(index.row()) + 1)
                print(self.lookup)
                self.new_ids()
                self.rowCountTable = self.rowCountTable - 1
                self.label_ew(False, 0.0, 0.0)
                self.faktor, self.summe = self.calc_sum(len(self.current_func.table_header))
                self.label_ew(True, self.faktor, self.summe)

    # Protokoll wird erstellt nur wenn ein Inhalt in der Liste vorhanden ist.
    def push_erstellen(self):
        try:
            Daydate = date.today()
            txt_geber, geber = self.get_line_auftraggeber()
            txt_intern, intern = self.get_line_auftrag_intern()
            txt_extern, extern = self.get_line_auftrag_extern()
            txt_bearb, bearb = self.get_line_bearbeiter()
            data = self.get_table_data()
            self.create = createExcel(extern)
            self.create.file_properties(bearb)
            self.create.writeString(1, [["Datum: ", Daydate.strftime("%d.%m.%Y")]])
            self.create.writeString(
                1,
                [
                    [txt_geber, geber, "", "", "Kiel Engineering GmbH"],
                    [txt_intern, intern, "", "", "Niederlassung Wesseling"],
                    [txt_extern, extern, "", "", "Kölner Straße 65"], [txt_bearb, bearb, "", "", "50389 Wesseling"]
                    ],
                )
            self.create.writeString(0, [self.current_func.table_header])
            self.create.get_width([self.current_func.table_header])
            self.create.writeString(0, data)
            self.create.get_width(data)
            end_off_data = [["Mehrung von: ", self.faktor, "Gesammtbetrag: %.2f €" % (self.summe)]]
            self.create.writeString(len(self.current_func.table_header) - 3, end_off_data)
            self.create.get_width(end_off_data)
            self.create.set_width()
            self.create.close()
            self.show_popup_info("Bericht wurde Erfolgreicht Erstellt!")
        except AttributeError:
            pass

    def new_lookup(self, delete):
        len_lookup = len(list(self.lookup.keys()))
        for key in range(delete, len_lookup):
            self.lookup.update({key: self.lookup[key + 1]})
            last_key = key
        del self.lookup[last_key + 1]

    def new_ids(self):
        for row in range(self.rowCountTable - 2):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row + 1)))


def main():
    app = QApplication(sys.argv)
    form = AWApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
