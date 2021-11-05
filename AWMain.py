import sys
from datetime import date

from PyQt5 import QtWidgets

from model.TableModel import TableModel
from moduls.ClearingRate import AW
from moduls.CreateCsv import CreateExcel
from RezeptView import RezeptWindow
from windows.MainWindow_qt5 import Ui_AWTool


class MainWindow(QtWidgets.QMainWindow, Ui_AWTool):

    __version = "1.2"

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.rezept_window = RezeptWindow(self.tableWidget)
        self.model = TableModel(self.tableWidget)
        self.aw = AW()
        self.label_faktor.setText("0.0")
        self.label_sum.setText("0.00")
        self.label_version.setText(self.__version)
        self.pushButton_hinzufgen.clicked.connect(self.push_hinzufuegen)
        self.pushButton_loeschen.clicked.connect(self.push_loeschen)
        self.pushButton_erstellen.clicked.connect(self.push_erstellen)
        self.pushButton_beenden.clicked.connect(self.push_beenden)
        self.tableWidget.itemChanged.connect(self.changed_table_data)

    def show_popup_info(self, string):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(string)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec()

    def changed_table_data(self, item):
        col = item.column()
        row = item.row()
        last_row = self.tableWidget.columnCount() - 1
        if col == last_row:
            men, price = self.model.sum_last_row(last_row)
            self.aw.increase = men
            self.label_faktor.setText(str(self.aw.increase))
            self.label_sum.setText("%.2f" % (self.aw.increase * price))
        if col == self.tableWidget.columnCount() - 2:
            faktor = float(self.tableWidget.item(row, col - 1).text())
            base_price = float(self.tableWidget.item(row, col - 2).text())
            prozent = float(self.tableWidget.item(row, col).text()) / 100.0
            price = faktor * base_price * prozent
            price = round(price, 2)
            self.model.setItemLastColumn(row, price)
            men, price = self.model.sum_last_row(col)
            self.aw.increase = men
            self.label_faktor.setText(str(self.aw.increase))
            self.label_sum.setText("%.2f" % (self.aw.increase * price))
        if col == self.tableWidget.columnCount() - 9:
            if self.tableWidget.item(row, col).text().upper() == "X":
                leistung = str(self.tableWidget.item(row, col + 4).text())
                faktor = float(self.tableWidget.item(row, col + 6).text())
                base_price = float(self.tableWidget.item(row, col + 5).text())
                zusatz_faktor = self.aw.weitere_position("Trennung", leistung)
                result = faktor + float(zusatz_faktor)
                prozent = float(self.tableWidget.item(row, col + 7).text()) / 100.0
                price = result * base_price * prozent
                price = round(price, 2)
                self.model.setItemLastColumn(row, price)
                self.model.setItemFaktorColumn(row, str(result))
                men, price = self.model.sum_last_row(col)
                self.aw.increase = men
                self.label_faktor.setText(str(self.aw.increase))
                self.label_sum.setText("%.2f" % (self.aw.increase * price))
        if col == self.tableWidget.columnCount() - 8:
            if self.tableWidget.item(row, col).text().upper() == "X":
                leistung = str(self.tableWidget.item(row, col + 3).text())
                faktor = float(self.tableWidget.item(row, col + 5).text())
                base_price = float(self.tableWidget.item(row, col + 4).text())
                zusatz_faktor = self.aw.weitere_position("Hilfsenergie", leistung)
                result = faktor + float(zusatz_faktor)
                prozent = float(self.tableWidget.item(row, col + 6).text()) / 100.0
                price = result * base_price * prozent
                price = round(price, 2)
                self.model.setItemLastColumn(row, price)
                self.model.setItemFaktorColumn(row, str(result))
                men, price = self.model.sum_last_row(col)
                self.aw.increase = men
                self.label_faktor.setText(str(self.aw.increase))
                self.label_sum.setText("%.2f" % (self.aw.increase * price))
        if col == self.tableWidget.columnCount() - 7:
            if self.tableWidget.item(row, col).text().upper() == "X":
                leistung = str(self.tableWidget.item(row, col + 2).text())
                faktor = float(self.tableWidget.item(row, col + 4).text())
                base_price = float(self.tableWidget.item(row, col + 3).text())
                zusatz_faktor = self.aw.weitere_position("Klemmpare", leistung)
                result = faktor + float(zusatz_faktor)
                prozent = float(self.tableWidget.item(row, col + 5).text()) / 100.0
                price = result * base_price * prozent
                price = round(price, 2)
                self.model.setItemLastColumn(row, price)
                self.model.setItemFaktorColumn(row, str(result))
                men, price = self.model.sum_last_row(col)
                self.aw.increase = men
                self.label_faktor.setText(str(self.aw.increase))
                self.label_sum.setText("%.2f" % (self.aw.increase * price))
        if col == self.tableWidget.columnCount() - 6:
            if self.tableWidget.item(row, col).text().upper() == "X":
                leistung = str(self.tableWidget.item(row, col + 1).text())
                faktor = float(self.tableWidget.item(row, col + 3).text())
                base_price = float(self.tableWidget.item(row, col + 2).text())
                zusatz_faktor = self.aw.weitere_position("Konfigurationsliste", leistung)
                result = faktor + float(zusatz_faktor)
                prozent = float(self.tableWidget.item(row, col + 4).text()) / 100.0
                price = result * base_price * prozent
                price = round(price, 2)
                self.model.setItemLastColumn(row, price)
                self.model.setItemFaktorColumn(row, str(result))
                men, price = self.model.sum_last_row(col)
                self.aw.increase = men
                self.label_faktor.setText(str(self.aw.increase))
                self.label_sum.setText("%.2f" % (self.aw.increase * price))

    def push_hinzufuegen(self, checked):
        self.rezept_window.show()

    def push_loeschen(self, checked):
        self.model.delete_row()
        col = self.model.last_colmn()
        men, price = self.model.sum_last_row(col - 1)
        self.aw.increase = men
        self.label_faktor.setText(str(self.aw.increase))
        self.label_sum.setText("%.2f" % (self.aw.increase * price))

    def push_erstellen(self, checked):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        try:
            Daydate = date.today()
            txt_geber = self.label_Auftraggeber.text()
            geber = self.lineEdit_Auftraggeber.text()
            txt_intern = self.label_intern.text()
            intern = self.lineEdit_intern.text()
            txt_extern = self.label_Extern.text()
            extern = self.lineEdit_Extern.text()
            txt_bearb = self.label_bearbeiter.text()
            bearb = self.lineEdit_bearbeiter.text()
            data = self.model.get_all_items()
            self.create = CreateExcel(folder, extern)
            self.create.file_properties(bearb)
            self.create.writeString(1, [["Datum: ", Daydate.strftime("%d.%m.%Y")]])
            self.create.writeString(
                1,
                [
                    [txt_geber, geber, "", "", "ECM Ingenieur-Unternehmen GmbH"],
                    [txt_intern, intern, "", "", "Abt. KIENK"], [txt_extern, extern, "", "", "Lessingstraße 15"],
                    [txt_bearb, bearb, "", "", "46149 Oberhausen"]
                    ],
                )
            header = self.model.get_header()
            self.create.writeString(0, [header])
            self.create.get_width([header])
            self.create.writeString(0, data)
            self.create.get_width(data)
            end_off_data = [
                ["Mehrung von: ",
                 self.label_faktor.text(),
                 "Gesammtbetrag: %.2f €" % (float(self.label_sum.text()))]
                ]
            self.create.writeString(len(header) - 3, end_off_data)
            self.create.get_width(end_off_data)
            self.create.set_width()
            self.create.close()
            self.show_popup_info("Bericht wurde Erfolgreicht Erstellt!")
        except AttributeError:
            pass

    def push_beenden(self, checked):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()
