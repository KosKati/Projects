from symtable import Class
from typing import List

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel
from StatsGame import AllStatsFrame
from PlayersStatLine import *
from dataclasses import dataclass

@dataclass
class StatPlayerLine:
    label_number: QGroupBox
    label_name: QGroupBox
    label_set: QGroupBox
    label_points: QGroupBox
    label_service: QGroupBox
    label_reception: QGroupBox
    label_attack: QGroupBox
    label_block: QGroupBox
    result_labels_number: List[QLabel]
    result_labels_name: List[QLabel]
    result_labels_set: List[QLabel]
    result_labels_points: List[QLabel]
    result_labels_service: List[QLabel]
    result_labels_reception: List[QLabel]
    result_labels_attack: List[QLabel]
    result_labels_block: List[QLabel]

@dataclass
class StatSetLine:
    label_set: QGroupBox
    label_points: QGroupBox
    label_service: QGroupBox
    label_reception: QGroupBox
    label_attack: QGroupBox
    label_block: QGroupBox
    result_labels_set: List[QLabel]
    result_labels_points: List[QLabel]
    result_labels_service: List[QLabel]
    result_labels_reception: List[QLabel]
    result_labels_attack: List[QLabel]
    result_labels_block: List[QLabel]






class PlayerFrame(QWidget):
    def __init__(self, players):
        super().__init__()
        self.all_labels_set = None
        self.set_names = None
        self.lay_header = None
        self.body = None
        self.body_row = None
        self.body_column = None
        self.header = None
        self.stat_header = None
        self.stat_list = []
        self.stat_set_list = []
        self.all_players_stats_labels = []
        self.players = [["1", "Linda Wilhelm"], ["2", "Mona Frauendorf"],["3", "Sophia Frauendorf"],["4", "Julia Mirgel"],
                        ["5", "Ina Mitte"],["6", "Maria Mitte2"],["7", "Jana Libero"],["8", " Alina Libero"],
                        ["9", "Vanessa "],["10", "Made"],["11", "Oli"],["12", "Anna Au"],["13", "Ahnugh"],
                        ["16", "Jojo"]]
        self.player_numbers = ["1", "2", "3","4","5","6","7","8","9","10","11","12","13","14"]
        #self.
        #self.stat_list.append([QLabel("Nr."), QLabel("Spieler"), QLabel("Satz"), QLabel("Punkte"), QLabel("Aufschlag"), QLabel("Annahme"), QLabel("Angriff"), QLabel("Block")])

        for line in range(0,14):

            tmp_body_number = self.create_label_body(1)
            tmp_body_name =self.create_label_body(1)
            tmp_body_set = self.create_label_body(5)
            tmp_body_points = self.create_label_body(3)
            tmp_body_service = self.create_label_body(3)
            tmp_body_reception = self.create_label_body(4)
            tmp_body_attack = self.create_label_body(5)
            tmp_body_block = self.create_label_body(1)
            self.stat_list.append(StatPlayerLine(label_number=tmp_body_number[0],
                                                 label_name=tmp_body_name[0],
                                                 label_set=tmp_body_set[0],
                                                 label_points=tmp_body_points[0],
                                                 label_attack=tmp_body_attack[0],
                                                 label_service=tmp_body_service[0],
                                                 label_reception=tmp_body_reception[0],
                                                 label_block=tmp_body_block[0],
                                                 result_labels_points=tmp_body_points[1],
                                                 result_labels_service=tmp_body_service[1],
                                                 result_labels_reception=tmp_body_reception[1],
                                                 result_labels_attack=tmp_body_attack[1],
                                                 result_labels_block=tmp_body_block[1],
                                                 result_labels_set=tmp_body_set[1],
                                                 result_labels_name=tmp_body_name[1],
                                                 result_labels_number=tmp_body_number[1]))

        for line in range(0, 5):

            tmp_body_set = self.create_label_body(1)
            tmp_body_points = self.create_label_body(4)
            tmp_body_service = self.create_label_body(3)
            tmp_body_reception = self.create_label_body(4)
            tmp_body_attack = self.create_label_body(5)
            tmp_body_block = self.create_label_body(1)
            self.stat_set_list.append(StatSetLine(
                                                 label_set=tmp_body_set[0],
                                                 label_points=tmp_body_points[0],
                                                 label_attack=tmp_body_attack[0],
                                                 label_service=tmp_body_service[0],
                                                 label_reception=tmp_body_reception[0],
                                                 label_block=tmp_body_block[0],
                                                 result_labels_points=tmp_body_points[1],
                                                 result_labels_service=tmp_body_service[1],
                                                 result_labels_reception=tmp_body_reception[1],
                                                 result_labels_attack=tmp_body_attack[1],
                                                 result_labels_block=tmp_body_block[1],
                                                 result_labels_set=tmp_body_set[1]))



    def create_label_header(self, values:list):
        result_layout = QVBoxLayout()
        header_label = QLabel(values[0])
        values_box = QHBoxLayout()
        for i in range(1,len(values)):
            tmp_label = QLabel(values[i])
            #tmp_label.layout().setContentsMargins(0,0,0,0)
            values_box.addWidget(tmp_label)
        result_layout.addWidget(header_label)
        result_layout.addLayout(values_box)

        result_box = QGroupBox()
        result_box.setLayout(result_layout)

        return result_box

    def create_label_body(self,fields: int):
        labels_list = []

        result_layout = QHBoxLayout()
        for i in range(fields):
            label_tmp = QLabel(".")


            result_layout.addWidget(label_tmp)
            labels_list.append(label_tmp)

        result_box = QGroupBox()

        result_box.setLayout(result_layout)
        #result_box
        return [result_box, labels_list]

    def create_header(self):
        label_header_number = self.create_label_header(["Nr"])
        #label_header_number.setStyleSheet("padding: 0px ")
        #label_header_number.layout().setContentsMargins(0,0,0,0)


        label_header_number.setFixedWidth(40)
        label_header_name = self.create_label_header(["Name"])
        #label_header_name.layout().setContentsMargins(0,0,0,0)
        label_header_name.setFixedWidth(133)
        label_header_set = self.create_label_header(["Satz"])
        #label_header_set.layout().setContentsMargins(0,0,0,0)
        label_header_set.setFixedWidth(133)
        label_header_points = self.create_label_header(["Punkte","Ges", "BP", "G-V"])
        #label_header_points.layout().setContentsMargins(0,0,0,0)
        label_header_points.setFixedWidth(133)
        label_header_service = self.create_label_header(["Aufschlag", "Ges", "Fhl", "Pkt"])
        #label_header_service.layout().setContentsMargins(0,0,0,0)
        label_header_service.setFixedWidth(134)
        label_header_reception = self.create_label_header(["Annahme", "Ges", "Fhl", "Pos%", "(Prf%)"])
        #label_header_reception.layout().setContentsMargins(0,0,0,0)
        label_header_reception.setFixedWidth(180)
        label_header_attack = self.create_label_header(["Angriff", "Ges", "Fhl", "Blo", "Pkt", "Pkt%"])
        label_header_attack.setFixedWidth(220)
        #label_header_attack.layout().setContentsMargins(0,0,0,0)
        label_header_block = self.create_label_header(["Block", "Pkt"])
        label_header_block.setFixedWidth(70)
        #label_header_block.layout().setContentsMargins(0, 0, 0, 0)
        self.header = QGroupBox()

        #self.header.setFlat(True)
        self.stat_header = QHBoxLayout()

        #self.stat_header.setSpacing(0)
        #self.stat_header.setContentsMargins(0,0,0,0)
        self.stat_header.addWidget(label_header_number)
        self.stat_header.addWidget(label_header_name)
        self.stat_header.addWidget(label_header_set)
        self.stat_header.addWidget(label_header_points)
        self.stat_header.addWidget(label_header_service)
        self.stat_header.addWidget(label_header_reception)
        self.stat_header.addWidget(label_header_attack)
        self.stat_header.addWidget(label_header_block)
        self.stat_header.layout().setSpacing(0)

        self.header.setLayout(self.stat_header)
        self.header.layout().setContentsMargins(0,0,0,0)
        return  self.header

    def create_header2(self):
        label_header_number = self.create_label_header(["Nr1"])
        label_header_number.setFixedWidth(50)
        label_header_number.setStyleSheet("padding-bottom: 0px ")
        label_header_name = self.create_label_header(["Name"])
        label_header_set = self.create_label_header(["Satz"])
        label_header_points = self.create_label_header(["Punkte","Ges", "BP", "G-V"])
        label_header_service = self.create_label_header(["Aufschlag", "Ges", "Fhl", "Pkt"])
        label_header_reception = self.create_label_header(["Annahme", "Ges", "Fhl", "Pos%", "(Prf%)"])
        label_header_attack = self.create_label_header(["Angriff", "Ges", "Fhl", "Blo", "Pkt", "Pkt%"])
        label_header_block = self.create_label_header(["Block", "Pkt"])

        self.header = QGroupBox()
        self.header.setStyleSheet("padding-bottom: 0px;")
        #self.header.setFlat(True)
        self.stat_header = QHBoxLayout()

        #self.stat_header.setSpacing(0)
        #self.stat_header.setContentsMargins(0,0,0,0)
        self.stat_header.addWidget(label_header_number)
        self.stat_header.addWidget(label_header_name)
        self.stat_header.addWidget(label_header_set)
        self.stat_header.addWidget(label_header_points)
        self.stat_header.addWidget(label_header_service)
        self.stat_header.addWidget(label_header_reception)
        self.stat_header.addWidget(label_header_attack)
        self.stat_header.addWidget(label_header_block)

        self.header.setLayout(self.stat_header)
        self.header.layout().setSpacing(0)
        return  self.stat_header

    def insert_names_to_label(self, names_list):
        for i in range(0, len(names_list)):
            self.stat_list[i].result_labels_name[0].setText(names_list[i])

    def create_body(self, players_numbers_list):

        self.body_row = QVBoxLayout()


        self.body_row.setSpacing(0)
        self.lay_header = self.create_header2()
        self.body_row.addLayout(self.lay_header)
        for i in range(0,len(players_numbers_list)):

            self.stat_list[i].result_labels_number[0].setText(players_numbers_list[i])

            self.stat_list[i].label_number.setFixedWidth(40)
            self.stat_list[i].label_name.setFixedWidth(133)
            self.stat_list[i].label_set.setFixedWidth(133)
            self.stat_list[i].label_points.setFixedWidth(133)
            self.stat_list[i].label_service.setFixedWidth(133)
            self.stat_list[i].label_reception.setFixedWidth(180)
            self.stat_list[i].label_attack.setFixedWidth(220)
            self.stat_list[i].label_block.setFixedWidth(70)
            self.body_column = QHBoxLayout()
            self.body_column.addWidget(self.stat_list[i].label_number)
            self.body_column.addWidget(self.stat_list[i].label_name)
            self.body_column.addWidget(self.stat_list[i].label_set)
            self.body_column.addWidget(self.stat_list[i].label_points)
            self.body_column.addWidget(self.stat_list[i].label_service)
            self.body_column.addWidget(self.stat_list[i].label_reception)
            self.body_column.addWidget(self.stat_list[i].label_attack)
            self.body_column.addWidget(self.stat_list[i].label_block)

            self.body_row.addLayout(self.body_column)
            self.body_row.layout().setSpacing(0)


        self.body = QGroupBox("")
        self.body.setFlat(True)

        self.body.setLayout(self.body_row)
        self.body.layout().setContentsMargins(0, 0, 0, 0)

        return self.body


    def create_stats_sets(self):
        self.set_names = ["Satz 1", "Satz 2", "Satz 3", "Satz 4", "Satz 5"]
        self.stats_sets_box = QGroupBox("Statistik")
        self.stats_sets_box.setContentsMargins(220,0,0,0)
        self.header_stat_points = QHBoxLayout()
        self.title_header = QHBoxLayout()
        self.values_header = QHBoxLayout()
        self.label_header = QLabel("Gew. Punkte")
        self.value_header_serv = QLabel("Auf    ")
        self.value_header_att = QLabel("Ang  ")
        self.value_header_blo = QLabel("Bk  ")
        self.value_header_uner = QLabel("GgFhl")
        self.values_header.setContentsMargins(0,0,750,0)
        self.header_stat_points.addWidget(self.label_header)
        self.title_header.addWidget(self.label_header)
        self.values_header.addWidget(self.value_header_serv)
        self.values_header.addWidget(self.value_header_att)
        self.values_header.addWidget(self.value_header_blo)
        self.values_header.addWidget(self.value_header_uner)
        self.header_stat_points.addLayout(self.title_header)
        self.header_stat_points.addLayout(self.values_header)

        self.body_row = QVBoxLayout()
        self.body_row.setContentsMargins(120,0,0,0)

        self.body_row.setSpacing(0)
        self.body_row.addLayout(self.header_stat_points)
        
        self.all_labels_set = []
        for i in range(0, len(self.set_names)):
            self.stat_set_list[i].result_labels_set[0].setText(self.set_names[i])
            self.stat_set_list[i].label_set.setFixedWidth(133)
            self.stat_set_list[i].label_points.setFixedWidth(133)
            self.stat_set_list[i].label_service.setFixedWidth(133)
            self.stat_set_list[i].label_reception.setFixedWidth(180)
            self.stat_set_list[i].label_attack.setFixedWidth(220)
            self.stat_set_list[i].label_block.setFixedWidth(70)
            self.all_labels_set.append(self.stat_set_list[i])
            self.body_column = QHBoxLayout()
            self.body_column.addWidget(self.stat_set_list[i].label_set)
            self.body_column.addWidget(self.stat_set_list[i].label_points)
            self.body_column.addWidget(self.stat_set_list[i].label_service)
            self.body_column.addWidget(self.stat_set_list[i].label_reception)
            self.body_column.addWidget(self.stat_set_list[i].label_attack)
            self.body_column.addWidget(self.stat_set_list[i].label_block)

            self.body_row.addLayout(self.body_column)
            self.body_row.layout().setSpacing(0)

        self.body = QGroupBox("")
        self.body.setFlat(True)

        self.body.setLayout(self.body_row)
        self.body.layout().setContentsMargins(0, 0, 0, 0)

        return self.body

class GameStats(QWidget):
    def __init__(self):
        super(GameStats, self).__init__()
        self.stat_serv_rece_labels = None
        self.defense_labels = None
        self.bad_reception_labels = None
        self.good_reception_labels = None

    def create_rotation_points(self):
        self.result_box = QVBoxLayout()
        self.tile = QLabel("Punkte \n Z in Diff")
        self.result_box.addWidget(self.tile)
        self.rotation_points_labels = []
        rotations_names_list = ["1", "6", "5", "4", "3", "2"]
        for i in reversed(range(6)):
            self.tmpbox = QHBoxLayout()
            self.tmp_label_position = QLabel(rotations_names_list[i])
            self.tmp_label_points = QLabel(".")
            self.rotation_points_labels.append(self.tmp_label_points)
            self.tmpbox.addWidget(self.tmp_label_position)
            self.tmpbox.addWidget(self.tmp_label_points)
            self.result_box.addLayout(self.tmpbox)



        return [self.result_box, self.rotation_points_labels]

    def create_serv_rece_points(self, label_header:str, label_value:str, stat_value:str, point_value:str ):
        self.result_box = QVBoxLayout()
        self.result_layout = QVBoxLayout()
        self.stat_serv_rece_labels = []

        self.tmp_header_layout = QHBoxLayout()
        self.tmp_hader_label = QLabel(label_header)
        self.tmp_header_layout.addWidget(self.tmp_hader_label)
        self.tmp_header_value = QLabel(".")
        self.tmp_header_layout.addWidget(self.tmp_header_value)
        self.result_layout.addLayout(self.tmp_header_layout)

        self.tmp_points_layout = QHBoxLayout()
        self.points_label = QLabel(label_value)
        self.points_label_value = QLabel(".")
        self.tmp_points_layout.addWidget(self.points_label)
        self.tmp_points_layout.addWidget(self.points_label_value)
        self.result_layout.addLayout(self.tmp_points_layout)

        self.stat_serv_rece_labels.append(self.tmp_header_value)
        self.stat_serv_rece_labels.append(self.points_label_value)


        self.stat_label_points = QLabel(f"Pro 0.00 {stat_value} \n 1 {point_value}")
        self.result_layout.addWidget(self.stat_label_points)
        self.stat_serv_rece_labels.append(self.stat_label_points)

        self.result_box.addLayout(self.result_layout)

        return [self.result_box, self.stat_serv_rece_labels]

    def create_reception_attack_frame(self):
        self.reception_attack_layout = QVBoxLayout()
        self.good_reception_layout = QHBoxLayout()
        self.bad_reception_layout = QHBoxLayout()
        self.defense_reception_layout = QHBoxLayout()
        self.good_reception_labels = []
        self.bad_reception_labels = []
        self.defense_labels = []

        self.label_title_good_reception = QLabel("Dir. Pkt. nach guter Annhame (+, ++, 1.Angriff)")
        self.label_error_title_good = QLabel("Fhl: ")
        self.label_error_title_good.setContentsMargins(30, 0, 0, 0)
        self.label_error_value_good = QLabel(".")
        self.label_blocked_title_good = QLabel("Blo: ")
        self.label_blocked_title_good.setContentsMargins(30, 0, 0, 0)
        self.label_blocked_value_good = QLabel(".")
        self.label_points_percent_title_good = QLabel("Pkt%: ")
        self.label_points_percent_title_good.setContentsMargins(30, 0, 0, 0)
        self.label_points_percent_value_good = QLabel(".")
        self.label_total_title_good = QLabel("Ges. : ")
        self.label_total_title_good.setContentsMargins(30, 0, 0, 0)
        self.label_total_value_good = QLabel(".")

        self.good_reception_layout.addWidget(self.label_title_good_reception)
        self.good_reception_layout.addWidget(self.label_error_title_good)
        self.good_reception_layout.addWidget(self.label_error_value_good)
        self.good_reception_layout.addWidget(self.label_blocked_title_good)
        self.good_reception_layout.addWidget(self.label_blocked_value_good)
        self.good_reception_layout.addWidget(self.label_points_percent_title_good)
        self.good_reception_layout.addWidget(self.label_points_percent_value_good)
        self.good_reception_layout.addWidget(self.label_total_title_good)
        self.good_reception_layout.addWidget(self.label_total_value_good)

        self.good_reception_labels.append(self.label_error_value_good)
        self.good_reception_labels.append(self.label_blocked_value_good)
        self.good_reception_labels.append(self.label_points_percent_value_good)
        self.good_reception_labels.append(self.label_total_value_good)

        self.label_title_bad_reception = QLabel("Dir. Pkt. nach schlechter Annhame (0, -, 1.Angriff)")
        self.label_error_title_bad = QLabel("Fhl: ")
        self.label_error_title_bad.setContentsMargins(30, 0, 0, 0)
        self.label_error_value_bad = QLabel(".")
        self.label_blocked_title_bad = QLabel("Blo: ")
        self.label_blocked_title_bad.setContentsMargins(30, 0, 0, 0)
        self.label_blocked_value_bad = QLabel(".")
        self.label_points_percent_title_bad = QLabel("Pkt%: ")
        self.label_points_percent_title_bad.setContentsMargins(30, 0, 0, 0)
        self.label_points_percent_value_bad = QLabel(".")
        self.label_total_title_bad = QLabel("Ges. : ")
        self.label_total_title_bad.setContentsMargins(30, 0, 0, 0)
        self.label_total_value_bad = QLabel(".")

        self.bad_reception_layout.addWidget(self.label_title_bad_reception)
        self.bad_reception_layout.addWidget(self.label_error_title_bad)
        self.bad_reception_layout.addWidget(self.label_error_value_bad)
        self.bad_reception_layout.addWidget(self.label_blocked_title_bad)
        self.bad_reception_layout.addWidget(self.label_blocked_value_bad)
        self.bad_reception_layout.addWidget(self.label_points_percent_title_bad)
        self.bad_reception_layout.addWidget(self.label_points_percent_value_bad)
        self.bad_reception_layout.addWidget(self.label_total_title_bad)
        self.bad_reception_layout.addWidget(self.label_total_value_bad)


        self.bad_reception_labels.append(self.label_error_value_bad)
        self.bad_reception_labels.append(self.label_blocked_value_bad)
        self.bad_reception_labels.append(self.label_points_percent_value_bad)
        self.bad_reception_labels.append(self.label_total_value_bad)


        self.defense_label_title = QLabel("Dir. Pkt. nach Abwehr")
        self.defense_label_error_title = QLabel("Fhl: ")
        self.defense_label_error_title.setContentsMargins(30, 0, 0, 0)
        self.defense_label_error_value = QLabel(".")
        self.defense_label_blocked_title= QLabel("Blo: ")
        self.defense_label_blocked_value = QLabel(".")
        self.defense_label_points_percent_title = QLabel("Pkt%: ")
        self.defense_label_points_percent_value = QLabel(".")
        self.defense_label_total_title = QLabel("Ges. : ")
        self.defense_label_total_value= QLabel(".")



        self.defense_reception_layout.addWidget(self.defense_label_title)
        self.defense_reception_layout.addWidget(self.defense_label_error_title)
        self.defense_reception_layout.addWidget(self.defense_label_error_value)
        self.defense_reception_layout.addWidget(self.defense_label_blocked_title)
        self.defense_reception_layout.addWidget(self.defense_label_blocked_value)
        self.defense_reception_layout.addWidget(self.defense_label_points_percent_title)
        self.defense_reception_layout.addWidget(self.defense_label_points_percent_value)
        self.defense_reception_layout.addWidget(self.defense_label_total_title)
        self.defense_reception_layout.addWidget(self.defense_label_total_value)

        self.defense_labels.append(self.defense_label_error_value)
        self.defense_labels.append(self.defense_label_blocked_value)
        self.defense_labels.append(self.defense_label_points_percent_value)
        self.defense_labels.append(self.defense_label_total_value)

        self.good_reception_layout.addStretch()

        self.reception_attack_layout.addLayout(self.good_reception_layout)
        self.reception_attack_layout.addLayout(self.bad_reception_layout)
        self.reception_attack_layout.addLayout(self.defense_reception_layout)

        return self.reception_attack_layout










class StatisticFrame(QWidget):
    def __init__(self):
        super().__init__()

        playernames = ["1", "2", "3", "4", "5", "6"]

        self.player_frame = PlayerFrame(playernames)
        self.header = self.player_frame.create_header()
        self.header.setStyleSheet("padding-bottom: 0px;")
        self.body = self.player_frame.create_body(self.player_frame.player_numbers)
        self.header.setStyleSheet("padding-bottom: 0px;")
        self.set_stats = self.player_frame.create_stats_sets()
        self.set_stats.setStyleSheet("padding-bottom: 0px;")

        self.current_set = QGroupBox("")
        self.current_set.setStyleSheet("border: 0px solid black; padding: 0px ")

        #self.current_set_layout = QGridLayout()
        self.current_set_layout = QVBoxLayout()
        self.current_set_layout.setSpacing(0)
        self.current_set_layout.addWidget(self.header)
        self.current_set_layout.addWidget(self.body)
        self.current_set_layout.addWidget(self.set_stats)
        #self.current_set_layout.addWidget(self.header, 0, 0, 1, 2)
        #self.current_set_layout.addWidget(self.body, 1, 0, 14, 2)
        self.current_set.setLayout(self.current_set_layout)
        #self.current_set.layout().setContentsMargins(0, 0, 0, 0)


        self.current_game = QGroupBox("Aktuelles Spiel")
        self.current_game_layout = QGridLayout()

        self.game_stats = GameStats()
        self.points_reception_defense = self.game_stats.create_reception_attack_frame()
        self.rotation_window = self.game_stats.create_rotation_points()
        self.rece_window = self.game_stats.create_serv_rece_points("Annahmen", "SO-Punkte", "Ann", "Punkt")
        self.serv_window = self.game_stats.create_serv_rece_points("Aufschlag", "BP", "Auf", "BP")
        self.current_game_layout.addLayout(self.rotation_window[0], 0, 0, 1, 2)
        self.current_game_layout.addLayout(self.rece_window[0], 0, 2, 1, 2)
        self.current_game_layout.addLayout(self.serv_window[0], 0, 4, 1, 2)
        self.current_game_layout.addLayout(self.points_reception_defense, 1, 0, 1, 2)

        self.current_game.setLayout(self.current_game_layout)

    def update_player_frame(self, players_numbers_list):
        self.body = self.player_frame.create_body(players_numbers_list)




