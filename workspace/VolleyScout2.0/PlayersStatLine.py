from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel
from StatsGame import AllStatsFrame

class StatLine(QWidget):
    def __init__(self, playername,  parent=None):
        super(StatLine, self).__init__(parent)

        self.player_number = playername
        self.detail_button = QPushButton("Details")
        self.label_player = QLabel(self.player_number)
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


    def update_label(self, label_value, new_value):

        match label_value:
            case "++":
                self.label_doublePlus.setText(str(new_value))
            case "+":
                self.label_plus.setText(str(new_value))
            case "0":
                self.label_zero.setText(str(new_value))
            case "-":
                self.label_minus.setText(str(new_value))
            case "--":
                self.label_doubleMinus.setText(str(new_value))