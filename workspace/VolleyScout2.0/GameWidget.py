from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,QGroupBox
from NewGameWindow import NewGameWindow
from NewTeamWindow import NewTeamWindow
from SetLineUpWindow import SetLineUp
from LoadTeamWindow import ImportWindow

class GameButtons(QWidget) :
    #Änerung 2 def __init__(self, player_labels, court_players, players_frame, current_set_layout, old_body):
    def __init__(self, court, statistic_frame) :
        super().__init__()
        self.old_body = statistic_frame.body
        self.current_set_layout = statistic_frame.current_set_layout
        self.players_frame = statistic_frame.player_frame
        self.player_labels = court.left_players_labels
        self.court_players = court.labels_court
        """
        self.old_body = old_body
        self.current_set_layout = current_set_layout
        self.players_frame = players_frame
        self.player_labels = player_labels
        self.court_players = court_players
        """
        self.game_team_btns = QVBoxLayout()
        self.new_game_Btn = QPushButton("Neues Spiel")
        self.loadBtn = QPushButton("Spiel laden")
        self.newTeamBtn = QPushButton("Neue Mannschaft")
        self.loadTeamBtn = QPushButton("Mannschaft laden")
        self.line_up_Btn = QPushButton("Startaufstelung eingeben")
    
        self.gameButtonBox = QHBoxLayout()
        self.teamButtonBox = QHBoxLayout()

        self.gameButtonBox.addWidget(self.new_game_Btn)
        self.gameButtonBox.addWidget(self.loadBtn)
        self.teamButtonBox.addWidget(self.newTeamBtn)
        self.teamButtonBox.addWidget(self.loadTeamBtn)
        self.teamButtonBox.addWidget(self.line_up_Btn)

        self.game_team_btns.addLayout(self.gameButtonBox)
        self.game_team_btns.addLayout(self.teamButtonBox)

        self.options_groupbox = QGroupBox()
        self.options_groupbox.setLayout(self.game_team_btns)

        self.new_game_Btn.clicked.connect(self.show_new_game_window)
        self.newTeamBtn.clicked.connect(self.show_new_team_window)
        self.loadBtn.clicked.connect(self.load_team)
        self.loadTeamBtn.clicked.connect(self.load_team)
        self.line_up_Btn.clicked.connect(self.set_line_up)


    def set_line_up(self):
        self.line_up = SetLineUp(self.court_players)
        self.line_up.show()

    def load_game(self):
        pass

    def load_team(self):
        self.team = ImportWindow()
        self.team.show()

    def show_new_game_window(self):
        self.new_gameWindow = NewGameWindow(self.player_labels, self.players_frame, self.current_set_layout, self.old_body)
        self.new_gameWindow.show()

    def show_new_team_window(self):
        self.new_teamWindow = NewTeamWindow()
        self.new_teamWindow.show()