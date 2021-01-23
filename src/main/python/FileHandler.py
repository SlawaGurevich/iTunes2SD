import os
import shutil
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
        self.destination = None
        self.playlist_format = None
        self.extended = False
        self.files_copied = 0
        self.all_item_count = 0

    @pyqtSlot()
    def run(self):
        print("worker")
        self.create_files(playlists=self.playlists, artists=self.artists, albums=self.albums, config=self.config)

    def create_file_from_song_item(self, item, url=None):
        src = QUrl(item.itunesAttibutes["Location"]).toLocalFile()
        # print(item.itunesAttibutes)

        # Check if compilation and place accordingly
        if "Compilation" in item.itunesAttibutes and bool(item.itunesAttibutes['Compilation']):
            dest = os.path.join(self.destination,
                                "Compilations",
                                item.itunesAttibutes['Album']
                                )
        else:
            dest = os.path.join(self.destination,
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

            length = int(int(item.itunesAttibutes['Total Time']) / 1000)
            localpath = dest.replace(self.destination, ".")
            title = item.itunesAttibutes['Name'] if "Name" in item.itunesAttibutes else ""
            artist = item.itunesAttibutes['Artist'] if "Artist" in item.itunesAttibutes else ""

            # write metadata
            if url:
                if self.extended:
                    with open(url, "a+") as file:
                        file.write(f'#EXTINF; {length}, {artist} - {title}\n')

                with open(url, "a+") as file:
                    file.write(f'{localpath}/{QUrl(item.itunesAttibutes["Location"]).fileName()}\n\n')

        except OSError as e:
            print(e)

        self.files_copied += 1
        self.signals.progress.emit(int(100 * self.files_copied / self.all_item_count), filename)
        # print(self.files_copied)

    def create_playlist_file(self, url):
        if self.extended:
            if not os.path.exists(url):
                with open(url, "w+") as file:
                    # initial line for extended format
                    file.write("#EXTM3U\n\n")

                # print(f'Length: {len(items)}')

    def create_files(self, playlists=[], artists=[], albums=[], config=None):
        self.destination = self.config.get("main", "destination")
        self.playlist_format = self.config.get("main", "format")
        self.extended = self.config.getboolean("main", "extended")

        self.files_copied = 0

        if playlists or artists or albums:
            self.all_item_count = 0

            if playlists:
                for playlist in playlists:
                    self.all_item_count += len(playlist.items)

            if albums:
                for album in albums:
                    self.all_item_count += len(album["items"])

            if artists:
                for artist in artists:
                    self.all_item_count += len(artist["items"])

            # print(self.all_item_count)

        if playlists:
            for playlist in playlists:
                url = os.path.join(self.destination, f'{playlist.title}.{self.playlist_format}')
                self.create_playlist_file(url)

                items = playlist.items
                for item in items:
                    self.create_file_from_song_item(item, url)

        if albums:
            print(self.config.get("general", "album_copy_type"))
            album_copy_type = self.config.get("general", "album_copy_type")

            for i, album in enumerate(albums):
                url = None

                if album_copy_type != "Just copy the files":
                    if album_copy_type == "Create a playlist with all albums":
                        url = os.path.join(self.destination, f'Albums.{self.playlist_format}')
                        if i == 0 and os.path.exists(url):
                            os.remove(url)
                    elif album_copy_type == "Create a playlist for each album":
                        url = os.path.join(self.destination, f'{album["name"]}.{self.playlist_format}')
                    self.create_playlist_file(url)

                for item in album["items"]:
                    # print(item.getItunesAttribute("Location"))
                    self.create_file_from_song_item(item, url)

        if artists:
            print(self.config.get("general", "artist_copy_type"))
            artist_copy_type = self.config.get("general", "artist_copy_type")

            for i, artist in enumerate(artists):
                url = None

                if artist_copy_type != "Just copy the files":
                    if artist_copy_type == "Create a playlist with all artists":
                        url = os.path.join(self.destination, f'Artists.{self.playlist_format}')
                        if i == 0 and os.path.exists(url):
                            os.remove(url)
                    elif artist_copy_type == "Create a playlist for each artist":
                        url = os.path.join(self.destination, f'{artist["name"]}.{self.playlist_format}')
                    self.create_playlist_file(url)

                for item in artist["items"]:
                    self.create_file_from_song_item(item, url)

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

    def create_files(self, playlists=[], artists=[], albums=[]):
        worker = Worker(playlists=playlists, artists=artists, albums=albums, config=self.config)
        worker.signals.progress.connect(self.emit_progress)
        worker.signals.finished.connect(self.emit_finished)
        self.thread_pool.start(worker)

    def emit_finished(self):
        self.finished.emit()

    def emit_progress(self, progress, file):
        self.progress.emit(progress, file)
        # print(f'{progress}, {file}')


