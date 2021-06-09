from PyQt5 import QtWidgets

from moduls.ClearingRate import AW, MSR, ET, PLS
from windows.RezeptWidget_qt5 import Ui_Rezept
from model.TableModel import TableModel


class RezeptWindow(QtWidgets.QWidget, Ui_Rezept):

    _dashes = "---"
    _bereiche = ["MSR", "ET", "PLS"]

    def __init__(self, tableWidget):
        super(RezeptWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_beenden.clicked.connect(self.push_beenden)
        self.rezept_data = AW()
        self.table = tableWidget
        self.model = TableModel(self.table)
        self.comboBox_bereich.addItems([self._dashes] + self.rezept_data.services)
        self.comboBox_position.addItems([self._dashes])
        self.comboBox_bezeichnung1.addItems([self._dashes])
        self.comboBox_bezeichnung2.addItems([self._dashes])
        self.comboBox_leistung.addItems([self._dashes])
        self.comboBox_bereich.currentTextChanged.connect(self.select_cbbereich)
        self.comboBox_position.currentTextChanged.connect(self.select_cbposition)
        self.comboBox_bezeichnung1.currentTextChanged.connect(self.select_bez1)
        self.pushButton_anwenden.clicked.connect(self.apply_service)

    def show_popup_info(self, string):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(string)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec()

    def select_cbbereich(self, text):
        if text == self._dashes:
            self.cb_position_vis()
            self.cb_bez1_vis("Bezeichnung 1")
            self.cb_bez2_vis("Bezeichnung 2")
            self.textBrowser_information.setText("")
            self.cb_leistung_vis()
            self.model.header()
        elif text == self._bereiche[0]:
            self.rezept_data.area = MSR
            self.cb_position_vis(*self.rezept_data.position)
            self.model.header(self.rezept_data.table_header)
        elif text == self._bereiche[1]:
            self.rezept_data.area = ET
            self.cb_position_vis(*self.rezept_data.position)
            self.model.header(self.rezept_data.table_header)
        elif text == self._bereiche[2]:
            self.rezept_data.area = PLS
            self.cb_position_vis(*self.rezept_data.position)
            self.model.header(self.rezept_data.table_header)

    def cb_position_vis(self, *args):
        self.comboBox_position.clear()
        self.comboBox_position.addItems([self._dashes] + list(args))
        self.comboBox_position.setCurrentIndex(0)

    def select_cbposition(self, text):
        if text == self._dashes or text == "":
            self.cb_bez1_vis("Bezeichnung 1")
            self.cb_bez2_vis("Bezeichnung 2")
            self.textBrowser_information.setText("")
            self.cb_leistung_vis()
        else:
            self.rezept_data.bez1 = text
            self.rezept_data.bez2 = text
            self.rezept_data.note = text
            if self.rezept_data.bez1 != None:
                self.cb_bez1_vis("Bezeichnung 1", *self.rezept_data.bez1)
                self.cb_bez2_vis("Bezeichnung 2")
            if self.rezept_data.bez2 != None:
                self.cb_bez2_vis("Bezeichnung 2", *self.rezept_data.bez2)
            if self.rezept_data.note != None:
                self.textBrowser_information.setText(self.rezept_data.note)
                self.rezept_data.service_spec = text
                self.cb_leistung_vis(*self.rezept_data.service_spec)

    def cb_bez1_vis(self, txt, *args):
        self.comboBox_bezeichnung1.clear()
        self.comboBox_bezeichnung1.addItems([self._dashes] + list(args))
        self.comboBox_bezeichnung1.setCurrentIndex(0)
        self.label_bezeichnung1.setText(txt)

    def select_bez1(self, text):
        if text == self._dashes or text == "":
            pass
        else:
            self.rezept_data.note = text
            self.rezept_data.service_spec = text
            if self.rezept_data.note != None:
                self.textBrowser_information.setText(self.rezept_data.note)
            if self.rezept_data.service_spec != None:
                self.cb_leistung_vis(*self.rezept_data.service_spec)

    def cb_bez2_vis(self, txt, *args):
        self.comboBox_bezeichnung2.clear()
        self.comboBox_bezeichnung2.addItems([self._dashes] + list(args))
        self.comboBox_bezeichnung2.setCurrentIndex(0)
        self.label_bezeichnung2.setText(txt)

    def cb_leistung_vis(self, *args):
        self.comboBox_leistung.clear()
        self.comboBox_leistung.addItems([self._dashes] + list(args))
        self.comboBox_leistung.setCurrentIndex(0)

    def apply_service(self, clicked):
        bem = self.lineEdit_Bemerkung.displayText()
        ber = self.comboBox_bereich.currentText()
        pos = self.comboBox_position.currentText()
        bez1 = self.comboBox_bezeichnung1.currentText()
        bez2 = self.comboBox_bezeichnung2.currentText()
        leist = self.comboBox_leistung.currentText()
        if isinstance(self.rezept_data.area, ET):
            self.rezept_data.service_price = leist
            self.rezept_data.effortprice = leist
            fak = self.rezept_data.service_price
            wert = self.rezept_data.effortprice
        if isinstance(self.rezept_data.area, PLS):
            self.rezept_data.effortprice = leist
            self.rezept_data.service_price = "programmierung"
            fak = self.rezept_data.service_price
            wert = self.rezept_data.effortprice
        if isinstance(self.rezept_data.area, MSR):
            self.rezept_data.effortprice = leist
            fak1 = 0.0
            if bez1 != self._dashes:
                self.rezept_data.bez1 = pos
                self.rezept_data.service_spec = bez1
                self.rezept_data.service_price = leist
                fak1 = float(self.rezept_data.service_price)
            fak2 = 0.0
            if bez2 != self._dashes:
                self.rezept_data.bez2 = pos
                self.rezept_data.service_spec = bez2
                self.rezept_data.service_price = leist
                fak2 = float(self.rezept_data.service_price)
            wert = self.rezept_data.effortprice
            if fak1 is None or fak2 is None:
                fak = None
            fak = fak1 + fak2
        if fak is None or wert is None or isinstance(fak, str):
            komi = "Leistung nicht vorhanden!"
            self.show_popup_info(komi)
            return None
        self.model.data([bem, ber, pos, bez1, bez2, leist, str(wert), str(fak), str(100.0), "%.2f " % (fak*wert)])

    def push_beenden(self, checked):
        self.hide()
