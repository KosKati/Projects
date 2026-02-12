from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QFormLayout, QPushButton, QGroupBox, QLineEdit, \
    QDateEdit, QMainWindow, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path

from icecream import ic

import JsonFunctions
import os.path
import json
from Libero_Settings_Window import LiberoSubPlayerSettings
from PlayerSubWindow import PlayerSubWindow


class CourtWidgets(QWidget):

    left_layout_front: QHBoxLayout | QHBoxLayout

    def __init__(self, player_stat_frame):
        super().__init__()

        self.libero_settings = None
        self.player_stat_frame = player_stat_frame
        self.left_side = QGroupBox()
        #self.left_side.setStyleSheet("border: 1px solid black;")
        #left_side_layout = QGridLayout()
        self.left_side_layout = QVBoxLayout()
        self.left_side_layout.setContentsMargins(0, 100, 0, 0)


        self.left_layout_front = QHBoxLayout()
        self.left_layout_front.setContentsMargins(44, 30, 40, 0)
        self.left_layout_back = QHBoxLayout()
        self.left_layout_back.setContentsMargins(44, 30, 40, 0)
        self.left_layout_libero_subs = QHBoxLayout()
        self.left_layout_libero_subs.setContentsMargins(0, 100 , 0, 0)
        self.left_layout_libero_subs_back = QHBoxLayout()
        self.label_1 = QLabel("Pos. 1")
        self.label_1.setStyleSheet("font-size: 16px;")
        self.label_1.setFixedWidth(50)
        self.label_2 = QLabel("Pos. 2")


        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_2 = QLabel("Pos. 2")
        self.label_2.setFixedWidth(50)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setStyleSheet("font-size: 16px;")
        self.label_3 = QLabel("Pos. 3")
        self.label_3.setFixedWidth(50)
        self.label_3.setStyleSheet("font-size: 16px;")
        self.label_4 = QLabel("Pos. 4")
        self.label_4.setFixedWidth(50)

        self.label_4.setStyleSheet("font-size: 16px;")
        self.label_5 = QLabel("Pos. 5")
        self.label_5.setFixedWidth(50)
        self.label_5.setStyleSheet("font-size: 16px;")
        self.label_6 = QLabel("Pos. 6")
        self.label_6.setFixedWidth(50)
        self.label_6.setStyleSheet("font-size: 16px;")
        self.label_libero_1 = QLabel("Libero 1 :")
        self.label_libero_1.setStyleSheet("font-size: 16px;")
        self.label_libero_1_label = QLabel("L1")
        self.label_libero_1_label.setStyleSheet("font-size: 16px;")
        self.label_libero_2 = QLabel("Libero 2 :")
        self.label_libero_2.setStyleSheet("font-size: 16px;")
        self.label_libero_2_label = QLabel("L2")
        self.label_libero_2_label.setStyleSheet("font-size: 16px;")
        self.label_libero_sub = QLabel("Libero Sub :")
        self.label_libero_sub.setStyleSheet("font-size: 16px;")
        self.label_libero_sub_label = QLabel("LS")
        self.label_libero_sub_label.setStyleSheet("font-size: 16px;")

        self.left_layout_back.addWidget(self.label_5)
        self.left_layout_back.addWidget(self.label_6)
        self.left_layout_back.addWidget(self.label_1)


        self.left_layout_front.addWidget(self.label_4)
        self.left_layout_front.addWidget(self.label_3)
        self.left_layout_front.addWidget(self.label_2)
        self.label_placeholder = QLabel("")
        self.left_layout_libero_subs.addWidget(self.label_libero_1)
        self.left_layout_libero_subs.addWidget(self.label_libero_1_label)
        self.left_layout_libero_subs.addWidget(self.label_libero_2)
        self.left_layout_libero_subs.addWidget(self.label_libero_2_label)
        self.left_layout_libero_subs_back.addWidget(self.label_libero_sub)
        self.left_layout_libero_subs_back.addWidget(self.label_libero_sub_label)
        self.left_layout_libero_subs_back.addWidget(self.label_placeholder)
        self.left_layout_libero_subs_back.addWidget(self.label_placeholder)



        self.left_side_layout.addLayout(self.left_layout_front,1)
        self.left_side_layout.addLayout(self.left_layout_back,1)
        self.left_side_layout.addLayout(self.left_layout_libero_subs,1)
        self.left_side_layout.addLayout(self.left_layout_libero_subs_back,1)

        self.left_side_layout.insertSpacing(0, 20)
        self.left_side_layout.insertSpacing(2, 70)
        """
        left_side_layout.addWidget(label_1, 1, 2)
        left_side_layout.addWidget(label_2, 0, 2)
        left_side_layout.addWidget(label_3, 0, 1)
        left_side_layout.addWidget(label_4, 0, 0, 2, 1)
        left_side_layout.addWidget(label_5, 3, 0, 2, 1)
        left_side_layout.addWidget(label_6, 1, 1 )
        left_side_layout.addWidget(label_libero_1, 2, 0, 1, 4)
        left_side_layout.addWidget(label_libero_1_label, 2, 4, 1, 4)
        left_side_layout.addWidget(label_libero_2, 3, 0, 1, 4)
        left_side_layout.addWidget(label_libero_2_label, 3, 4, 1, 4)
        left_side_layout.addWidget(label_libero_sub, 2, 8, 1, 4)
        left_side_layout.addWidget(label_libero_sub_label, 2, 12, 1, 4)
"""
        self.labels_court = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6]

        label = QLabel("")
        label.setStyleSheet("background-color: lightgreen")
        self.left_side.setLayout(self.left_side_layout)

        self.team_window = QGroupBox()
        team_layout = QGridLayout()

        btn_rotation =QPushButton("Rotieren")
        btn_sub = QPushButton("Spielerwechsel")
        btn_libero_1 = QPushButton("Libero 1 in/out")
        btn_libero_2 = QPushButton("Libero 2 in/out")
        btn_libero_settings = QPushButton("Libero Einstellungen")

        label_plyr_1 = QLabel("P1")
        label_plyr_2 = QLabel("P2")
        label_plyr_3 = QLabel("P3")
        label_plyr_4 = QLabel("P4")
        label_plyr_5 = QLabel("P5")
        label_plyr_6 = QLabel("P6")
        label_plyr_7 = QLabel("P7")
        label_plyr_8 = QLabel("P8")
        label_plyr_9 = QLabel("P9")
        label_plyr_10 = QLabel("P10")
        label_plyr_11 = QLabel("P11")
        label_plyr_12 = QLabel("P12")
        label_plyr_13 = QLabel("P13")
        label_plyr_14 = QLabel("P14")


        self.left_players_labels = [label_plyr_1, label_plyr_2, label_plyr_3, label_plyr_4, label_plyr_5, label_plyr_6, label_plyr_7, label_plyr_8, label_plyr_9, label_plyr_10, label_plyr_11, label_plyr_12, label_plyr_13, label_plyr_14]

        team_layout.addWidget(label_plyr_1, 0, 0, 1, 1)
        team_layout.addWidget(label_plyr_2, 0, 1, 1, 1)
        team_layout.addWidget(label_plyr_3, 0, 2, 1, 1)
        team_layout.addWidget(label_plyr_4, 0, 3, 1, 1)
        team_layout.addWidget(label_plyr_5, 0, 4, 1, 1)
        team_layout.addWidget(label_plyr_6, 1, 0, 1, 1)
        team_layout.addWidget(label_plyr_7, 1, 1, 1, 1)
        team_layout.addWidget(label_plyr_8, 1, 2, 1, 1)
        team_layout.addWidget(label_plyr_9, 1, 3, 1, 1)
        team_layout.addWidget(label_plyr_10, 1, 4, 1, 1)
        team_layout.addWidget(label_plyr_11, 2, 0, 1, 1)
        team_layout.addWidget(label_plyr_12, 2, 1, 1, 1)
        team_layout.addWidget(label_plyr_13, 2, 2, 1, 1)
        team_layout.addWidget(label_plyr_14, 2, 3, 1, 1)
        team_layout.addWidget(btn_rotation, 3, 0, 1, 1)
        team_layout.addWidget(btn_sub, 3, 1, 1, 1)
        team_layout.addWidget(btn_libero_1, 3, 2, 1, 1)
        team_layout.addWidget(btn_libero_2, 3, 3, 1, 1)
        team_layout.addWidget(btn_libero_settings, 3, 4, 1, 1)


        self.team_window.setLayout(team_layout)
        btn_rotation.clicked.connect(self.rotieren)
        btn_libero_settings.clicked.connect(self.show_libero_settings)
        btn_sub.clicked.connect(self.sub_players)

        try:
            libero_1 = JsonFunctions.get_libero_1()
            libero_2 = JsonFunctions.get_libero_2()
            btn_libero_1.clicked.connect(lambda : self.libero_io(libero_1, libero_2 ))
            btn_libero_2.clicked.connect(lambda : self.libero_io(libero_2 , libero_1))
        except:
            print("No libero 1")

    def sub_players(self):
        self.sub_player_window = PlayerSubWindow(self.labels_court)
        self.sub_player_window.show()

    def libero_io(self, libero_sub, libero_in):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

            line_up = data["line_up"]
            libero_1 = libero_sub
            libero_2 = libero_in
            sub_1 = data["sub1"]
            sub_2 = data["sub2"]
            data_warte = data["warte"]

            # def libero_out_test(self, libero, sub, line_up, data_warte, data_sub ):
            if sub_1 in [line_up[0], line_up[4], line_up[5]]:
                self.libero_in_test(libero_1, sub_1, line_up, data_warte, sub_1)
                return None

            elif sub_2 in [line_up[0], line_up[4], line_up[5]]:
                self.libero_in_test(libero_1, sub_2, line_up, data_warte, sub_2)
                return None

            elif libero_1 in [line_up[0], line_up[4], line_up[5]]:
                self.libero_out_test(libero_1, line_up, data_warte)
                return None

            else:
                if libero_2 in [line_up[0], line_up[4], line_up[5]]:
                    self.other_libero_in_test(libero_1, libero_2, line_up, data_warte)
                return None

    def other_libero_in_test(self, libero_1, libero_2, line_up, data_warte):

        if libero_2 in [line_up[0], line_up[4], line_up[5]]:
            idx = line_up.index(libero_2)
            line_up[idx] = libero_1
            libero_2 = f"{libero_2}(L)"
            for court_label in self.labels_court:
                if court_label.text() == libero_2:
                    court_label.setText(f"{libero_1}(L)")

            JsonFunctions.set_line_up(line_up)

    def libero_out_test(self, libero, line_up, data_warte):
        if libero in [line_up[0], line_up[4], line_up[5]]:
            idx = line_up.index(libero)
            line_up[idx] = data_warte
            for court_label in self.labels_court:
                if court_label.text() == f"{libero}(L)":

                    court_label.setText(f"{data_warte}")
            JsonFunctions.set_warte("")
            JsonFunctions.set_line_up(line_up)

    def libero_in_test(self, libero, sub, line_up, data_warte, data_sub):
        if sub in [line_up[0], line_up[4], line_up[5]]:
            idx = line_up.index(sub)
            JsonFunctions.set_warte(line_up[idx])
            # self.replace_warte(line_up[idx])
            line_up[idx] = libero

            for court_label in self.labels_court:
                if court_label.text() == data_sub:
                    court_label.setText(f"{libero}(L)")
            JsonFunctions.set_line_up(line_up)

    def replace_warte(self, new_value):
        with open("./Data/Line_up_data.json", "r") as f:
            data = json.load(f)
            data["warte"] = new_value

        with open("./Data/Line_up_data.json", "w") as f:
            json.dump(data, f)

    def show_libero_settings(self):
        self.libero_settings = LiberoSubPlayerSettings(self.labels_court)
        self.libero_settings.show()

    def rotieren(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

        line_up = data["line_up"]

        tmp = line_up.pop(0)
        line_up.append(tmp)
        for i in range(0, len(self.labels_court)):
            if self.check_libero(line_up[i]):
                self.labels_court[i].setText(f"{str(line_up[i])}(L)")
            else:
                self.labels_court[i].setText(str(line_up[i]))

        if self.check_libero(line_up[3]):
            line_up[3] = data["warte"]

            for court_label in self.labels_court:
                if court_label.text() == f"{self.return_libero_number_in_court()}(L)":
                    court_label.setText(f"{data["warte"]}")
            data["warte"] = ""

        field_key = 'line_up'
        if field_key in data:
            data[field_key] = line_up
        file_path = "./Data/Line_up_data.json"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        with open("./Data/Line_up_data.json", "w") as f:
            json.dump(data, f)

    def return_libero_number_in_court(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

        libero_1 = data["libero1"]
        libero_2 = data["libero2"]
        line_up = data["line_up"]

        if libero_1 in line_up:
            return libero_1
        elif libero_2 in line_up:
            return libero_2
        else:
            print("No libero")

    def check_libero(self, number):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

        libero_1 = data["libero1"]
        libero_2 = data["libero2"]

        if number == libero_1 or number == libero_2:
            return True

        return False
