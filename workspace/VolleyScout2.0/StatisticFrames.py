from symtable import Class

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel
from StatsGame import AllStatsFrame

class StatLine(QWidget):
    def __init__(self, playername,  parent=None):
        super(StatLine, self).__init__(parent)

        self.playername = playername
        self.detail_button = QPushButton("Details")
        self.label_player = QLabel(self.playername)
        self.label_doublePlus = QLabel("0/0 (0%)")
        self.label_plus = QLabel("0/0 (0%)")
        self.label_zero = QLabel("0/0 (0%)")
        self.label_minus = QLabel("0/0 (0%)")
        self.label_doubleMinus = QLabel("0/0 (0%)")

        self.set_serv_header = QHBoxLayout()
        self.set_serv_header.addWidget(self.label_player)
        self.set_serv_header.addWidget(self.label_doublePlus)
        self.set_serv_header.addWidget(self.label_plus)
        self.set_serv_header.addWidget(self.label_zero)
        self.set_serv_header.addWidget(self.label_minus)
        self.set_serv_header.addWidget(self.label_doubleMinus)
        self.set_serv_header.addWidget(self.detail_button)


class StatHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.label_player = QLabel("Spieler")
        self.label_doublePlus = QLabel("++")
        self.label_plus = QLabel("+")
        self.label_zero = QLabel("0")
        self.label_minus = QLabel("-")
        self.label_doubleMinus = QLabel("--")
        self.label_place = QLabel("")


        self.set_serv_header = QHBoxLayout()
        self.set_serv_header.addWidget(self.label_player)
        self.set_serv_header.addWidget(self.label_doublePlus)
        self.set_serv_header.addWidget(self.label_plus)
        self.set_serv_header.addWidget(self.label_zero)
        self.set_serv_header.addWidget(self.label_minus)
        self.set_serv_header.addWidget(self.label_doubleMinus)
        self.set_serv_header.addWidget(self.label_place)



class ServiceFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.player5 = StatLine(self.playernames[4])
        self.player6 = StatLine(self.playernames[5])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header
        self.player5_line = self.player5.set_serv_header
        self.player6_line = self.player6.set_serv_header

        self.box_set_serv = QGroupBox("Aufschlag")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)
        self.layout_stat.addLayout(self.player5_line)
        self.layout_stat.addLayout(self.player6_line)

        self.box_set_serv.setLayout(self.layout_stat)


class ReceptionFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.player5 = StatLine(self.playernames[4])
        self.player6 = StatLine(self.playernames[5])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header
        self.player5_line = self.player5.set_serv_header
        self.player6_line = self.player6.set_serv_header

        self.box_set_recep = QGroupBox("Annahme")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)
        self.layout_stat.addLayout(self.player5_line)
        self.layout_stat.addLayout(self.player6_line)

        self.box_set_recep.setLayout(self.layout_stat)



class AttackFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.player5 = StatLine(self.playernames[4])
        self.player6 = StatLine(self.playernames[5])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header
        self.player5_line = self.player5.set_serv_header
        self.player6_line = self.player6.set_serv_header

        self.box_set_attack = QGroupBox("Angriff")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)
        self.layout_stat.addLayout(self.player5_line)
        self.layout_stat.addLayout(self.player6_line)

        self.box_set_attack.setLayout(self.layout_stat)


class BlockFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.player5 = StatLine(self.playernames[4])
        self.player6 = StatLine(self.playernames[5])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header
        self.player5_line = self.player5.set_serv_header
        self.player6_line = self.player6.set_serv_header

        self.box_set_block = QGroupBox("Block")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)
        self.layout_stat.addLayout(self.player5_line)
        self.layout_stat.addLayout(self.player6_line)

        self.box_set_block.setLayout(self.layout_stat)


class DefenceFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.player5 = StatLine(self.playernames[4])
        self.player6 = StatLine(self.playernames[5])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header
        self.player5_line = self.player5.set_serv_header
        self.player6_line = self.player6.set_serv_header

        self.box_set_defence = QGroupBox("Verteidigung")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)
        self.layout_stat.addLayout(self.player5_line)
        self.layout_stat.addLayout(self.player6_line)

        self.box_set_defence.setLayout(self.layout_stat)


class SettingFrame(QWidget):
    def __init__(self, playernames):
        super().__init__()
        self.playernames = playernames
        self. header = StatHeader()
        self.player1 = StatLine(self.playernames[0])
        self.player2 = StatLine(self.playernames[1])
        self.player3 = StatLine(self.playernames[2])
        self.player4 = StatLine(self.playernames[3])
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header
        self.player4_line = self.player4.set_serv_header

        self.box_set_set = QGroupBox("Zuspiel")
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)
        self.layout_stat.addLayout(self.player4_line)

        self.box_set_set.setLayout(self.layout_stat)

class StatisticFrame(QWidget):
    def __init__(self):
        super().__init__()

        playernames = ["Herbert", "Carsten", "Keule", "Momo", "Bitch", "Whore"]
        service_stat_frame = ServiceFrame(playernames)
        service_stat = service_stat_frame.box_set_serv

        reception_stat_frame = ReceptionFrame(playernames)
        reception_stat = reception_stat_frame.box_set_recep

        attack_stat_frame = AttackFrame(playernames)
        self.attack_stat = attack_stat_frame.box_set_attack

        block_stat_frame = BlockFrame(playernames)
        block_stat = block_stat_frame.box_set_block

        defence_stat_frame = DefenceFrame(playernames)
        defence_stat = defence_stat_frame.box_set_defence

        setting_stat_frame = SettingFrame(playernames)
        setting_stat = setting_stat_frame.box_set_set

        self.current_set = QGroupBox("Aktuelle Spieler")
        self.current_set_layout = QGridLayout()
        self.current_set_layout.addWidget(service_stat, 0, 0, 1, 1)
        self.current_set_layout.addWidget(reception_stat, 0, 1, 1, 1)
        self.current_set_layout.addWidget(self.attack_stat, 0, 2, 1, 1)
        self.current_set_layout.addWidget(block_stat, 1, 0, 1, 1)
        self.current_set_layout.addWidget(defence_stat, 1, 1, 1, 1)
        self.current_set_layout.addWidget(setting_stat, 1, 2, 1, 1)
        self.current_set.setLayout(self.current_set_layout)


        self.current_game = QGroupBox("Aktuelles Spiel")
        self.current_game_layout = QGridLayout()
        self.all_stats = AllStatsFrame()

        self.rotation1_stat_layout = self.all_stats.game_rotation_1
        self.rotation6_stat_layout = self.all_stats.game_rotation_6
        self.rotation5_stat_layout = self.all_stats.game_rotation_5
        self.rotation4_stat_layout = self.all_stats.game_rotation_4
        self.rotation3_stat_layout = self.all_stats.game_rotation_3
        self.rotation2_stat_layout = self.all_stats.game_rotation_2

        self.set1_stats_layout = self.all_stats.set1_stat
        self.set2_stats_layout = self.all_stats.set2_stat
        self.set3_stats_layout = self.all_stats.set3_stat
        self.set4_stats_layout = self.all_stats.set4_stat
        self.set5_stats_layout = self.all_stats.set5_stat
        self.all_stats_layout = self.all_stats.game_stat
        self.current_game_layout.addWidget(self.set1_stats_layout, 0, 0, 1, 1)
        self.current_game_layout.addWidget(self.set2_stats_layout, 1, 0, 1, 1)
        self.current_game_layout.addWidget(self.set3_stats_layout, 2, 0, 1, 1)
        self.current_game_layout.addWidget(self.set4_stats_layout, 3, 0, 1, 1)
        self.current_game_layout.addWidget(self.set5_stats_layout, 4, 0, 1, 1)
        self.current_game_layout.addWidget(self.all_stats_layout, 5, 0, 1, 1)
        self.current_game_layout.addWidget(self.rotation1_stat_layout, 0, 1, 1, 1)
        self.current_game_layout.addWidget(self.rotation6_stat_layout, 1, 1, 1, 1)
        self.current_game_layout.addWidget(self.rotation5_stat_layout, 2, 1, 1, 1)
        self.current_game_layout.addWidget(self.rotation4_stat_layout, 3, 1, 1, 1)
        self.current_game_layout.addWidget(self.rotation3_stat_layout, 4, 1, 1, 1)
        self.current_game_layout.addWidget(self.rotation2_stat_layout, 5, 1, 1, 1)
        self.current_game.setLayout(self.current_game_layout)

    def get_attack_label(self):
        return self.attack_stat

