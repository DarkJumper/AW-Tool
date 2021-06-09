# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AWMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AWTool(object):
    def setupUi(self, AWTool):
        AWTool.setObjectName("AWTool")
        AWTool.resize(1105, 997)
        AWTool.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(AWTool)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.grid.setObjectName("grid")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid.addItem(spacerItem, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(110, 16))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../img/dj2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.grid.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid.addItem(spacerItem1, 2, 4, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Kosten = QtWidgets.QLabel(self.centralwidget)
        self.label_Kosten.setObjectName("label_Kosten")
        self.horizontalLayout_10.addWidget(self.label_Kosten)
        self.label_faktor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_faktor.setFont(font)
        self.label_faktor.setAutoFillBackground(False)
        self.label_faktor.setObjectName("label_faktor")
        self.horizontalLayout_10.addWidget(self.label_faktor)
        self.label_sum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_sum.setFont(font)
        self.label_sum.setAutoFillBackground(False)
        self.label_sum.setObjectName("label_sum")
        self.horizontalLayout_10.addWidget(self.label_sum)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.grid.addLayout(self.horizontalLayout_10, 4, 0, 1, 4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_hinzufgen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hinzufgen.setObjectName("pushButton_hinzufgen")
        self.verticalLayout.addWidget(self.pushButton_hinzufgen)
        self.pushButton_loeschen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loeschen.setObjectName("pushButton_loeschen")
        self.verticalLayout.addWidget(self.pushButton_loeschen)
        self.pushButton_erstellen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_erstellen.setObjectName("pushButton_erstellen")
        self.verticalLayout.addWidget(self.pushButton_erstellen)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.grid.addLayout(self.verticalLayout, 1, 4, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Auftraggeber = QtWidgets.QLabel(self.centralwidget)
        self.label_Auftraggeber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Auftraggeber.setObjectName("label_Auftraggeber")
        self.verticalLayout_2.addWidget(self.label_Auftraggeber)
        self.label_Extern = QtWidgets.QLabel(self.centralwidget)
        self.label_Extern.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Extern.setObjectName("label_Extern")
        self.verticalLayout_2.addWidget(self.label_Extern)
        self.label_intern = QtWidgets.QLabel(self.centralwidget)
        self.label_intern.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_intern.setObjectName("label_intern")
        self.verticalLayout_2.addWidget(self.label_intern)
        self.label_bearbeiter = QtWidgets.QLabel(self.centralwidget)
        self.label_bearbeiter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bearbeiter.setObjectName("label_bearbeiter")
        self.verticalLayout_2.addWidget(self.label_bearbeiter)
        self.grid.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.pushButton_beenden = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_beenden.setObjectName("pushButton_beenden")
        self.grid.addWidget(self.pushButton_beenden, 4, 4, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Auftraggeber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Auftraggeber.setObjectName("lineEdit_Auftraggeber")
        self.gridLayout_2.addWidget(self.lineEdit_Auftraggeber, 0, 0, 1, 1)
        self.lineEdit_Extern = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Extern.setObjectName("lineEdit_Extern")
        self.gridLayout_2.addWidget(self.lineEdit_Extern, 1, 0, 1, 1)
        self.lineEdit_intern = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_intern.setObjectName("lineEdit_intern")
        self.gridLayout_2.addWidget(self.lineEdit_intern, 2, 0, 1, 1)
        self.lineEdit_bearbeiter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bearbeiter.setObjectName("lineEdit_bearbeiter")
        self.gridLayout_2.addWidget(self.lineEdit_bearbeiter, 3, 0, 1, 1)
        self.grid.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid.addItem(spacerItem4, 3, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_vers = QtWidgets.QLabel(self.centralwidget)
        self.label_vers.setObjectName("label_vers")
        self.horizontalLayout.addWidget(self.label_vers)
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout.addWidget(self.label_version)
        self.grid.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.grid.addWidget(self.tableWidget, 1, 0, 3, 4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.grid, 0, 0, 1, 1)
        AWTool.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(AWTool)
        self.toolBar.setObjectName("toolBar")
        AWTool.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(AWTool)
        self.statusbar.setObjectName("statusbar")
        AWTool.setStatusBar(self.statusbar)

        self.retranslateUi(AWTool)
        QtCore.QMetaObject.connectSlotsByName(AWTool)
        AWTool.setTabOrder(self.lineEdit_Auftraggeber, self.lineEdit_Extern)
        AWTool.setTabOrder(self.lineEdit_Extern, self.lineEdit_intern)
        AWTool.setTabOrder(self.lineEdit_intern, self.lineEdit_bearbeiter)
        AWTool.setTabOrder(self.lineEdit_bearbeiter, self.pushButton_hinzufgen)
        AWTool.setTabOrder(self.pushButton_hinzufgen, self.pushButton_loeschen)
        AWTool.setTabOrder(self.pushButton_loeschen, self.pushButton_erstellen)
        AWTool.setTabOrder(self.pushButton_erstellen, self.pushButton_beenden)
        AWTool.setTabOrder(self.pushButton_beenden, self.tableWidget)

    def retranslateUi(self, AWTool):
        _translate = QtCore.QCoreApplication.translate
        AWTool.setWindowTitle(_translate("AWTool", "MainWindow"))
        self.label_2.setText(_translate("AWTool", "Creator:"))
        self.label_Kosten.setText(_translate("AWTool", "Gesammt Kosten:"))
        self.label_faktor.setToolTip(_translate("AWTool", "<html><head/><body><p>Dieser Wert wird auf die gesammt summe gerechnet</p></body></html>"))
        self.label_faktor.setText(_translate("AWTool", "TextLabel"))
        self.label_sum.setText(_translate("AWTool", "TextLabel"))
        self.pushButton_hinzufgen.setText(_translate("AWTool", "Hinzufügen"))
        self.pushButton_loeschen.setText(_translate("AWTool", "Löschen"))
        self.pushButton_erstellen.setText(_translate("AWTool", "Bericht Erstellen"))
        self.label_Auftraggeber.setText(_translate("AWTool", "Auftraggeber"))
        self.label_Extern.setText(_translate("AWTool", "Auftragsnr. Extern"))
        self.label_intern.setText(_translate("AWTool", "Auftragsnr. Intern"))
        self.label_bearbeiter.setText(_translate("AWTool", "Bearbeiter"))
        self.pushButton_beenden.setText(_translate("AWTool", "Beenden"))
        self.label_vers.setText(_translate("AWTool", "Version:"))
        self.label_version.setText(_translate("AWTool", "----"))
        self.toolBar.setWindowTitle(_translate("AWTool", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AWTool = QtWidgets.QMainWindow()
    ui = Ui_AWTool()
    ui.setupUi(AWTool)
    AWTool.show()
    sys.exit(app.exec_())
