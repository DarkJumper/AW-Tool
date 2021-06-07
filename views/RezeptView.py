from PySide6 import QtWidgets

from .ClearingRate import AW, MSR, ET, PLS
from .windows.RezeptWidget import Ui_Rezept


class RezeptWindow(QtWidgets.QWidget, Ui_Rezept):

    _dashes = "---"
    _bereiche = ["MSR", "ET", "PLS"]

    def __init__(self):
        super(RezeptWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_beenden.clicked.connect(self.push_beenden)
        self.rezept_data = AW()
        self.comboBox_bereich.addItems([self._dashes] + self.rezept_data.services)
        self.comboBox_position.addItems([self._dashes])
        self.comboBox_bezeichnung1.addItems([self._dashes])
        self.comboBox_bezeichnung2.addItems([self._dashes])
        self.comboBox_leistung.addItems([self._dashes])
        self.comboBox_bereich.currentTextChanged.connect(self.select_cbbereich)
        self.comboBox_position.currentTextChanged.connect(self.select_cbposition)
        self.comboBox_bezeichnung1.currentTextChanged.connect(self.select_bez1)

    def select_cbbereich(self, text):
        if text == self._dashes:
            self.cb_position_vis()
            self.cb_bez1_vis("Bezeichnung 1")
            self.cb_bez2_vis("Bezeichnung 2")
            self.textBrowser_information.setText("")
            self.cb_leistung_vis()
        elif text == self._bereiche[0]:
            self.rezept_data.area = MSR
            self.cb_position_vis(*self.rezept_data.position)
        elif text == self._bereiche[1]:
            self.rezept_data.area = ET
            self.cb_position_vis(*self.rezept_data.position)
        elif text == self._bereiche[2]:
            self.rezept_data.area = PLS
            self.cb_position_vis(*self.rezept_data.position)

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

    def push_beenden(self, checked):
        self.hide()
