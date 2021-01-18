from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class ArtistModel(QtCore.QAbstractListModel):
    def __init__(self, artists=None):
        super().__init__()
        self._checked_rows = set()
        self.artists = artists or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.artists[index.row()]

        if role == Qt.CheckStateRole:
            return Qt.Checked if index.row() in self._checked_rows else Qt.Unchecked

    def rowCount(self, index):
        return len(self.artists)

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            if value == Qt.Checked:
                self._checked_rows.add(index.row())
            else:
                self._checked_rows.discard(index.row())
            return True
        return QtCore.QAbstractListModel.setData(self, index, value, role)

    def flags(self, index):
        return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled