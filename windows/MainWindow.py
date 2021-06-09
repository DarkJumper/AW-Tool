# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AWMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_AWTool(object):
    def setupUi(self, AWTool):
        if not AWTool.objectName():
            AWTool.setObjectName(u"AWTool")
        AWTool.resize(1105, 997)
        AWTool.setDocumentMode(False)
        self.centralwidget = QWidget(AWTool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grid = QGridLayout()
        self.grid.setObjectName(u"grid")
        self.grid.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(110, 16))
        self.label_5.setPixmap(QPixmap(u"../img/dj2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.grid.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grid.addItem(self.verticalSpacer_2, 2, 4, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_Kosten = QLabel(self.centralwidget)
        self.label_Kosten.setObjectName(u"label_Kosten")

        self.horizontalLayout_10.addWidget(self.label_Kosten)

        self.label_faktor = QLabel(self.centralwidget)
        self.label_faktor.setObjectName(u"label_faktor")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_faktor.setFont(font)
        self.label_faktor.setAutoFillBackground(False)

        self.horizontalLayout_10.addWidget(self.label_faktor)

        self.label_sum = QLabel(self.centralwidget)
        self.label_sum.setObjectName(u"label_sum")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_sum.setFont(font1)
        self.label_sum.setAutoFillBackground(False)

        self.horizontalLayout_10.addWidget(self.label_sum)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.grid.addLayout(self.horizontalLayout_10, 4, 0, 1, 4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_hinzufgen = QPushButton(self.centralwidget)
        self.pushButton_hinzufgen.setObjectName(u"pushButton_hinzufgen")

        self.verticalLayout.addWidget(self.pushButton_hinzufgen)

        self.pushButton_loeschen = QPushButton(self.centralwidget)
        self.pushButton_loeschen.setObjectName(u"pushButton_loeschen")

        self.verticalLayout.addWidget(self.pushButton_loeschen)

        self.pushButton_erstellen = QPushButton(self.centralwidget)
        self.pushButton_erstellen.setObjectName(u"pushButton_erstellen")

        self.verticalLayout.addWidget(self.pushButton_erstellen)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.grid.addLayout(self.verticalLayout, 1, 4, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_Auftraggeber = QLabel(self.centralwidget)
        self.label_Auftraggeber.setObjectName(u"label_Auftraggeber")
        self.label_Auftraggeber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_Auftraggeber)

        self.label_Extern = QLabel(self.centralwidget)
        self.label_Extern.setObjectName(u"label_Extern")
        self.label_Extern.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_Extern)

        self.label_intern = QLabel(self.centralwidget)
        self.label_intern.setObjectName(u"label_intern")
        self.label_intern.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_intern)

        self.label_bearbeiter = QLabel(self.centralwidget)
        self.label_bearbeiter.setObjectName(u"label_bearbeiter")
        self.label_bearbeiter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_bearbeiter)


        self.grid.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.pushButton_beenden = QPushButton(self.centralwidget)
        self.pushButton_beenden.setObjectName(u"pushButton_beenden")

        self.grid.addWidget(self.pushButton_beenden, 4, 4, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_Auftraggeber = QLineEdit(self.centralwidget)
        self.lineEdit_Auftraggeber.setObjectName(u"lineEdit_Auftraggeber")

        self.gridLayout_2.addWidget(self.lineEdit_Auftraggeber, 0, 0, 1, 1)

        self.lineEdit_Extern = QLineEdit(self.centralwidget)
        self.lineEdit_Extern.setObjectName(u"lineEdit_Extern")

        self.gridLayout_2.addWidget(self.lineEdit_Extern, 1, 0, 1, 1)

        self.lineEdit_intern = QLineEdit(self.centralwidget)
        self.lineEdit_intern.setObjectName(u"lineEdit_intern")

        self.gridLayout_2.addWidget(self.lineEdit_intern, 2, 0, 1, 1)

        self.lineEdit_bearbeiter = QLineEdit(self.centralwidget)
        self.lineEdit_bearbeiter.setObjectName(u"lineEdit_bearbeiter")

        self.gridLayout_2.addWidget(self.lineEdit_bearbeiter, 3, 0, 1, 1)


        self.grid.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grid.addItem(self.verticalSpacer_3, 3, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_vers = QLabel(self.centralwidget)
        self.label_vers.setObjectName(u"label_vers")

        self.horizontalLayout.addWidget(self.label_vers)

        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName(u"label_version")

        self.horizontalLayout.addWidget(self.label_version)


        self.grid.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.grid.addWidget(self.tableWidget, 1, 0, 3, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.grid, 0, 0, 1, 1)

        AWTool.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(AWTool)
        self.toolBar.setObjectName(u"toolBar")
        AWTool.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QStatusBar(AWTool)
        self.statusbar.setObjectName(u"statusbar")
        AWTool.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_Auftraggeber, self.lineEdit_Extern)
        QWidget.setTabOrder(self.lineEdit_Extern, self.lineEdit_intern)
        QWidget.setTabOrder(self.lineEdit_intern, self.lineEdit_bearbeiter)
        QWidget.setTabOrder(self.lineEdit_bearbeiter, self.pushButton_hinzufgen)
        QWidget.setTabOrder(self.pushButton_hinzufgen, self.pushButton_loeschen)
        QWidget.setTabOrder(self.pushButton_loeschen, self.pushButton_erstellen)
        QWidget.setTabOrder(self.pushButton_erstellen, self.pushButton_beenden)
        QWidget.setTabOrder(self.pushButton_beenden, self.tableWidget)

        self.retranslateUi(AWTool)

        QMetaObject.connectSlotsByName(AWTool)
    # setupUi

    def retranslateUi(self, AWTool):
        AWTool.setWindowTitle(QCoreApplication.translate("AWTool", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("AWTool", u"Creator:", None))
        self.label_5.setText("")
        self.label_Kosten.setText(QCoreApplication.translate("AWTool", u"Gesammt Kosten:", None))
#if QT_CONFIG(tooltip)
        self.label_faktor.setToolTip(QCoreApplication.translate("AWTool", u"<html><head/><body><p>Dieser Wert wird auf die gesammt summe gerechnet</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_faktor.setText(QCoreApplication.translate("AWTool", u"TextLabel", None))
        self.label_sum.setText(QCoreApplication.translate("AWTool", u"TextLabel", None))
        self.pushButton_hinzufgen.setText(QCoreApplication.translate("AWTool", u"Hinzuf\u00fcgen", None))
        self.pushButton_loeschen.setText(QCoreApplication.translate("AWTool", u"L\u00f6schen", None))
        self.pushButton_erstellen.setText(QCoreApplication.translate("AWTool", u"Bericht Erstellen", None))
        self.label_Auftraggeber.setText(QCoreApplication.translate("AWTool", u"Auftraggeber", None))
        self.label_Extern.setText(QCoreApplication.translate("AWTool", u"Auftragsnr. Extern", None))
        self.label_intern.setText(QCoreApplication.translate("AWTool", u"Auftragsnr. Intern", None))
        self.label_bearbeiter.setText(QCoreApplication.translate("AWTool", u"Bearbeiter", None))
        self.pushButton_beenden.setText(QCoreApplication.translate("AWTool", u"Beenden", None))
        self.label_vers.setText(QCoreApplication.translate("AWTool", u"Version:", None))
        self.label_version.setText(QCoreApplication.translate("AWTool", u"----", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("AWTool", u"toolBar", None))
    # retranslateUi

