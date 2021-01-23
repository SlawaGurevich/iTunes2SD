from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from configparser import ConfigParser
from LoadingMessageBox import LoadingMessageBox
from DialogLoading import DialogLoading

import sys
import os

from Library import Library

from MainWindow import Ui_MainWindow
from OptionsView import OptionsView
from PlaylistModel import PlaylistModel
from ArtistModel import ArtistModel
from AlbumModel import AlbumModel
from FileHandler import FileHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    config = ConfigParser()
    library = None
    playlist_model = None
    artist_model = None
    album_model = None

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.options = OptionsView()
        self.path_to_cfg = os.path.join(os.path.expanduser('~'), '.i2sd', 'conf.ini')
        self.config.read(self.path_to_cfg)
        self.file_handler = FileHandler(self.config)
        self.setupUi(self)
        self.load_config()
        self.loading_message = DialogLoading()

        self.set_UI()
        self.set_signals()

        self.check_sync()

        self.check_lib()

    def set_UI(self):
        self.cmbFormat.setCurrentIndex(0)
        self.cpProgress.setValue(0)

    def set_signals(self):
        self.bSync.clicked.connect(self.sync)
        self.bDestination.clicked.connect(self.select_dir)
        self.cbExtended.stateChanged.connect(self.save_config)
        self.cbOnlyPlaylist.stateChanged.connect(self.save_config)
        self.cmbFormat.currentIndexChanged.connect(self.save_config)
        self.bMoreOptions.clicked.connect(lambda x: self.options.setVisible(not self.options.isVisible()))
        self.options.reload.connect(self.check_lib)
        self.iDestination.textChanged.connect(self.check_sync)
        self.file_handler.progress.connect(lambda progress, file: self.cpProgress.setValue(progress))
        self.file_handler.finished.connect(lambda: self.bSync.setEnabled(True))

    def check_lib(self):
        print("check")
        if self.config.has_option("library", "path") and self.config.get("library", "path") != "":
            if os.path.isfile(self.config.get("library", "path")):
                self.library = Library(path_to_xml=self.config.get("library", "path"))
                if self.library.get_playlists():
                    self.set_up_lib()
                    self.show()
                else:
                    self.loading_message.show()
                    self.library.loaded.connect(self.set_up_lib)

                self.lNoLib.setVisible(False)
                return
            self.lNoLib.setText("XML File not valid.")
            self.lNoLib.setVisible(True)
            return
        self.lNoLib.setText("No library defined. Please provide XML file.")
        self.lNoLib.setVisible(True)

    def set_up_lib(self):
        print("Library set up")
        self.playlist_model = PlaylistModel(playlists=self.library.get_playlists())
        self.artist_model = ArtistModel(library=self.library)
        self.album_model = AlbumModel(library=self.library)

        self.lPlaylistCount.setText(f'{len(self.library.get_playlists())}')
        self.lArtistCount.setText(f'{len(self.library.get_artists())}')
        self.lAlbumCount.setText(f'{len(self.library.get_albums())}')

        self.vPlaylists.setModel(self.playlist_model)
        self.vArtists.setModel(self.artist_model)
        self.vAlbums.setModel(self.album_model)

        self.loading_message.done()
        self.show()

    def load_config(self):
        if not os.path.exists(self.path_to_cfg):
            try:
                os.makedirs(os.path.dirname(self.path_to_cfg))
                open(self.path_to_cfg, "w+").close()
            except OSError:
                print("Creation of the directory %s failed" % self.path_to_cfg)

        self.config.read(self.path_to_cfg)

        if not self.config.has_section("main"):
            self.config.add_section("main")

        self.cbExtended.setChecked(self.config.getboolean("main", "extended", fallback=False))
        self.cbOnlyPlaylist.setChecked(self.config.getboolean("main", "plonly", fallback=False))
        self.cmbFormat.setCurrentText(self.config.get("main", "format", fallback="m3u"))
        if self.config.has_option("main", "destination"):
            self.iDestination.setText(self.config.get("main", "destination"))

    def save_config(self):
        if not self.config.has_section("main"):
            self.config.add_section("main")

        self.config.set("main", "extended", str(self.cbExtended.isChecked()))
        self.config.set("main", "plonly", str(self.cbOnlyPlaylist.isChecked()))
        self.config.set("main", "format", self.cmbFormat.currentText())
        self.config.set("main", "destination", self.iDestination.text())

        with open(self.path_to_cfg, 'w+') as f:
            self.config.write(f)

    def select_dir(self):
        destination = str(QFileDialog.getExistingDirectory(self, "Select Target Directory"))
        if destination:
            self.iDestination.setText(destination)
            self.save_config()

    def check_sync(self):
        condition = self.iDestination.text() != ""
        self.bSync.setEnabled(condition)

    def sync(self):
        self.cpProgress.setValue(0)
        self.bSync.setEnabled(False)
        playlists = self.playlist_model.get_selected_playlists()
        artists = self.artist_model.get_selected_artists()
        albums = self.album_model.get_selected_albums()
        self.file_handler.create_files(playlists=playlists, artists=artists, albums=albums, config=self.config)


class AppContext(ApplicationContext):
    def run(self):
        window = MainWindow()
        version = self.build_settings["version"]
        window.setWindowTitle(f'iTunes2SD ({ version })')
        window.show()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)