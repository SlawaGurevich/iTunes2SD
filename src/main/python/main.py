from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore
from ConfigHandler import ConfigHandler
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
    config = None
    library = None
    playlist_model = None
    artist_model = None
    album_model = None
    path_to_cfg = os.path.join(os.path.expanduser('~'), '.i2sd', 'conf.ini')
    config = ConfigHandler(path_to_cfg)

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.load_config()

        self.file_handler = FileHandler(config=self.config)
        self.options = OptionsView(config=self.config)
        self.loading_message = DialogLoading()

        self.set_ui()
        self.set_signals()

        self.check_lib()

    def set_ui(self):
        self.cmbFormat.setCurrentIndex(0)
        self.cpProgress.setValue(0)
        self.check_sync()


    def set_signals(self):
        self.bSync.clicked.connect(self.sync)
        self.bDestination.clicked.connect(self.select_dir)
        self.cbExtended.stateChanged.connect(self.save_config)
        self.cbOnlyPlaylist.stateChanged.connect(self.save_config)
        self.cmbFormat.currentIndexChanged.connect(self.save_config)
        self.bMoreOptions.clicked.connect(lambda x: self.options.setVisible(not self.options.isVisible()))
        self.options.load.connect(self.check_lib)
        self.options.reload.connect(self.reload_library)
        self.iDestination.textChanged.connect(self.check_sync)
        self.file_handler.progress.connect(lambda progress, file: self.cpProgress.setValue(progress))
        self.file_handler.finished.connect(lambda: self.bSync.setEnabled(True))

    def reload_library(self):
        print("Main.py: reload_library")
        self.loading_message.show()
        self.library.reload_library()

    def check_lib(self):
        print("check")

        if self.config.has_option("library", "path") and self.config.get("library", "path") != "":

            if os.path.isfile(self.config.get("library", "path")):
                self.loading_message.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.loading_message.show()
                self.library = Library(path_to_xml=self.config.get("library", "path"))
                self.library.loaded.connect(self.set_up_lib)
                self.library.check_for_library()
                self.lNoLib.setVisible(False)

                return
            self.lNoLib.setText("XML File not valid.")
            self.lNoLib.setVisible(True)
            return

        self.lNoLib.setText("No library defined. Please provide XML file.")
        self.lNoLib.setVisible(True)

    def set_up_lib(self):
        print("Library set up")
        self.playlist_model = PlaylistModel(library=self.library)
        self.artist_model = ArtistModel(library=self.library)
        self.album_model = AlbumModel(library=self.library)

        self.lPlaylistCount.setText(f'{len(self.library.get_playlists())}')
        self.lArtistCount.setText(f'{len(self.library.get_artists())}')
        self.lAlbumCount.setText(f'{len(self.library.get_albums())}')

        self.vPlaylists.setModel(self.playlist_model)
        self.vArtists.setModel(self.artist_model)
        self.vAlbums.setModel(self.album_model)

        self.loading_message.close()
        self.show()

    def load_config(self):
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

        self.config.save()

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
        self.file_handler.create_files(playlists=playlists, artists=artists, albums=albums)


class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        window = MainWindow()
        version = self.build_settings["version"]
        window.setWindowTitle(f'iTunes2SD ({ version })')
        return window

if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)