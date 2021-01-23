from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class ArtistModel(QtCore.QAbstractListModel):
    def __init__(self, library=[]):
        super().__init__()
        self.library = library
        self._checked_rows = set()
        self.artists = library.get_artists() or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.artists[index.row()]

        if role == Qt.CheckStateRole:
            return Qt.Checked if index.row() in self._checked_rows else Qt.Unchecked

    def rowCount(self, index):
        return len(self.artists)

    def get_selected_artists(self):
        selected_artist_names = [self.artists[x] for x in self._checked_rows]
        selected_artists = []
        for artist_name in selected_artist_names:
            selected_artists.append({
                "name": artist_name,
                "items": list(filter(lambda x: x.getItunesAttribute("Artist") == artist_name, self.library.get_songs()))
            })

        return selected_artists

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