from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore


class TableModel:

    def __init__(self, tableWidget):
        self.table = tableWidget

    def header(self, header_data):
        self.table.setRowCount(0)
        self.table.setColumnCount(len(header_data))
        self.table.setHorizontalHeaderLabels(header_data)

    def get_header(self):
        colmns = self.table.columnCount()
        return [self.table.horizontalHeaderItem(colmn).text() for colmn in range(colmns)]

    def data(self, new_data):
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        for colmn, cell in enumerate(new_data):
            if cell == "---":
                self.table.setItem(row, colmn, QTableWidgetItem(""))
                continue
            self.table.setItem(row, colmn, QTableWidgetItem(cell))

    def sum_last_row(self, colmn):
        colmn = self.table.columnCount() - 1
        last_row = self.table.rowCount()
        price = 0.0
        men = 0
        for row in range(0, last_row):
            price = price + float(self.table.item(row, colmn).text())
            men += 1
        return men, price

    def get_all_items(self):
        f_colmn = []
        f_row = []
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                inhalt = self.table.item(row, column)
                f_colmn.append(str(inhalt.text()))
            f_row.append(f_colmn)
            f_colmn = []
        return f_row

    def delete_row(self):
        index_list = []
        for model_index in self.table.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)

        for index in index_list:
            self.table.removeRow(index.row())

    def last_row(self):
        return self.table.rowCount()

    def last_colmn(self):
        return self.table.columnCount()

    def setItemLastColumn(self, row, item):
        colmn = self.table.columnCount() - 1
        self.table.setItem(row, colmn, QTableWidgetItem(str(item)))

    def setItemFaktorColumn(self, row, item):
        colmn = self.table.columnCount() - 3
        self.table.setItem(row, colmn, QTableWidgetItem(str(item)))