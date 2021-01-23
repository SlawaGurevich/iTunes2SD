from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class AlbumModel(QtCore.QAbstractListModel):
    def __init__(self, library=None):
        super().__init__()
        self.library = library
        self._checked_rows = set()
        self.albums = self.library.get_albums() or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.albums[index.row()]

        if role == Qt.CheckStateRole:
            return Qt.Checked if index.row() in self._checked_rows else Qt.Unchecked

    def rowCount(self, index):
        return len(self.albums)

    def get_selected_albums(self):
        selected_album_names = [self.albums[x] for x in self._checked_rows]
        selected_albums = []
        for album_name in selected_album_names:
            selected_albums.append({
                "name": album_name,
                "items": list(filter(lambda x: x.getItunesAttribute("Album") == album_name, self.library.get_songs()))
            })

        return selected_albums

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
