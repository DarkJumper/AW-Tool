# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rezept.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Rezept(object):
    def setupUi(self, Rezept):
        if not Rezept.objectName():
            Rezept.setObjectName(u"Rezept")
        Rezept.resize(658, 531)
        Rezept.setMaximumSize(QSize(1141, 531))
        self.gridLayout = QGridLayout(Rezept)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_bereich = QLabel(Rezept)
        self.label_bereich.setObjectName(u"label_bereich")
        self.label_bereich.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bereich, 1, 0, 1, 1)

        self.comboBox_leistung = QComboBox(Rezept)
        self.comboBox_leistung.setObjectName(u"comboBox_leistung")

        self.gridLayout.addWidget(self.comboBox_leistung, 5, 2, 1, 1)

        self.lineEdit_Bemerkung = QLineEdit(Rezept)
        self.lineEdit_Bemerkung.setObjectName(u"lineEdit_Bemerkung")

        self.gridLayout.addWidget(self.lineEdit_Bemerkung, 7, 2, 1, 1)

        self.label_bemerkung = QLabel(Rezept)
        self.label_bemerkung.setObjectName(u"label_bemerkung")
        self.label_bemerkung.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bemerkung, 7, 0, 1, 1)

        self.comboBox_bereich = QComboBox(Rezept)
        self.comboBox_bereich.setObjectName(u"comboBox_bereich")

        self.gridLayout.addWidget(self.comboBox_bereich, 1, 2, 1, 1)

        self.label_bezeichnung2 = QLabel(Rezept)
        self.label_bezeichnung2.setObjectName(u"label_bezeichnung2")
        self.label_bezeichnung2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bezeichnung2, 4, 0, 1, 1)

        self.label_Leistung = QLabel(Rezept)
        self.label_Leistung.setObjectName(u"label_Leistung")
        self.label_Leistung.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_Leistung, 5, 0, 1, 1)

        self.comboBox_bezeichnung2 = QComboBox(Rezept)
        self.comboBox_bezeichnung2.setObjectName(u"comboBox_bezeichnung2")

        self.gridLayout.addWidget(self.comboBox_bezeichnung2, 4, 2, 1, 1)

        self.label = QLabel(Rezept)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_position = QLabel(Rezept)
        self.label_position.setObjectName(u"label_position")
        self.label_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_position, 2, 0, 1, 1)

        self.comboBox_bezeichnung1 = QComboBox(Rezept)
        self.comboBox_bezeichnung1.setObjectName(u"comboBox_bezeichnung1")

        self.gridLayout.addWidget(self.comboBox_bezeichnung1, 3, 2, 1, 1)

        self.pushButton_anwenden = QPushButton(Rezept)
        self.pushButton_anwenden.setObjectName(u"pushButton_anwenden")

        self.gridLayout.addWidget(self.pushButton_anwenden, 9, 2, 1, 1)

        self.pushButton_beenden = QPushButton(Rezept)
        self.pushButton_beenden.setObjectName(u"pushButton_beenden")

        self.gridLayout.addWidget(self.pushButton_beenden, 9, 0, 1, 1)

        self.textBrowser_information = QTextBrowser(Rezept)
        self.textBrowser_information.setObjectName(u"textBrowser_information")

        self.gridLayout.addWidget(self.textBrowser_information, 8, 2, 1, 1)

        self.label_bezeichnung1 = QLabel(Rezept)
        self.label_bezeichnung1.setObjectName(u"label_bezeichnung1")
        self.label_bezeichnung1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bezeichnung1, 3, 0, 1, 1)

        self.comboBox_position = QComboBox(Rezept)
        self.comboBox_position.setObjectName(u"comboBox_position")

        self.gridLayout.addWidget(self.comboBox_position, 2, 2, 1, 1)

        self.label_information = QLabel(Rezept)
        self.label_information.setObjectName(u"label_information")
        self.label_information.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_information, 8, 0, 1, 1)

        self.label_2 = QLabel(Rezept)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_3 = QLabel(Rezept)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(110, 16))
        self.label_3.setPixmap(QPixmap(u"../img/dj2.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 10, 2, 1, 1)


        self.retranslateUi(Rezept)

        QMetaObject.connectSlotsByName(Rezept)
    # setupUi

    def retranslateUi(self, Rezept):
        Rezept.setWindowTitle(QCoreApplication.translate("Rezept", u"Form", None))
        self.label_bereich.setText(QCoreApplication.translate("Rezept", u"Bereich", None))
        self.label_bemerkung.setText(QCoreApplication.translate("Rezept", u"Bemerkung", None))
        self.label_bezeichnung2.setText(QCoreApplication.translate("Rezept", u"Bezeichnung 2", None))
        self.label_Leistung.setText(QCoreApplication.translate("Rezept", u"Leistung", None))
        self.label.setText(QCoreApplication.translate("Rezept", u"Leistung Einf\u00fcgen", None))
        self.label_position.setText(QCoreApplication.translate("Rezept", u"Position", None))
        self.pushButton_anwenden.setText(QCoreApplication.translate("Rezept", u"Anwenden", None))
        self.pushButton_beenden.setText(QCoreApplication.translate("Rezept", u"Beenden", None))
        self.label_bezeichnung1.setText(QCoreApplication.translate("Rezept", u"Bezeichnung 1", None))
        self.label_information.setText(QCoreApplication.translate("Rezept", u"Information:", None))
        self.label_2.setText(QCoreApplication.translate("Rezept", u"Creator:", None))
        self.label_3.setText("")
    # retranslateUi

