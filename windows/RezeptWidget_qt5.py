# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rezept.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rezept(object):
    def setupUi(self, Rezept):
        Rezept.setObjectName("Rezept")
        Rezept.resize(658, 531)
        Rezept.setMaximumSize(QtCore.QSize(1141, 531))
        self.gridLayout = QtWidgets.QGridLayout(Rezept)
        self.gridLayout.setObjectName("gridLayout")
        self.label_bereich = QtWidgets.QLabel(Rezept)
        self.label_bereich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bereich.setObjectName("label_bereich")
        self.gridLayout.addWidget(self.label_bereich, 1, 0, 1, 1)
        self.comboBox_leistung = QtWidgets.QComboBox(Rezept)
        self.comboBox_leistung.setObjectName("comboBox_leistung")
        self.gridLayout.addWidget(self.comboBox_leistung, 5, 2, 1, 1)
        self.lineEdit_Bemerkung = QtWidgets.QLineEdit(Rezept)
        self.lineEdit_Bemerkung.setObjectName("lineEdit_Bemerkung")
        self.gridLayout.addWidget(self.lineEdit_Bemerkung, 7, 2, 1, 1)
        self.label_bemerkung = QtWidgets.QLabel(Rezept)
        self.label_bemerkung.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bemerkung.setObjectName("label_bemerkung")
        self.gridLayout.addWidget(self.label_bemerkung, 7, 0, 1, 1)
        self.comboBox_bereich = QtWidgets.QComboBox(Rezept)
        self.comboBox_bereich.setObjectName("comboBox_bereich")
        self.gridLayout.addWidget(self.comboBox_bereich, 1, 2, 1, 1)
        self.label_bezeichnung2 = QtWidgets.QLabel(Rezept)
        self.label_bezeichnung2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bezeichnung2.setObjectName("label_bezeichnung2")
        self.gridLayout.addWidget(self.label_bezeichnung2, 4, 0, 1, 1)
        self.label_Leistung = QtWidgets.QLabel(Rezept)
        self.label_Leistung.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Leistung.setObjectName("label_Leistung")
        self.gridLayout.addWidget(self.label_Leistung, 5, 0, 1, 1)
        self.comboBox_bezeichnung2 = QtWidgets.QComboBox(Rezept)
        self.comboBox_bezeichnung2.setObjectName("comboBox_bezeichnung2")
        self.gridLayout.addWidget(self.comboBox_bezeichnung2, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Rezept)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_position = QtWidgets.QLabel(Rezept)
        self.label_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 2, 0, 1, 1)
        self.comboBox_bezeichnung1 = QtWidgets.QComboBox(Rezept)
        self.comboBox_bezeichnung1.setObjectName("comboBox_bezeichnung1")
        self.gridLayout.addWidget(self.comboBox_bezeichnung1, 3, 2, 1, 1)
        self.pushButton_anwenden = QtWidgets.QPushButton(Rezept)
        self.pushButton_anwenden.setObjectName("pushButton_anwenden")
        self.gridLayout.addWidget(self.pushButton_anwenden, 9, 2, 1, 1)
        self.pushButton_beenden = QtWidgets.QPushButton(Rezept)
        self.pushButton_beenden.setObjectName("pushButton_beenden")
        self.gridLayout.addWidget(self.pushButton_beenden, 9, 0, 1, 1)
        self.textBrowser_information = QtWidgets.QTextBrowser(Rezept)
        self.textBrowser_information.setObjectName("textBrowser_information")
        self.gridLayout.addWidget(self.textBrowser_information, 8, 2, 1, 1)
        self.label_bezeichnung1 = QtWidgets.QLabel(Rezept)
        self.label_bezeichnung1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bezeichnung1.setObjectName("label_bezeichnung1")
        self.gridLayout.addWidget(self.label_bezeichnung1, 3, 0, 1, 1)
        self.comboBox_position = QtWidgets.QComboBox(Rezept)
        self.comboBox_position.setObjectName("comboBox_position")
        self.gridLayout.addWidget(self.comboBox_position, 2, 2, 1, 1)
        self.label_information = QtWidgets.QLabel(Rezept)
        self.label_information.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_information.setObjectName("label_information")
        self.gridLayout.addWidget(self.label_information, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Rezept)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Rezept)
        self.label_3.setMaximumSize(QtCore.QSize(110, 16))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../img/dj2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 2, 1, 1)

        self.retranslateUi(Rezept)
        QtCore.QMetaObject.connectSlotsByName(Rezept)

    def retranslateUi(self, Rezept):
        _translate = QtCore.QCoreApplication.translate
        Rezept.setWindowTitle(_translate("Rezept", "Form"))
        self.label_bereich.setText(_translate("Rezept", "Bereich"))
        self.label_bemerkung.setText(_translate("Rezept", "Bemerkung"))
        self.label_bezeichnung2.setText(_translate("Rezept", "Bezeichnung 2"))
        self.label_Leistung.setText(_translate("Rezept", "Leistung"))
        self.label.setText(_translate("Rezept", "Leistung Einfügen"))
        self.label_position.setText(_translate("Rezept", "Position"))
        self.pushButton_anwenden.setText(_translate("Rezept", "Anwenden"))
        self.pushButton_beenden.setText(_translate("Rezept", "Beenden"))
        self.label_bezeichnung1.setText(_translate("Rezept", "Bezeichnung 1"))
        self.label_information.setText(_translate("Rezept", "Information:"))
        self.label_2.setText(_translate("Rezept", "Creator:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rezept = QtWidgets.QWidget()
    ui = Ui_Rezept()
    ui.setupUi(Rezept)
    Rezept.show()
    sys.exit(app.exec_())