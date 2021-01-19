from itunesLibrary import library
import pickle
import os
import errno


class Library:
    lib = {}
    xml_path = os.path.join(os.getenv("HOME"), "Music/iTunes/Library.xml")
    parsed_lib = None
    path_to_lib = os.path.join(os.path.expanduser('~'), '.i2sd', 'library.lib')

    def __init__(self, path_to_xml=None):
        self.config.read(self.path_to_cfg)

        self.check_for_xml()
        self.check_for_library()

    def get_library(self):
        return self.lib

    def get_playlists(self):
        return self.lib["playlists"]

    def get_songs(self):
        return self.lib["songs"]

    def get_albums(self):
        return self.lib["albums"]

    def get_artists(self):
        return self.lib["artists"]

    def reload_library(self, path=xml_path):
        self.parsed_lib = library.parse(path)
        self.save_library()

    def save_library(self):
        playlists = []
        songs = []

        for playlist in self.parsed_lib.playlists:
            playlists.append(playlist)

        for song in self.parsed_lib.items:
            songs.append(song)

        print(songs[0].itunesAttibutes)
        artists = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Artist")), songs))))
        albums = sorted(list(set(map(lambda x: str(x.getItunesAttribute("Album")), songs))))

        self.lib["playlists"] = playlists
        self.lib["songs"] = songs
        self.lib["artists"] = artists
        self.lib["albums"] = albums

        print(f'{len(self.lib)} new playlists generated.')

        with open(self.path_to_lib, 'wb+') as file:
            pickle.dump(self.lib, file)

    def load_library(self):
        with open(self.path_to_lib, 'rb') as file:
            self.lib = pickle.load(file)
        print(f'{len(self.lib)} playlists available.')

    def check_for_library(self):
        if os.path.exists(self.path_to_lib):
            self.load_library()
        else:
            try:
                os.makedirs(os.path.dirname(self.path_to_lib))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

            self.reload_library()



