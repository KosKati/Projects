from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel


class StatHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.label_player = QLabel("Spielsituation")
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

class StatHeaderRotaion(QWidget):
    def __init__(self):
        super().__init__()

        self.label_pass = QLabel("Pass")
        self.label_pass_two = QLabel("2")
        self.label_pass_three = QLabel("3")
        self.label_pass_four = QLabel("4")
        self.label_pass_one = QLabel("1")
        self.label_pass_six = QLabel("6")
        self.label_place = QLabel("")

        self.set_rotation_header = QHBoxLayout()
        self.set_rotation_header.addWidget(self.label_pass)
        self.set_rotation_header.addWidget(self.label_pass_two)
        self.set_rotation_header.addWidget(self.label_pass_three)
        self.set_rotation_header.addWidget(self.label_pass_four)
        self.set_rotation_header.addWidget(self.label_pass_one)
        self.set_rotation_header.addWidget(self.label_pass_six )
        self.set_rotation_header.addWidget(self.label_place)

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


class GameStatsFrame(QWidget):
    def __init__(self, set):
        super().__init__()
        self.set = set
        self. header = StatHeader()
        self.player1 = StatLine("K0")
        self.player2 = StatLine("K1")
        self.player3 = StatLine("K2")
        self.header_line = self.header.set_serv_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header

        self.box_set_game = QGroupBox(set)
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)

        self.box_set_game.setLayout(self.layout_stat)

class RotationStatsFrame(QWidget):
    def __init__(self, rotation):
        super().__init__()
        self.rotation = rotation
        self.header = StatHeaderRotaion()
        self.player1 = StatLine("K1")
        self.player2 = StatLine("K2")
        self.player3 = StatLine("K3")
        self.header_line = self.header.set_rotation_header
        self.player1_line = self.player1.set_serv_header
        self.player2_line = self.player2.set_serv_header
        self.player3_line = self.player3.set_serv_header

        self.box_rotation_game = QGroupBox(rotation)
        self.layout_stat = QVBoxLayout()
        self.layout_stat.addLayout(self.header_line)
        self.layout_stat.addLayout(self.player1_line)
        self.layout_stat.addLayout(self.player2_line)
        self.layout_stat.addLayout(self.player3_line)

        self.box_rotation_game.setLayout(self.layout_stat)


class AllStatsFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.set1_stat_frame = GameStatsFrame("set1")
        self.set1_stat = self.set1_stat_frame.box_set_game

        self.set2_stat_frame = GameStatsFrame("set2")
        self.set2_stat = self.set2_stat_frame.box_set_game

        self.set3_stat_frame = GameStatsFrame("set3")
        self.set3_stat = self.set3_stat_frame.box_set_game

        self.set4_stat_frame = GameStatsFrame("set4")
        self.set4_stat = self.set4_stat_frame.box_set_game

        self.set5_stat_frame = GameStatsFrame("set5")
        self.set5_stat = self.set5_stat_frame.box_set_game

        self.game_stat_frame = GameStatsFrame("Gesamt")
        self.game_stat = self.game_stat_frame.box_set_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 1")
        self.game_rotation_1 = self.game_rotation_frame.box_rotation_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 6")
        self.game_rotation_6 = self.game_rotation_frame.box_rotation_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 5")
        self.game_rotation_5 = self.game_rotation_frame.box_rotation_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 4")
        self.game_rotation_4 = self.game_rotation_frame.box_rotation_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 3")
        self.game_rotation_3 = self.game_rotation_frame.box_rotation_game

        self.game_rotation_frame = RotationStatsFrame("Läufer 2")
        self.game_rotation_2 = self.game_rotation_frame.box_rotation_game


