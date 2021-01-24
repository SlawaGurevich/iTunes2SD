from loadingdialog import Ui_dgLoading
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

class DialogLoading(QDialog, Ui_dgLoading):
    def __init__(self, *args, **kwargs):
        super(DialogLoading, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setupUi(self)

    def done(self, s):
        print("done")
        self.hide()


