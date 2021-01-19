from loadingdialog import Ui_dgLoading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

class DialogLoading(QDialog, Ui_dgLoading):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogLoading, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dgLoadingLibProgress.setMaximum(100)

    def update(self, val):
        self.dgLoadingLibProgress.setValue(val)

    def done(self):
        self.hide()


