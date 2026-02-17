from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QGroupBox, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton, \
    QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt
#from MediaPlayer import Window
#from MediaPlayer import Window
from GameWidget import GameButtons
from Court import CourtWidgets
from StatisticFrames import StatisticFrame
from ActualGame import ActualGame
from icecream import ic
import os
import sys
import vlc


class StatsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.left_layout = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)

        self.statistic_frame = StatisticFrame()
        self.statistic_frame_players = self.statistic_frame.current_set
        self.statistic_frame_game = self.statistic_frame.current_game

        self.court = CourtWidgets(self.statistic_frame.player_frame)

        self.game_btn = GameButtons(self.court, self.statistic_frame)

        self.actual_game = ActualGame()
        self.actual_game_box = self.actual_game.box_teams
        self.left_side = self.court.left_side
        self.team_labels = self.court.team_window
        self.left_side_layout = QGridLayout()
        self.label_court_img = QLabel()
        self.label_court_img.setScaledContents(True)
        palette = QPalette()
        self.pixmap = QPixmap("Pics/Volleyball_Half_Court.png")
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self.pixmap))
        #self.left_side.setPalette(palette)
        #self.left_side.setAutoFillBackground(True)

        self.label = QLabel("")
        self.label.setStyleSheet("background-color: #0eadb0")

        self.label2 = QLabel("")
        self.label2.setStyleSheet("background-color: #0eadb0")
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")

        self.game_btn_box = self.game_btn.options_groupbox

        #self.parentLayout.addWidget(self.label)
        self.left_layout.addWidget(self.actual_game_box)
        self.left_layout.addWidget(self.label_court_img)
        self.left_layout.addWidget(self.left_side)
        self.left_layout.addWidget(self.team_labels)
        self.left_layout.addWidget(self.game_btn_box)
        #self.parentLayout.addWidget(self.label2)
        self.right_layout.addWidget(self.statistic_frame_players)
        self.right_layout.addWidget(self.statistic_frame_game)

        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)

        self.setLayout(self.layout)
