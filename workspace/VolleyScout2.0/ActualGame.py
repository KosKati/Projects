from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel

class ActualGame(QWidget):
    def __init__(self):
        super().__init__()


        self.box_teams = QGroupBox("Aktuelles Spiel")
        self.layout_stat = QVBoxLayout()
        self.labelTeam = QLabel("Zu analysierendes Team:")
        self.labelAnalyseTeam = QLabel("")
        self.labelOpponend = QLabel("Gegner")
        self.labelOpponendTeam = QLabel("")
        self.layout_stat.addWidget(self.labelTeam)
        self.layout_stat.addWidget(self.labelAnalyseTeam)
        self.layout_stat.addWidget(self.labelOpponend)
        self.layout_stat.addWidget(self.labelOpponendTeam)

        self.box_teams.setLayout(self.layout_stat)
