from functools import partial

from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, \
    QLineEdit, QMessageBox, QComboBox
import sqlite3
import sys
from XMLFunctions import XMLFuctions
import DBFunctions

from websockets.asyncio.client import connect

class ImportWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, number_line_edits, name_line_edits, team_name):
        super().__init__()
        self.number_line_edits = number_line_edits
        self.name_line_edits = name_line_edits
        self.team_name = team_name
        self.resize(200, 100)
        layout = QVBoxLayout()
        self.label = QLabel("Mannschaft wählen")
        layout.addWidget(self.label)
        self.team_box = QComboBox(self)
        names = DBFunctions.get_all_table_names("Teams.db")
        for name in names:
            self.team_box.addItem(name[0])
        layout.addWidget(self.team_box)
        layout_buttons = QHBoxLayout()
        button_import = QPushButton("Importieren")
        button_abort = QPushButton("Abbrechen")
        layout_buttons.addWidget(button_import)
        layout_buttons.addWidget(button_abort)
        layout.addLayout(layout_buttons)
        self.setLayout(layout)

        button_import.clicked.connect(self.import_team)

    def import_team(self):
        self.team_name.setText(self.team_box.currentText())
        values = DBFunctions.get_team_values("Teams.db", self.team_box.currentText())
        for i in range(0, len(values)):
            self.name_line_edits[i].setText(str(values[i][0]))
            self.number_line_edits[i].setText(str(values[i][1]))

        self.close()




class NewTeamWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.resize(300, 450)
        self.setWindowTitle("New Game Window")
        layout_main = QGridLayout()

        label_teamname = QLabel("Teamname")
        self.le_teamname = QLineEdit()

        label_name = QLabel("Name")
        label_number = QLabel("Nummer")

        layout_main.addWidget(label_teamname, 0, 0)
        layout_main.addWidget(self.le_teamname, 0, 1)

        line_name_1 = QLineEdit()
        line_name_2 = QLineEdit()
        line_name_3 = QLineEdit()
        line_name_4 = QLineEdit()
        line_name_5 = QLineEdit()
        line_name_6 = QLineEdit()
        line_name_7 = QLineEdit()
        line_name_8 = QLineEdit()
        line_name_9 = QLineEdit()
        line_name_10 = QLineEdit()
        line_name_11 = QLineEdit()
        line_name_12 = QLineEdit()
        line_name_13 = QLineEdit()
        line_name_14 = QLineEdit()

        self.all_line_names = [line_name_1, line_name_2, line_name_3, line_name_4, line_name_5, line_name_6, line_name_7, line_name_8, line_name_9, line_name_10, line_name_11, line_name_12, line_name_13, line_name_14]

        line_number_1 = QLineEdit()
        line_number_2 = QLineEdit()
        line_number_3 = QLineEdit()
        line_number_4 = QLineEdit()
        line_number_5 = QLineEdit()
        line_number_6 = QLineEdit()
        line_number_7 = QLineEdit()
        line_number_8 = QLineEdit()
        line_number_9 = QLineEdit()
        line_number_10 = QLineEdit()
        line_number_11 = QLineEdit()
        line_number_12 = QLineEdit()
        line_number_13 = QLineEdit()
        line_number_14 = QLineEdit()


        self.all_line_numbers = [line_number_1, line_number_2, line_number_3, line_number_4, line_number_5, line_number_6, line_number_7, line_number_8, line_number_9, line_number_10, line_number_11, line_number_12, line_number_13, line_number_14  ]

        layout_main.addWidget(label_name, 1, 0)
        layout_main.addWidget(line_name_1, 2, 0)
        layout_main.addWidget(line_name_2, 3, 0)
        layout_main.addWidget(line_name_3, 4, 0)
        layout_main.addWidget(line_name_4, 5, 0)
        layout_main.addWidget(line_name_5, 6, 0)
        layout_main.addWidget(line_name_6, 7, 0)
        layout_main.addWidget(line_name_7, 8, 0)
        layout_main.addWidget(line_name_8, 9, 0)
        layout_main.addWidget(line_name_9, 10, 0)
        layout_main.addWidget(line_name_10, 11, 0)
        layout_main.addWidget(line_name_11, 12, 0)
        layout_main.addWidget(line_name_12, 13, 0)
        layout_main.addWidget(line_name_13, 14, 0)
        layout_main.addWidget(line_name_14, 15, 0)

        layout_main.addWidget(label_number, 1, 1)
        layout_main.addWidget(line_number_1, 2, 1)
        layout_main.addWidget(line_number_2, 3, 1)
        layout_main.addWidget(line_number_3, 4, 1)
        layout_main.addWidget(line_number_4, 5, 1)
        layout_main.addWidget(line_number_5, 6, 1)
        layout_main.addWidget(line_number_6, 7, 1)
        layout_main.addWidget(line_number_7, 8, 1)
        layout_main.addWidget(line_number_8, 9, 1)
        layout_main.addWidget(line_number_9, 10, 1)
        layout_main.addWidget(line_number_10, 11, 1)
        layout_main.addWidget(line_number_11, 12, 1)
        layout_main.addWidget(line_number_12, 13, 1)
        layout_main.addWidget(line_number_13, 14, 1)
        layout_main.addWidget(line_number_14, 15, 1)




        self.player_numbers = []
        for player_number in self.all_line_numbers:
            self.player_numbers.append(player_number.text())
        button = QPushButton("Neue Mannschaft")
        button_import = QPushButton("Mannschaft importieren")
        layout_main.addWidget(button, 16, 0)
        layout_main.addWidget(button_import, 16, 1)

        self.setLayout(layout_main)

        button.clicked.connect(self.create_new_team)
        button_import.clicked.connect(self.import_team)

    def import_team(self):
        self.w = ImportWindow(self.all_line_numbers, self.all_line_names, self.le_teamname)
        self.w.show()

    def check_fields(self):

        for i in range(0,len(self.all_line_names)):
            name_exist = False
            if self.all_line_names[i].text():
                name_exist = True
            number_exist = False
            if self.all_line_numbers[i].text():
                number_exist = True
            if name_exist ^ number_exist:
                return False

            if number_exist and (not self.all_line_numbers[i].text().isdigit()):
                return False
            #break

        return True

    def check_duplicate_numbers(self):
        result = []
        for number in self.all_line_numbers:
            if number.text() != "":
                result.append(number.text())
        return len(result) != len(set(result))


    def check_enough_players(self):
        result = []
        for number in self.all_line_numbers:
            if number.text() != "":
                result.append(number.text())

        return len(result) > 5


    def create_new_team(self):
       if DBFunctions.check_table_exists('Teams.db', self.le_teamname.text()):

            self.show_warning("Team exisitert bereits")
       else:
            DBFunctions.create_new_team(self.le_teamname.text())

            for i in range(0,len(self.all_line_numbers)):
                if self.all_line_numbers[i].text():
                    DBFunctions.insert_player_in_table(self.le_teamname.text(), self.all_line_numbers[i].text(), self.all_line_names[i].text())



    def check_inputs(self):
        if not self.check_enough_players() :
            self.show_warning("Nicht genug Spieler")
            return False
        if not self.check_fields():
            self.show_warning("Felder nicht ausgefüllt")
            return False
        if self.check_duplicate_numbers():
            self.show_warning("Nummern doppelt")
            return False

        return True

    def show_warning(self, s):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(s)
        msg.setWindowTitle("Fehler")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        retval = msg.exec()
