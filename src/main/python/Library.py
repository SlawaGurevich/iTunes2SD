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
    loaded = pyqtSignal()
    thread_pool = QThreadPool()

    lib = {}
    parsed_lib = None

    xml_path = os.path.join(os.getenv("HOME"), "Music/iTunes/Library.xml")
    path_to_lib = os.path.join(os.path.expanduser('~'), '.i2sd', 'library.lib')

    def __init__(self, path_to_xml=xml_path):
        # print("lib init")
        # print(path_to_xml)
        super().__init__()
        self.path_to_xml = path_to_xml

    def check_for_library(self, replace=False):
        if os.path.exists(self.path_to_lib) and replace is False:
            print("Lib exists.")
            self.load_library()
        else:
            try:
                os.makedirs(os.path.dirname(os.path.dirname(self.path_to_lib)))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

            self.scan_library()

    def load_library(self):
        with open(self.path_to_lib, 'rb') as file:
            self.lib = pickle.load(file)
            self.loaded.emit()
        file.close()
        # print(f'{len(self.lib)} items available. {len(self.lib["songs"])}')

    def scan_library(self, path=xml_path):
        worker = Worker(path)
        worker.signals.result.connect(self.save_library)
        self.thread_pool.start(worker)


    def save_library(self, lib):
        self.parsed_lib = lib

        playlists = []
        songs = []

        for playlist in self.parsed_lib.playlists:
            playlists.append(playlist)

        for song in self.parsed_lib.items:
            songs.append(song)

        artists = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Artist")), songs))))
        albums = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Album")), songs))))

        self.lib["playlists"] = playlists  # [obj]
        self.lib["songs"] = songs  # [obj]
        self.lib["artists"] = artists  # [str]
        self.lib["albums"] = albums  # [str]

        # print(f'{len(self.lib)} new playlists generated.')

        with open(self.path_to_lib, 'wb') as file:
            pickle.dump(self.lib, file)

        self.loaded.emit()

    # helper #

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

    def reload_library(self):
        self.check_for_library(replace=True)




