from PySide6 import QtCore


class TableModel(QtCore.QAbstractListModel):

    def __init__(self, data=[], parent=None):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        pass

    def rowCount(self, index):
        pass

    def columnCount(self, index):
        pass