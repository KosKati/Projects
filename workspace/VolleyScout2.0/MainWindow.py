from PyQt6.QtWidgets import QApplication, QGroupBox, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
#from MediaPlayer import Window
from MediaPlayer import Window
from GameWidget import GameButtons
from Court import CourtWidgets
from StatisticFrames import StatisticFrame
from ActualGame import ActualGame


app = QApplication([])

window = QMainWindow()
parentLayout = QGridLayout()
videoplayer = Window()
gameBtns = GameButtons()
court = CourtWidgets()
actual_game = ActualGame()
actual_game_box = actual_game.box_teams

left_side = court.left_side
team_labels = court.team_window
statistic_frame = StatisticFrame()
statistic_frame_players = statistic_frame.current_set
statistic_frame_game = statistic_frame.current_game

left_side_layout = QGridLayout()
label_court_img = QLabel()
label_court_img.setScaledContents(True)
pixmap = QPixmap( "Pics/Volleyball_Half_Court.png")
label_court_img.setPixmap(pixmap)

label = QLabel("")
label.setStyleSheet("background-color: #0eadb0")


label2 = QLabel("")
label2.setStyleSheet("background-color: #0eadb0" )
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")

game_btn = gameBtns.options_groupbox
open_btn = videoplayer.person_groupbox
play_ptn = videoplayer.playBtn
video = videoplayer.videowidget
input = videoplayer.input_groupbox

parentLayout.addWidget(label, 0, 0, 10,4)
parentLayout.addWidget(actual_game_box, 0, 0, 3,4)
parentLayout.addWidget(label_court_img, 3, 0, 4,4)
parentLayout.addWidget(left_side,3,0,4,4)
parentLayout.addWidget(team_labels,7,0,3,4)
parentLayout.addWidget(game_btn, 10, 0, 1,4)

parentLayout.addWidget(video, 0,4, 10,8)
parentLayout.addWidget(input, 10, 4, 1,8)
parentLayout.addWidget(open_btn, 11,4, 1,8)
parentLayout.addWidget(label2, 0, 13, 12,8)
parentLayout.addWidget(statistic_frame_players, 0, 13, 6,8)
parentLayout.addWidget(statistic_frame_game, 6, 13, 6,8)


centerWidget = QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.showMaximized()

app.exec()

