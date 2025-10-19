from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,QGroupBox


class GameButtons(QWidget) :
    def __init__(self):
        super().__init__()

        self.game_team_btns = QVBoxLayout()
        self.new_game_Btn = QPushButton("Neues Spiel")
        self.loadBtn = QPushButton("Spiel laden")
        self.newTeamBtn = QPushButton("Neue Mannschaft")
        self.loadTeamBtn = QPushButton("Mannschaft laden")
        self.addPlayerBtn = QPushButton("Spieler hinzufügen")
    
        self.gameButtonBox = QHBoxLayout()
        self.teamButtonBox = QHBoxLayout()

        self.gameButtonBox.addWidget(self.new_game_Btn)
        self.gameButtonBox.addWidget(self.loadBtn )
        self.teamButtonBox.addWidget(self.newTeamBtn)
        self.teamButtonBox.addWidget(self.loadTeamBtn)
        self.teamButtonBox.addWidget(self.addPlayerBtn)

        self.game_team_btns.addLayout(self.gameButtonBox)
        self.game_team_btns.addLayout(self.teamButtonBox)

        self.options_groupbox = QGroupBox()
        self.options_groupbox.setLayout(self.game_team_btns)