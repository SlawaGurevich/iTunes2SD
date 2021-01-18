from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys
from Library import Library

from MainWindow import Ui_MainWindow
from OptionsView import OptionsView
from PlaylistModel import PlaylistModel
from ArtistModel import ArtistModel
from AlbumModel import AlbumModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("iTunes2SD")

        self.set_UI()
        self.set_signals()

        self.library = Library()
        self.playlist_model = PlaylistModel(playlists=self.library.get_playlists())
        self.artist_model = ArtistModel(artists=self.library.get_artists())
        self.album_model = AlbumModel(albums=self.library.get_albums())

        self.vPlaylists.setModel(self.playlist_model)
        self.vArtists.setModel(self.artist_model)
        self.vAlbums.setModel(self.album_model)

    def set_UI(self):
        self.cmbFormat.setCurrentIndex(0)

    def set_signals(self):
        self.bSync.clicked.connect(self.list_checked)

    def list_checked(self):
        print(list(self.playlist_model._checked_rows))
        saved_lists = self.library.get_playlists()
        playlists = sorted([saved_lists[x].title for x in self.playlist_model._checked_rows])
        print(playlists)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(250, 150)
    window.show()

    options = OptionsView()
    options.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)