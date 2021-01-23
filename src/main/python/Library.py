from itunesLibrary import library
from PyQt5.QtCore import QRunnable, QObject, QThreadPool, pyqtSlot, pyqtSignal
import pickle
import os
import errno


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(library.Library)


class Worker(QRunnable):
    def __init__(self, xml):
        super().__init__()
        self.signals = WorkerSignals()
        self.xml = xml

    @pyqtSlot()
    def run(self):
        try:
            lib = library.parse(self.xml)
        except Exception as e:
            self.signals.error.emit(str(e))
        else:
            self.signals.finished.emit()
            self.signals.result.emit(lib)


class Library(QObject):
    lib = {}
    thread_pool = QThreadPool()
    xml_path = os.path.join(os.getenv("HOME"), "Music/iTunes/Library.xml")
    parsed_lib = None
    path_to_lib = os.path.join(os.path.expanduser('~'), '.i2sd', 'library.lib')
    loaded = pyqtSignal()

    def __init__(self, path_to_xml=xml_path):
        # print("lib init")
        # print(path_to_xml)
        super().__init__()
        self.check_for_library()

    def get_library(self):
        # print("Get library")
        return self.lib

    def get_playlists(self):
        # print("Get playlists")
        if len(self.lib):
            return self.lib["playlists"]
        return False

    def get_songs(self):
        return self.lib["songs"]

    def get_albums(self):
        return self.lib["albums"]

    def get_artists(self):
        return self.lib["artists"]

    def rescan_library(self, path=xml_path):
        worker = Worker(path)
        worker.signals.result.connect(self.set_lib)
        self.thread_pool.start(worker)

    def set_lib(self, lib):
        self.parsed_lib = lib
        self.save_library()

    def check_for_library(self):
        if os.path.exists(self.path_to_lib):
            print("Path to Lib exists.")
            self.load_library()
        else:
            try:
                os.makedirs(os.path.dirname(os.path.dirname(self.path_to_lib)))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

            self.rescan_library()

    def save_library(self):
        playlists = []
        songs = []

        for playlist in self.parsed_lib.playlists:
            playlists.append(playlist)

        for song in self.parsed_lib.items:
            songs.append(song)

        artists = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Artist")), songs))))
        albums = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Album")), songs))))

        self.lib["playlists"] = playlists
        self.lib["songs"] = songs
        self.lib["artists"] = artists
        self.lib["albums"] = albums

        # print(f'{len(self.lib)} new playlists generated.')

        with open(self.path_to_lib, 'wb+') as file:
            pickle.dump(self.lib, file)

        self.loaded.emit()

    def load_library(self):
        with open(self.path_to_lib, 'rb') as file:
            self.lib = pickle.load(file)
        file.close()
        # print(f'{len(self.lib)} items available. {len(self.lib["songs"])}')



        print("Lib Loaded emitted.")




