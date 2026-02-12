from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, \
    QMessageBox, QComboBox
import sqlite3

from icecream import ic

import DBFunctions
import sys

from websockets.asyncio.client import connect


class NewGameWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, team_labels, player_stat_frame, current_set_layout, old_body):
        super().__init__()
        self.old_body = old_body
        self.current_set_layout = current_set_layout
        self.player_stat_frame = player_stat_frame
        self.team_name = None
        self.team_labels = team_labels
        self.resize(210, 270)
        self.setWindowTitle("New Game Window")
        layout = QVBoxLayout()
        self.label_team_to_analye = QLabel("Name des anaylsierendes Teams:")
        self.line_edit_team_to_analye = QLineEdit(self)
        self.label_opponent_to_analye = QLabel("Name des Gegners:")
        self.line_edit_opponent = QLineEdit(self)
        self.label_id = QLabel("ID:")
        self.label_team = QLabel("Mannschaft wählen")
        self.label_placeholder = QLabel("")
        self.line_id = QLineEdit(self)
        self.make_new_game_button = QPushButton("Neues Spiel erstellem")
        self.team_box = QComboBox(self)
        self.table_name = None
        names = DBFunctions.get_all_table_names("Teams.db")
        for name in names:
            self.team_box.addItem(name[0])

        self.table_name = None

        layout.addWidget(self.label_team_to_analye)
        layout.addWidget(self.line_edit_team_to_analye)
        layout.addWidget(self.label_opponent_to_analye)
        layout.addWidget(self.line_edit_opponent)
        layout.addWidget(self.label_id)
        layout.addWidget(self.line_id)
        layout.addWidget(self.label_team)
        layout.addWidget(self.team_box)
        layout.addWidget(self.label_placeholder)
        layout.addWidget(self.make_new_game_button)


        self.setLayout(layout)

        self.make_new_game_button.clicked.connect(self.create_new_game)


    def create_new_game(self):
        self.table_name = self.create_table_name()
        if self.check_table_exists(self.table_name):

            self.show_warning("Tabelle existiert bereits!")
        else:
            self.create_table()

            self.insert_stats_values()
            self.set_label_values()

            self.update_stat_frame()

            self.write_database_name_to_file()

            self.set_set1()

    def write_database_name_to_file(self):
        with open("./Data/Database_name.txt", "w") as f:  # in write mode
            f.write(self.table_name)

    def set_set1(self):
        with open("./Data/Current_Set.txt", "w") as f:  # in write mode
            f.write("Satz 1")

    def update_stat_frame(self):
        numbers = []
        names = []
        rows = DBFunctions.get_all_numbers('Volleyscout2.db',self.table_name)
        for i in range(0, len(rows)):
            numbers.append(rows[i][0])

        rows_names = DBFunctions.get_all_player_names('Volleyscout2.db',self.table_name)
        for i in range(0, len(rows)):
            names.append(rows_names[i][0])

        numbers = list(filter(lambda num: num is not None, numbers))
        names = list(filter(lambda num: num is not None, names))
        body_new = self.player_stat_frame.create_body(numbers)
        self.player_stat_frame.insert_names_to_label(names)
        self.current_set_layout.replaceWidget(self.old_body, body_new)

        self.old_body.hide()
        self.old_body.deleteLater()

    def insert_stats_values(self):
        values = DBFunctions.get_team_values("Teams.db", self.team_box.currentText())
        print("val")
        print(values[1][0])
        for i in range(0, len(values)):
            DBFunctions.insert_number(self.table_name, str(values[i][1]), str(values[i][0]))


        rows = DBFunctions.get_all_numbers('Volleyscout2.db', self.table_name )

        for i in range(0,len(rows)):
            DBFunctions.insert_start_values(self.table_name, str(rows[i][0]))


        DBFunctions.insert_start_values_set(self.table_name)
        DBFunctions.insert_start_values_game_stats(self.table_name)
        DBFunctions.insert_start_values_sets_stats(self.table_name)
        DBFunctions.insert_start_values_rotation_stats(self.table_name)
        DBFunctions.insert_start_values_reception_defense_points_stats(self.table_name)
        DBFunctions.insert_start_values_so_bp_stats(self.table_name)


    def set_label_values(self):
        self.team_name = self.team_box.currentText()
        values = DBFunctions.get_team_values("Teams.db", self.team_box.currentText())
        for i in range(0, len(values)):
            self.team_labels[i].setText(str(values[i][1] + " " + str(values[i][0])))

        self.close()

    def create_table_name(self):

        if self.line_edit_team_to_analye.text() == "":
            self.show_warning("Bitte geben Sie ein \nzu analysierendes Team ein")
        else:
            self.table_name = f"game_data{self.add_value(self.line_edit_team_to_analye.text())}{self.add_value(self.line_edit_opponent.text())}{self.add_value(self.line_id.text())}"

        return self.table_name

    def add_value(self,s):
        if s == "":
            return s
        else:
            return "_"+ s

    def check_table_exists(self, table_name):
        connection_insert = sqlite3.connect('VolleyScout2.db')
        cursor_insert = connection_insert.cursor()

        _SQL = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor_insert.execute(_SQL)
        results = cursor_insert.fetchall()
        result = None
        for table in results:
            if table_name == table[0]:
                result =  True
                break
            else:
                result = False
        connection_insert.close()
        return result

    def show_warning(self, s):
            button = QMessageBox.critical(
                    self,
                    "Fehler",
                    s,
                    buttons=QMessageBox.StandardButton.Ok,

                    defaultButton=QMessageBox.StandardButton.Ok,
                )

            if button == QMessageBox.StandardButton.Discard:
                    pass

    def create_table(self):
        self.table_name = self.create_table_name()
        if self.check_table_exists(self.table_name):

            self.show_warning("Tabelle existiert bereits!")
        else:
            connection = sqlite3.connect('VolleyScout2.db')
            cursor = connection.cursor()
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS  {self.table_name} (
                                Number TEXT,
                                Name TEXT,
                                Action TEXT,
                                Evaluation TEXT,
                                Rotation TEXT,
                                Timestamp TEXT, 
                                Points_Data TEXT, 
                                Service_Data TEXT, 
                                Reception_Data TEXT, 
                                Attack_Data TEXT, 
                                Block_Data TEXT, 
                                Details TEXT,
                                Current_Set TEXT, 
                                ID TEXT,
                                Set1_points TEXT,
                                Set1_service TEXT,
                                Set1_reception TEXT,
                                Set1_attack TEXT,
                                Set1_block TEXT,
                                Set2_points TEXT,
                                Set2_service TEXT,
                                Set2_reception TEXT,
                                Set2_attack TEXT,
                                Set2_block TEXT,
                                Set3_points TEXT,
                                Set3_service TEXT,
                                Set3_reception TEXT,
                                Set3_attack TEXT,
                                Set3_block TEXT,
                                Set4_points TEXT,
                                Set4_service TEXT,
                                Set4_reception TEXT,
                                Set4_attack TEXT,
                                Set4_block TEXT,
                                Set5_points TEXT,
                                Set5_service TEXT,
                                Set5_reception TEXT,
                                Set5_attack TEXT,
                                Set5_block TEXT,
                                game_stats TEXT,
                                rotation1_difference TEXT,
                                rotation2_difference TEXT,
                                rotation3_difference TEXT,
                                rotation4_difference TEXT,
                                rotation5_difference TEXT,
                                rotation6_difference TEXT,
                                points_good_reception TEXT,
                                points_bad_reception TEXT,
                                points_defense TEXT,
                                points_so TEXT,
                                points_bp TEXT)''')
            connection.close()



