from PyQt5.QtWidgets import QMessageBox


class LoadingMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Loading library...")
        self.setText("Please wait while the library is being loaded.")
        self.setStandardButtons(QMessageBox.Cancel)
        self.buttonClicked.connect(self.button_clicked)

    def button_clicked(self, i):
        print(i)
        pass
