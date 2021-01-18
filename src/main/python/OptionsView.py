from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QStyle
from OptionsWindow import Ui_OptionsWindow

import resources

class OptionsView(QMainWindow, Ui_OptionsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(OptionsView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Options")
        self.set_up_toolbar()

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



    def show_widget(self, widget):
        self.stckOptionsPages.setCurrentWidget(widget)

