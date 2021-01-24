import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog
from PyQt5.QtCore import pyqtSignal, QUrl
from OptionsWindow import Ui_OptionsWindow

from configparser import ConfigParser

import resources


class OptionsView(QMainWindow, Ui_OptionsWindow):
    reload = pyqtSignal()
    load = pyqtSignal()

    def __init__(self, *args, config=None, obj=None, **kwargs):
        super(OptionsView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.config = config
        self.load_config()
        self.setWindowTitle("Options")
        self.set_up_toolbar()
        self.signals()

    def set_up_toolbar(self):
        placeholder_icon = QtGui.QIcon(":/icons/assets/icon_placeholder.png")
        group = QtWidgets.QActionGroup(self)
        group.setExclusive(True)

        bLibrary = QAction(placeholder_icon, "Library", self, checkable=True)
        bLibrary.setStatusTip("Change the options regarding your library.")
        bLibrary.setObjectName("bLibrary")
        bLibrary.setChecked(True)
        bLibrary.triggered.connect(lambda s: self.show_widget(self.pgOptionsLibrary))

        bGeneral = QAction(placeholder_icon, "Copying", self, checkable=True)
        bGeneral.setStatusTip("Change general settings.")
        bLibrary.setObjectName("bGeneral")
        bGeneral.triggered.connect(lambda s: self.show_widget(self.pgOptionsCopying))

        group.addAction(bLibrary)
        self.tbOptions.addAction(bLibrary)

        group.addAction(bGeneral)
        self.tbOptions.addAction(bGeneral)

        self.stckOptionsPages.setCurrentIndex(0)

    def load_config(self):
        if not self.config.has_section("general"):
            self.config.add_section("general")

        if not self.config.has_section("library"):
            self.config.add_section("library")

        if self.config.has_option("general", "album_copy_type"):
            # print(self.config.get("general", "album_copy_type"))
            self.cbAlbumCopy.setCurrentText(self.config.get("general", "album_copy_type"))
        else:
            self.config.set("general", "album_copy_type", "Just copy the files")
            self.config.save()

        if self.config.has_option("general", "artist_copy_type"):
            # print(self.config.get("general", "artist_copy_type"))
            self.cbArtistCopy.setCurrentText(self.config.get("general", "artist_copy_type"))
        else:
            self.config.set("general", "artist_copy_type", "Just copy the files")
            self.config.save()

        if self.config.has_option("library", "path"):
            self.iLibraryXML.setText(self.config.get("library", "path"))

    def signals(self):
        self.bLibraryXML.clicked.connect(self.set_lib)
        self.iLibraryXML.textChanged.connect(self.set_lib_value)
        self.bReloadLibrary.clicked.connect(self.reload.emit)
        self.cbArtistCopy.currentTextChanged.connect(
            lambda x: self.set_option("general", "artist_copy_type", self.cbArtistCopy.currentText())
        )
        self.cbAlbumCopy.currentTextChanged.connect(
            lambda x: self.set_option("general", "album_copy_type", self.cbAlbumCopy.currentText())
        )

    def set_option(self, group, option, value):
        print(group, option, value)
        self.config.set(group, option, value)
        self.save_config()

    def set_lib(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select XML File")

        if file:
            print(type(file))
            print(file)
            if not self.config.has_section("library"):
                self.config.add_section("library")
                self.set_lib_value()

            self.iLibraryXML.setText(file)
            self.save_config()

    def set_lib_value(self):
        self.config.set("library", "path", self.iLibraryXML.text())
        self.save_config()

    def set_album_copy_type_value(self):
        self.config.set("general", "album_copy_type", self.cbAlbumCopy.currentText())
        print(self.config.get("general", "album_copy_type"))
        self.save_config()

    def set_artist_copy_type_value(self):
        self.config.set("general", "artist_copy_type", self.cbArtistCopy.currentText())
        print(self.config.get("general", "artist_copy_type"))
        self.save_config()

    def save_config(self):
        self.config.save()
        self.load.emit()

    def show_widget(self, widget):
        self.stckOptionsPages.setCurrentWidget(widget)

