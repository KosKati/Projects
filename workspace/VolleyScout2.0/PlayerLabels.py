from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QGroupBox, QFrame, QLineEdit, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
import sys

class NewTeamWidgets(QWidget):
    def __init__(self):
        super().__init__()

        
        self.label_player_0 = QLabel("")
        self.label_player_1 = QLabel("Spieler 1")
        self.label_player_2 = QLabel("Spieler 2")
        self.label_player_3 = QLabel("Spieler 3")
        self.label_player_4 = QLabel("Spieler 4")
        self.label_player_5 = QLabel("Spieler 5")
        self.label_player_6 = QLabel("Spieler 6")
        self.label_player_7 = QLabel("Spieler 7")
        self.label_player_8 = QLabel("Spieler 8")
        self.label_player_9 = QLabel("Spieler 9")
        self.label_player_10 = QLabel("Spieler 10")
        self.label_player_11 = QLabel("Spieler 11")
        self.label_player_12 = QLabel("Spieler 12")
        self.label_player_13 = QLabel("Spieler 13")
        self.label_player_14 = QLabel("Spieler 14")

        self.player_labels = [self.label_player_0,self.label_player_1,self.label_player_2,self.label_player_3, \
                              self.label_player_4,self.label_player_5,self.label_player_6,self.label_player_7, \
                              self.label_player_8,self.label_player_9,self.label_player_10,self.label_player_11,\
                              self.label_player_12,self.label_player_13,self.label_player_14 ]

        
        self.line_edit_number_player_0 = QLabel("Nummer")
        self.line_edit_number_player_1 = QLineEdit()
        self.line_edit_number_player_2 = QLineEdit()
        self.line_edit_number_player_3 = QLineEdit()
        self.line_edit_number_player_4 = QLineEdit()
        self.line_edit_number_player_5 = QLineEdit()
        self.line_edit_number_player_6 = QLineEdit()
        self.line_edit_number_player_7 = QLineEdit()
        self.line_edit_number_player_8 = QLineEdit()
        self.line_edit_number_player_9 = QLineEdit()
        self.line_edit_number_player_10 = QLineEdit()
        self.line_edit_number_player_11 = QLineEdit()
        self.line_edit_number_player_12 = QLineEdit()
        self.line_edit_number_player_13 = QLineEdit()
        self.line_edit_number_player_14 = QLineEdit()

        self.label_edit_numbers = [self.line_edit_number_player_0,self.line_edit_number_player_1,self.line_edit_number_player_2,self.line_edit_number_player_3, \
                              self.line_edit_number_player_4,self.line_edit_number_player_5,self.line_edit_number_player_6,self.line_edit_number_player_7, \
                              self.line_edit_number_player_8,self.line_edit_number_player_9,self.line_edit_number_player_10,self.line_edit_number_player_11,\
                              self.line_edit_number_player_12,self.line_edit_number_player_13,self.line_edit_number_player_14 ]

        
        self.line_edit_name_player_0 = QLabel("Name")
        self.line_edit_name_player_1 = QLineEdit()
        self.line_edit_name_player_2 = QLineEdit()
        self.line_edit_name_player_3 = QLineEdit()
        self.line_edit_name_player_4 = QLineEdit()
        self.line_edit_name_player_5 = QLineEdit()
        self.line_edit_name_player_6 = QLineEdit()
        self.line_edit_name_player_7 = QLineEdit()
        self.line_edit_name_player_8 = QLineEdit()
        self.line_edit_name_player_9 = QLineEdit()
        self.line_edit_name_player_10 = QLineEdit()
        self.line_edit_name_player_11 = QLineEdit()
        self.line_edit_name_player_12 = QLineEdit()
        self.line_edit_name_player_13 = QLineEdit()
        self.line_edit_name_player_14 = QLineEdit()

        self.label_edit_names = [self.line_edit_name_player_0,self.line_edit_name_player_1,self.line_edit_name_player_2,self.line_edit_name_player_3, \
                              self.line_edit_name_player_4,self.line_edit_name_player_5,self.line_edit_name_player_6,self.line_edit_name_player_7, \
                              self.line_edit_name_player_8,self.line_edit_name_player_9,self.line_edit_name_player_10,self.line_edit_name_player_11,\
                              self.line_edit_name_player_12,self.line_edit_name_player_13,self.line_edit_name_player_14 ]

        self.layout_player0 = QHBoxLayout()
        self.layout_player1 = QHBoxLayout()
        self.layout_player2 = QHBoxLayout()
        self.layout_player3 = QHBoxLayout()
        self.layout_player4 = QHBoxLayout()
        self.layout_player5 = QHBoxLayout()
        self.layout_player6 = QHBoxLayout()
        self.layout_player7 = QHBoxLayout()
        self.layout_player8 = QHBoxLayout()
        self.layout_player9 = QHBoxLayout()
        self.layout_player10 = QHBoxLayout()
        self.layout_player11 = QHBoxLayout()
        self.layout_player12 = QHBoxLayout()
        self.layout_player13 = QHBoxLayout()
        self.layout_player14 = QHBoxLayout()

        self.line_players = [self.layout_player0,self.layout_player1,self.layout_player2,self.layout_player3,self.layout_player4, \
                             self.layout_player5,self.layout_player6,self.layout_player7,self.layout_player8, \
                             self.layout_player9,self.layout_player10,self.layout_player11,self.layout_player12, \
                             self.layout_player13,self.layout_player14]
        
        self.layout_names = QVBoxLayout()
        self.layout_window = QVBoxLayout()

        self.team_name = QLabel("Mannschaftsname:")
        self.team_name_edit = QLineEdit()

        self.layout_newTeam = QHBoxLayout()
        self.layout_newTeam.addWidget(self.team_name)
        self.layout_newTeam.addWidget(self.team_name_edit)

        self.layout_window.addLayout(self.layout_newTeam)

        for layout_player, label in zip(self.line_players,self.player_labels) :
                layout_player.addWidget(label)

        for layout_player, label in zip(self.line_players,self.label_edit_numbers) :
                layout_player.addWidget(label)
        
        for layout_player, label in zip(self.line_players,self.label_edit_names) :
                layout_player.addWidget(label)

        for layout_player in self.line_players:
            self.layout_window.addLayout(layout_player)
        
        self.save_Button = QPushButton("Mannschaft speichern")
        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.save_Button)
        self.layout_button.addWidget(QLabel(""))
        self.layout_window.addLayout(self.layout_button)
        

        
        self.layout_window.addLayout(self.layout_names)