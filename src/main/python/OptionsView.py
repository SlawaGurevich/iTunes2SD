import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog
from PyQt5.QtCore import pyqtSignal, QUrl
from OptionsWindow import Ui_OptionsWindow

from configparser import ConfigParser

import resources

class OptionsView(QMainWindow, Ui_OptionsWindow):
    reload = pyqtSignal(bool)
    config = ConfigParser()
    path_to_cfg = os.path.join(os.path.expanduser('~'), '.i2sd', 'conf.ini')

    def __init__(self, *args, obj=None, **kwargs):
        super(OptionsView, self).__init__(*args, **kwargs)
        self.config.read(self.path_to_cfg)
        self.setupUi(self)
        self.setWindowTitle("Options")
        self.set_up_toolbar()
        self.signals()
        self.load_config()

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
        if self.config.has_option("library", "path"):
            self.iLibraryXML.setText(self.config.get("library", "path"))

    def signals(self):
        self.bLibraryXML.clicked.connect(self.set_lib)
        self.iLibraryXML.textChanged.connect(self.save_config)

    def set_lib(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select XML File")

        if file:
            print(type(file))
            print(file)
            if not self.config.has_section("library"):
                self.config.add_section("library")

            self.iLibraryXML.setText(file)
            self.save_config()


    def save_config(self):
        self.config.set("library", "path", self.iLibraryXML.text())
        with open(self.path_to_cfg, 'w+') as f:
            self.config.write(f)
        self.reload.emit(True)

    def show_widget(self, widget):
        self.stckOptionsPages.setCurrentWidget(widget)

