from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import Qt


class Dialogs:
    def showdialog_lineUp(self):
        d = QDialog()

        okButton = QPushButton("ok", d)
        abortButton = QPushButton("Abbrechen", d)
        d.setWindowTitle("Fehler")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

        def closwDialog(self):
            self.close


