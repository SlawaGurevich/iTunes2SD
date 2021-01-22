# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 887)
        MainWindow.setMinimumSize(QtCore.QSize(930, 850))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: transparent;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QListView {\n"
"    border: 2px solid #3e3e3e;\n"
"    border-radius: 4;\n"
"}\n"
"\n"
".QListView::item {\n"
"    margin: 4px 10px;\n"
"    left: 4px;\n"
"}\n"
"\n"
".QListView:alternate {\n"
"    background-color: rgba(255,255,255,.2);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vPlaylists = QtWidgets.QListView(self.widget)
        self.vPlaylists.setMinimumSize(QtCore.QSize(400, 0))
        self.vPlaylists.setObjectName("vPlaylists")
        self.gridLayout_3.addWidget(self.vPlaylists, 1, 0, 1, 1)
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lPlaylists = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lPlaylists.setFont(font)
        self.lPlaylists.setObjectName("lPlaylists")
        self.horizontalLayout_6.addWidget(self.lPlaylists)
        self.lPlaylistCount = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lPlaylistCount.setFont(font)
        self.lPlaylistCount.setStyleSheet("#lPlaylistCount {\n"
"    color: #666;\n"
"}")
        self.lPlaylistCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lPlaylistCount.setObjectName("lPlaylistCount")
        self.horizontalLayout_6.addWidget(self.lPlaylistCount)
        self.gridLayout_3.addWidget(self.widget_12, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.vArtists = QtWidgets.QListView(self.widget_2)
        self.vArtists.setMinimumSize(QtCore.QSize(400, 0))
        self.vArtists.setObjectName("vArtists")
        self.gridLayout_4.addWidget(self.vArtists, 1, 0, 1, 1)
        self.widget_13 = QtWidgets.QWidget(self.widget_2)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lArtists = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lArtists.setFont(font)
        self.lArtists.setObjectName("lArtists")
        self.horizontalLayout_7.addWidget(self.lArtists)
        self.lArtistCount = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lArtistCount.setFont(font)
        self.lArtistCount.setStyleSheet("#lArtistCount {\n"
"    color: #666;\n"
"}")
        self.lArtistCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lArtistCount.setObjectName("lArtistCount")
        self.horizontalLayout_7.addWidget(self.lArtistCount)
        self.gridLayout_4.addWidget(self.widget_13, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lAlbums = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lAlbums.setFont(font)
        self.lAlbums.setObjectName("lAlbums")
        self.horizontalLayout_5.addWidget(self.lAlbums)
        self.lAlbumCount = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lAlbumCount.setFont(font)
        self.lAlbumCount.setStyleSheet("#lAlbumCount {\n"
"    color: #666\n"
"}")
        self.lAlbumCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lAlbumCount.setObjectName("lAlbumCount")
        self.horizontalLayout_5.addWidget(self.lAlbumCount)
        self.gridLayout_5.addWidget(self.widget_6, 0, 0, 1, 1)
        self.vAlbums = QtWidgets.QListView(self.widget_3)
        self.vAlbums.setMinimumSize(QtCore.QSize(400, 0))
        self.vAlbums.setStyleSheet("")
        self.vAlbums.setObjectName("vAlbums")
        self.gridLayout_5.addWidget(self.vAlbums, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lOptions = QtWidgets.QLabel(self.widget_4)
        self.lOptions.setMinimumSize(QtCore.QSize(0, 29))
        self.lOptions.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lOptions.setFont(font)
        self.lOptions.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lOptions.setObjectName("lOptions")
        self.gridLayout_6.addWidget(self.lOptions, 0, 0, 1, 1)
        self.grOptions = QtWidgets.QWidget(self.widget_4)
        self.grOptions.setStyleSheet("")
        self.grOptions.setObjectName("grOptions")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grOptions)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_8 = QtWidgets.QWidget(self.grOptions)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbExtended = QtWidgets.QCheckBox(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbExtended.setFont(font)
        self.cbExtended.setStyleSheet("QCheckBox {\n"
"    padding: 10 0;\n"
"    border-radius: 8;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width : 16;\n"
"    height: 16;\n"
"    border: 1px solid white;\n"
"    border-radius: 4;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #FF3C6A;\n"
"    border-color: #FF3C6A;\n"
"}")
        self.cbExtended.setChecked(False)
        self.cbExtended.setObjectName("cbExtended")
        self.verticalLayout_2.addWidget(self.cbExtended)
        self.verticalLayout.addWidget(self.widget_8)
        self.widget_10 = QtWidgets.QWidget(self.grOptions)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbOnlyPlaylist = QtWidgets.QCheckBox(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbOnlyPlaylist.setFont(font)
        self.cbOnlyPlaylist.setStyleSheet("QCheckBox {\n"
"    padding: 10 0;\n"
"    border-radius: 8;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width : 16;\n"
"    height: 16;\n"
"    border: 1px solid white;\n"
"    border-radius: 4;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #FF3C6A;\n"
"    border-color: #FF3C6A;\n"
"}")
        self.cbOnlyPlaylist.setChecked(False)
        self.cbOnlyPlaylist.setObjectName("cbOnlyPlaylist")
        self.verticalLayout_4.addWidget(self.cbOnlyPlaylist)
        self.verticalLayout.addWidget(self.widget_10)
        self.widget_7 = QtWidgets.QWidget(self.grOptions)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lFormat = QtWidgets.QLabel(self.widget_7)
        self.lFormat.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lFormat.setFont(font)
        self.lFormat.setObjectName("lFormat")
        self.horizontalLayout_3.addWidget(self.lFormat)
        self.cmbFormat = QtWidgets.QComboBox(self.widget_7)
        self.cmbFormat.setMinimumSize(QtCore.QSize(0, 42))
        self.cmbFormat.setStyleSheet("#cmbFormat {\n"
"    padding: 10;\n"
"    background-color: #3e3e3e;\n"
"    border-radius: 4;\n"
"}\n"
"\n"
"\n"
"#cmbFormat::drop-down {\n"
"    right: 10;\n"
"    width: 20;\n"
"    image: url(:/icons/assets/down-arrow.png)\n"
"}")
        self.cmbFormat.setObjectName("cmbFormat")
        self.cmbFormat.addItem("")
        self.cmbFormat.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbFormat)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_9 = QtWidgets.QWidget(self.grOptions)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iDestination = QtWidgets.QLineEdit(self.widget_9)
        self.iDestination.setMinimumSize(QtCore.QSize(200, 40))
        self.iDestination.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.iDestination.setFont(font)
        self.iDestination.setStyleSheet("QLineEdit {\n"
"    padding: 5;\n"
"min-height:30;\n"
"border-radius: 4;\n"
"    background-color: #3e3e3e;\n"
"}")
        self.iDestination.setReadOnly(True)
        self.iDestination.setObjectName("iDestination")
        self.horizontalLayout_2.addWidget(self.iDestination)
        self.bDestination = QtWidgets.QPushButton(self.widget_9)
        self.bDestination.setMinimumSize(QtCore.QSize(100, 40))
        self.bDestination.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bDestination.setFont(font)
        self.bDestination.setStyleSheet("#bDestination {\n"
"    background-color: #666;\n"
"    border-radius: 4;\n"
"    border: 1px solid #333;\n"
"}")
        self.bDestination.setObjectName("bDestination")
        self.horizontalLayout_2.addWidget(self.bDestination)
        self.verticalLayout.addWidget(self.widget_9)
        self.widget_11 = QtWidgets.QWidget(self.grOptions)
        self.widget_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lNoLib = QtWidgets.QLabel(self.widget_11)
        self.lNoLib.setEnabled(True)
        self.lNoLib.setVisible(False)
        self.lNoLib.setStyleSheet("#lNoLib {\n"
"    color: red;\n"
"}")
        self.lNoLib.setObjectName("lNoLib")
        self.horizontalLayout_4.addWidget(self.lNoLib)
        self.bMoreOptions = QtWidgets.QPushButton(self.widget_11)
        self.bMoreOptions.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bMoreOptions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bMoreOptions.setStyleSheet("#bMoreOptions {\n"
"    border: none;\n"
"    background: #3e3e3e;\n"
"    padding: 7;\n"
"    border-radius: 4;\n"
"}")
        self.bMoreOptions.setObjectName("bMoreOptions")
        self.horizontalLayout_4.addWidget(self.bMoreOptions)
        self.verticalLayout.addWidget(self.widget_11)
        self.gridLayout_6.addWidget(self.grOptions, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bSync = QtWidgets.QPushButton(self.widget_5)
        self.bSync.setEnabled(True)
        self.bSync.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bSync.setFont(font)
        self.bSync.setStyleSheet("#bSync {\n"
"    padding: 15;\n"
"    border-radius: 4;\n"
"    background-color: #FF3C6A;\n"
"}\n"
"\n"
"#bSync:disabled {\n"
"    background-color: #3e3e3e;\n"
"}")
        self.bSync.setObjectName("bSync")
        self.horizontalLayout.addWidget(self.bSync)
        self.gridLayout.addWidget(self.widget_5, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lPlaylists.setText(_translate("MainWindow", "Playlists"))
        self.lPlaylistCount.setText(_translate("MainWindow", "0"))
        self.lArtists.setText(_translate("MainWindow", "Artists"))
        self.lArtistCount.setText(_translate("MainWindow", "0"))
        self.lAlbums.setText(_translate("MainWindow", "Albums"))
        self.lAlbumCount.setText(_translate("MainWindow", "0"))
        self.lOptions.setText(_translate("MainWindow", "Playlist Options"))
        self.cbExtended.setText(_translate("MainWindow", "Use extended playlist format"))
        self.cbOnlyPlaylist.setText(_translate("MainWindow", "Only create playlists (don\'t copy files)"))
        self.lFormat.setText(_translate("MainWindow", "Playlist Format"))
        self.cmbFormat.setPlaceholderText(_translate("MainWindow", "playlist format"))
        self.cmbFormat.setItemText(0, _translate("MainWindow", "m3u"))
        self.cmbFormat.setItemText(1, _translate("MainWindow", "m3u8"))
        self.iDestination.setPlaceholderText(_translate("MainWindow", "Destination Folder"))
        self.bDestination.setText(_translate("MainWindow", "select"))
        self.lNoLib.setText(_translate("MainWindow", "No Library defined! Please provide XML file. "))
        self.bMoreOptions.setText(_translate("MainWindow", "More Options  »"))
        self.bSync.setText(_translate("MainWindow", "SYNC"))
