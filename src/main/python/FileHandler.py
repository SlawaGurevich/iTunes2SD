import os
import shutil
import functools
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QRunnable, QThreadPool
from PyQt5.QtCore import QObject, QUrl


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    progress = pyqtSignal(int, str)


class Worker(QRunnable):
    def __init__(self, playlists=[], artists=[], albums=[], config=None):
        super().__init__()
        self.signals = WorkerSignals()
        self.playlists = playlists
        self.artists = artists
        self.albums = albums
        self.config = config

    @pyqtSlot()
    def run(self):
        print("worker")
        self.create_files(playlists=self.playlists, artists=self.artists, albums=self.albums, config=self.config)

    def create_files(self, playlists=[], artists=[], albums=[], config=None):
        destination = self.config.get("main", "destination")
        playlist_format = self.config.get("main", "format")
        extended = self.config.getboolean("main", "extended")
        files_copied = 0

        if playlists or artists or albums:
            all_item_count = 0

            if playlists:
                for playlist in playlists:
                    all_item_count += len(playlist.items)

            if albums:
                for album in albums:
                    all_item_count += len(album["items"])

            if artists:
                for artist in artists:
                    all_item_count += len(artist["items"])

            print(all_item_count)

        if playlists:
            for playlist in playlists:
                url = os.path.join(destination, f'{playlist.title}.{playlist_format}')
                items = playlist.items

                if extended:
                    with open(url, "w+") as file:
                        #initial line for extended format
                        file.write("#EXTM3U\n\n")

                        # print(f'Length: {len(items)}')

                for item in items:
                    src = QUrl(item.itunesAttibutes["Location"]).toLocalFile()
                    # print(item.itunesAttibutes)

                    # Check if compilation and place accordingly
                    if "Compilation" in item.itunesAttibutes and bool(item.itunesAttibutes['Compilation']):
                        dest = os.path.join(destination,
                                            "Compilations",
                                            item.itunesAttibutes['Album']
                                            )
                    else:
                        dest = os.path.join(destination,
                                            item.itunesAttibutes['Artist'],
                                            item.itunesAttibutes['Album']
                                        )

                    try:
                        if not os.path.exists(dest):
                            os.makedirs(dest)

                        filename = QUrl(item.itunesAttibutes["Location"]).fileName()
                        filepath = os.path.join(dest, filename)

                        if not os.path.exists(filepath):
                            shutil.copy(src, filepath)

                        length = int(int(item.itunesAttibutes['Total Time'])/1000)
                        localpath = dest.replace(destination, ".")
                        title = item.itunesAttibutes['Name'] if "Name" in item.itunesAttibutes else ""
                        artist = item.itunesAttibutes['Artist'] if "Artist" in item.itunesAttibutes else ""

                        # write metadata
                        if extended:
                            with open(url, "a") as file:
                                file.write(f'#EXTINF; {length}, {artist} - {title}\n')

                        with open(url, "a") as file:
                            file.write(f'{localpath}/{QUrl(item.itunesAttibutes["Location"]).fileName()}\n\n')

                    except OSError as e:
                        print(e)

                    files_copied += 1
                    self.signals.progress.emit(int(100 * files_copied / all_item_count), filename)
                    print(files_copied)

        self.signals.finished.emit()

                    # print(item.itunesAttibutes)
                    # print(QUrl(item.itunesAttibutes["Location"]).toLocalFile())

                # print(dir(playlist))
                # print(playlist)

class FileHandler(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int, str)

    def __init__(self, config=None):
        super().__init__()
        self.config = config
        self.thread_pool = QThreadPool()

    def create_files(self, playlists=[], artists=[], albums=[], config=None):
        worker = Worker(playlists=playlists, artists=artists, albums=albums, config=config)
        worker.signals.progress.connect(self.emit_progress)
        worker.signals.finished.connect(self.emit_finished)
        self.thread_pool.start(worker)

    def emit_finished(self):
        self.finished.emit()

    def emit_progress(self, progress, file):
        self.progress.emit(progress, file)
        print(f'{progress}, {file}')


