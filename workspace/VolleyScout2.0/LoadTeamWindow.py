from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, \
    QMessageBox, QComboBox, QHBoxLayout
import sqlite3
import DBFunctions
import sys

class ImportWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.resize(200, 100)
        layout = QVBoxLayout()
        self.label = QLabel("Mannschaft wählen")
        layout.addWidget(self.label)
        self.team_box = QComboBox(self)
        names = DBFunctions.get_all_table_names("VolleyScout2.db")
        for name in names:
            self.team_box.addItem(name[0])
        layout.addWidget(self.team_box)
        layout_buttons = QHBoxLayout()
        button_import = QPushButton("Laden")
        button_abort = QPushButton("Abbrechen")
        layout_buttons.addWidget(button_import)
        layout_buttons.addWidget(button_abort)
        layout.addLayout(layout_buttons)
        self.setLayout(layout)

        button_import.clicked.connect(self.load_team)

    def load_team(self):
        pass