import os
import shutil
from PyQt5.QtCore import QObject, QUrl


class FileHandler(QObject):
    def __init__(self, config=None):
        super().__init__()
        self.config = config

    def create_playlist_files(self, playlists):
        destination = self.config.get("main", "destination")
        playlist_format = self.config.get("main", "format")


        for playlist in playlists:
            url = os.path.join(destination, f'{playlist.title}.{playlist_format}')
            items = playlist.items

            with open(url, "w+") as file:
                #initial line for extended format
                file.write("#EXTM3U\n\n")

                print(f'Length: {len(items)}')

            for item in items:
                src = QUrl(item.itunesAttibutes["Location"]).toLocalFile()
                print(item.itunesAttibutes)

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

                    filepath = os.path.join(dest, QUrl(item.itunesAttibutes["Location"]).fileName())

                    if not os.path.exists(filepath):
                        shutil.copy(src, filepath)

                    length = int(int(item.itunesAttibutes['Total Time'])/1000)
                    localpath = dest.replace(destination, ".")
                    title = item.itunesAttibutes['Name'] if "Name" in item.itunesAttibutes else ""
                    artist = item.itunesAttibutes['Artist'] if "Artist" in item.itunesAttibutes else ""

                    # write metadata
                    with open(url, "a") as file:
                        file.write(f'#EXTINF; {length}, {artist} - {title}\n')

                    with open(url, "a") as file:
                        file.write(f'{localpath}/{QUrl(item.itunesAttibutes["Location"]).fileName()}\n\n')

                except OSError as e:
                    print(e)

                # print(item.itunesAttibutes)
                # print(QUrl(item.itunesAttibutes["Location"]).toLocalFile())

            print(dir(playlist))
            print(playlist)