# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AW-GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AWTool(object):
    def setupUi(self, AWTool):
        AWTool.setObjectName("AWTool")
        AWTool.resize(946, 730)
        self.centralwidget = QtWidgets.QWidget(AWTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(760, 340, 160, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_hinzufgen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_hinzufgen.setObjectName("pushButton_hinzufgen")
        self.verticalLayout.addWidget(self.pushButton_hinzufgen)
        self.pushButton_loeschen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_loeschen.setObjectName("pushButton_loeschen")
        self.verticalLayout.addWidget(self.pushButton_loeschen)
        self.pushButton_erstellen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_erstellen.setObjectName("pushButton_erstellen")
        self.verticalLayout.addWidget(self.pushButton_erstellen)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 300, 731, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_kommentar = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_kommentar.setObjectName("lineEdit_kommentar")
        self.horizontalLayout_4.addWidget(self.lineEdit_kommentar)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(520, 240, 154, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_menge = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_menge.setObjectName("label_menge")
        self.horizontalLayout_6.addWidget(self.label_menge)
        self.comboBox_menge = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_menge.setObjectName("comboBox_menge")
        self.horizontalLayout_6.addWidget(self.comboBox_menge)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(320, 630, 431, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Kosten = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_Kosten.setObjectName("label_Kosten")
        self.horizontalLayout_10.addWidget(self.label_Kosten)
        self.label_faktor = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_faktor.setFont(font)
        self.label_faktor.setAutoFillBackground(False)
        self.label_faktor.setObjectName("label_faktor")
        self.horizontalLayout_10.addWidget(self.label_faktor)
        self.label_sum = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_sum.setFont(font)
        self.label_sum.setAutoFillBackground(False)
        self.label_sum.setObjectName("label_sum")
        self.horizontalLayout_10.addWidget(self.label_sum)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 340, 731, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 20, 331, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(350, 240, 162, 31))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_leistung = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.label_leistung.setObjectName("label_leistung")
        self.horizontalLayout_12.addWidget(self.label_leistung)
        self.comboBox_Leistung = QtWidgets.QComboBox(self.horizontalLayoutWidget_12)
        self.comboBox_Leistung.setObjectName("comboBox_Leistung")
        self.horizontalLayout_12.addWidget(self.comboBox_Leistung)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 121, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Auftraggeber = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_Auftraggeber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Auftraggeber.setObjectName("label_Auftraggeber")
        self.verticalLayout_2.addWidget(self.label_Auftraggeber)
        self.label_Extern = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_Extern.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Extern.setObjectName("label_Extern")
        self.verticalLayout_2.addWidget(self.label_Extern)
        self.label_intern = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_intern.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_intern.setObjectName("label_intern")
        self.verticalLayout_2.addWidget(self.label_intern)
        self.label_bearbeiter = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_bearbeiter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bearbeiter.setObjectName("label_bearbeiter")
        self.verticalLayout_2.addWidget(self.label_bearbeiter)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(150, 20, 181, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_Auftraggeber = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_Auftraggeber.setObjectName("lineEdit_Auftraggeber")
        self.verticalLayout_3.addWidget(self.lineEdit_Auftraggeber)
        self.lineEdit_Extern = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_Extern.setObjectName("lineEdit_Extern")
        self.verticalLayout_3.addWidget(self.lineEdit_Extern)
        self.lineEdit_intern = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_intern.setObjectName("lineEdit_intern")
        self.verticalLayout_3.addWidget(self.lineEdit_intern)
        self.lineEdit_bearbeiter = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_bearbeiter.setObjectName("lineEdit_bearbeiter")
        self.verticalLayout_3.addWidget(self.lineEdit_bearbeiter)
        self.comboBox_bereich = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_bereich.setGeometry(QtCore.QRect(150, 150, 181, 26))
        self.comboBox_bereich.setObjectName("comboBox_bereich")
        self.comboBox_position = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_position.setGeometry(QtCore.QRect(150, 180, 181, 26))
        self.comboBox_position.setMaxVisibleItems(10)
        self.comboBox_position.setObjectName("comboBox_position")
        self.comboBox_bezeichner1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_bezeichner1.setGeometry(QtCore.QRect(150, 210, 181, 26))
        self.comboBox_bezeichner1.setObjectName("comboBox_bezeichner1")
        self.comboBox_bezeichner2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_bezeichner2.setGeometry(QtCore.QRect(150, 240, 181, 26))
        self.comboBox_bezeichner2.setObjectName("comboBox_bezeichner2")
        self.label_bereich = QtWidgets.QLabel(self.centralwidget)
        self.label_bereich.setGeometry(QtCore.QRect(20, 150, 119, 24))
        self.label_bereich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bereich.setObjectName("label_bereich")
        self.label_position = QtWidgets.QLabel(self.centralwidget)
        self.label_position.setGeometry(QtCore.QRect(20, 180, 119, 21))
        self.label_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_position.setObjectName("label_position")
        self.label_bezeichner1 = QtWidgets.QLabel(self.centralwidget)
        self.label_bezeichner1.setGeometry(QtCore.QRect(20, 210, 119, 21))
        self.label_bezeichner1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bezeichner1.setObjectName("label_bezeichner1")
        self.label_bezeichner2 = QtWidgets.QLabel(self.centralwidget)
        self.label_bezeichner2.setGeometry(QtCore.QRect(20, 240, 119, 21))
        self.label_bezeichner2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bezeichner2.setObjectName("label_bezeichner2")
        self.label_copyright = QtWidgets.QLabel(self.centralwidget)
        self.label_copyright.setGeometry(QtCore.QRect(20, 630, 261, 16))
        self.label_copyright.setObjectName("label_copyright")
        self.label_vers = QtWidgets.QLabel(self.centralwidget)
        self.label_vers.setGeometry(QtCore.QRect(20, 650, 61, 16))
        self.label_vers.setObjectName("label_vers")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(80, 650, 61, 16))
        self.label_version.setObjectName("label_version")
        self.pushButton_beenden = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_beenden.setGeometry(QtCore.QRect(760, 630, 160, 32))
        self.pushButton_beenden.setObjectName("pushButton_beenden")
        AWTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AWTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 22))
        self.menubar.setObjectName("menubar")
        AWTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AWTool)
        self.statusbar.setObjectName("statusbar")
        AWTool.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(AWTool)
        self.toolBar.setObjectName("toolBar")
        AWTool.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(AWTool)
        QtCore.QMetaObject.connectSlotsByName(AWTool)

    def retranslateUi(self, AWTool):
        _translate = QtCore.QCoreApplication.translate
        AWTool.setWindowTitle(_translate("AWTool", "MainWindow"))
        self.pushButton_hinzufgen.setText(_translate("AWTool", "Hinzufügen"))
        self.pushButton_loeschen.setText(_translate("AWTool", "Löschen"))
        self.pushButton_erstellen.setText(_translate("AWTool", "Bericht Erstellen"))
        self.label_4.setText(_translate("AWTool", "Kommentar"))
        self.label_menge.setText(_translate("AWTool", "Menge"))
        self.label_Kosten.setText(_translate("AWTool", "Gesammt Kosten:"))
        self.label_faktor.setToolTip(_translate("AWTool", "<html><head/><body><p>Dieser Wert wird auf die gesammt summe gerechnet</p></body></html>"))
        self.label_faktor.setText(_translate("AWTool", "TextLabel"))
        self.label_sum.setText(_translate("AWTool", "TextLabel"))
        self.label.setText(_translate("AWTool", "Bemerkung:"))
        self.label_leistung.setText(_translate("AWTool", "Leistung"))
        self.label_Auftraggeber.setText(_translate("AWTool", "Auftraggeber"))
        self.label_Extern.setText(_translate("AWTool", "Auftragsnr. Extern"))
        self.label_intern.setText(_translate("AWTool", "Auftragsnr. Intern"))
        self.label_bearbeiter.setText(_translate("AWTool", "Bearbeiter"))
        self.label_bereich.setText(_translate("AWTool", "Planungsbereich"))
        self.label_position.setText(_translate("AWTool", "Position"))
        self.label_bezeichner1.setText(_translate("AWTool", "Bezeichnung 1"))
        self.label_bezeichner2.setText(_translate("AWTool", "Bezeichnung 2"))
        self.label_copyright.setText(_translate("AWTool", "copyright Peter Schwarz Dezember 2020"))
        self.label_vers.setText(_translate("AWTool", "Version:"))
        self.label_version.setText(_translate("AWTool", "----"))
        self.pushButton_beenden.setText(_translate("AWTool", "Beenden"))
        self.toolBar.setWindowTitle(_translate("AWTool", "toolBar"))
