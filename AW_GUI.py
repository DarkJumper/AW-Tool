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
        AWTool.resize(803, 730)
        self.centralwidget = QtWidgets.QWidget(AWTool)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_intern = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_intern.setObjectName("label_intern")
        self.horizontalLayout.addWidget(self.label_intern)
        self.lineEdit_intern = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_intern.setObjectName("lineEdit_intern")
        self.horizontalLayout.addWidget(self.lineEdit_intern)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 291, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Extern = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_Extern.setObjectName("label_Extern")
        self.horizontalLayout_2.addWidget(self.label_Extern)
        self.lineEdit_Extern = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_Extern.setObjectName("lineEdit_Extern")
        self.horizontalLayout_2.addWidget(self.lineEdit_Extern)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Auftraggeber = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_Auftraggeber.setObjectName("label_Auftraggeber")
        self.horizontalLayout_3.addWidget(self.label_Auftraggeber)
        self.lineEdit_Auftraggeber = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_Auftraggeber.setObjectName("lineEdit_Auftraggeber")
        self.horizontalLayout_3.addWidget(self.lineEdit_Auftraggeber)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 340, 160, 134))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_loeschen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_loeschen.setObjectName("pushButton_loeschen")
        self.verticalLayout.addWidget(self.pushButton_loeschen)
        self.pushButton_erstellen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_erstellen.setObjectName("pushButton_erstellen")
        self.verticalLayout.addWidget(self.pushButton_erstellen)
        self.pushButton_beenden = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_beenden.setObjectName("pushButton_beenden")
        self.verticalLayout.addWidget(self.pushButton_beenden)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 290, 501, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_kommentar = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_kommentar.setObjectName("lineEdit_kommentar")
        self.horizontalLayout_4.addWidget(self.lineEdit_kommentar)
        self.pushButton_hinzufgen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hinzufgen.setGeometry(QtCore.QRect(620, 290, 160, 32))
        self.pushButton_hinzufgen.setObjectName("pushButton_hinzufgen")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 240, 241, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_bezeichner2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_bezeichner2.setObjectName("label_bezeichner2")
        self.horizontalLayout_5.addWidget(self.label_bezeichner2)
        self.comboBox_bezeichner2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_bezeichner2.setObjectName("comboBox_bezeichner2")
        self.horizontalLayout_5.addWidget(self.comboBox_bezeichner2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(530, 290, 91, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_menge = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_menge.setObjectName("label_menge")
        self.horizontalLayout_6.addWidget(self.label_menge)
        self.comboBox_bereich_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_bereich_2.setObjectName("comboBox_bereich_2")
        self.horizontalLayout_6.addWidget(self.comboBox_bereich_2)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 150, 241, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_bereich = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_bereich.setObjectName("label_bereich")
        self.horizontalLayout_7.addWidget(self.label_bereich)
        self.comboBox_bereich = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.comboBox_bereich.setObjectName("comboBox_bereich")
        self.horizontalLayout_7.addWidget(self.comboBox_bereich)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 180, 241, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_position = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_position.setObjectName("label_position")
        self.horizontalLayout_8.addWidget(self.label_position)
        self.comboBox_position = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        self.comboBox_position.setObjectName("comboBox_position")
        self.horizontalLayout_8.addWidget(self.comboBox_position)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 110, 291, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_bearbeiter = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_bearbeiter.setObjectName("label_bearbeiter")
        self.horizontalLayout_9.addWidget(self.label_bearbeiter)
        self.lineEdit_bearbeiter = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_bearbeiter.setObjectName("lineEdit_bearbeiter")
        self.horizontalLayout_9.addWidget(self.lineEdit_bearbeiter)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(310, 630, 301, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Kosten = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_Kosten.setObjectName("label_Kosten")
        self.horizontalLayout_10.addWidget(self.label_Kosten)
        self.label_sum = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_sum.setFont(font)
        self.label_sum.setAutoFillBackground(False)
        self.label_sum.setObjectName("label_sum")
        self.horizontalLayout_10.addWidget(self.label_sum)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(20, 210, 241, 31))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_bezeichner1 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_bezeichner1.setObjectName("label_bezeichner1")
        self.horizontalLayout_11.addWidget(self.label_bezeichner1)
        self.comboBox_bezeichner1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_11)
        self.comboBox_bezeichner1.setObjectName("comboBox_bezeichner1")
        self.horizontalLayout_11.addWidget(self.comboBox_bezeichner1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 340, 601, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 81, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(420, 20, 351, 261))
        self.textBrowser.setObjectName("textBrowser")
        AWTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AWTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 22))
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
        self.label_intern.setText(_translate("AWTool", "Auftragsnr. Intern"))
        self.label_Extern.setText(_translate("AWTool", "Auftragsnr. Extern"))
        self.label_Auftraggeber.setText(_translate("AWTool", "Auftraggeber"))
        self.pushButton_loeschen.setText(_translate("AWTool", "Löschen"))
        self.pushButton_erstellen.setText(_translate("AWTool", "Bericht Erstellen"))
        self.pushButton_beenden.setText(_translate("AWTool", "Beenden"))
        self.label_4.setText(_translate("AWTool", "Kommentar"))
        self.pushButton_hinzufgen.setText(_translate("AWTool", "Hinzufügen"))
        self.label_bezeichner2.setText(_translate("AWTool", "Bezeichnung 2"))
        self.label_menge.setText(_translate("AWTool", "Menge"))
        self.label_bereich.setText(_translate("AWTool", "Planungsbereich"))
        self.label_position.setText(_translate("AWTool", "Position"))
        self.label_bearbeiter.setText(_translate("AWTool", "Bearbeiter"))
        self.label_Kosten.setText(_translate("AWTool", "Gesammt Kosten:"))
        self.label_sum.setText(_translate("AWTool", "TextLabel"))
        self.label_bezeichner1.setText(_translate("AWTool", "Bezeichnung 1"))
        self.label.setText(_translate("AWTool", "Bemerkung:"))
        self.toolBar.setWindowTitle(_translate("AWTool", "toolBar"))
