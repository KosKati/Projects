from functools import partial
import re

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QGroupBox, QFrame, QLineEdit, QLabel, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
from Updates import Update
import os.path
from pathlib import Path
from UpdatePlayers import PlayersUpdate
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy import *
 
 
 
class Window(QWidget):
    def __init__(self, statistic_frame):
        super().__init__()

        self.statistic_frame = statistic_frame
 
        #self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt Media Player")
        self.setWindowIcon(QIcon('player.ico'))

        self.frame = QFrame

        self.file_name = None

 
 
        self.mediaplayer = QMediaPlayer()
        self.audio = QAudioOutput()
 
        self.videowidget = QVideoWidget()
 
 
        #btn for opening
        self.openBtn = QPushButton("Open Video")
        self.openBtn.clicked.connect(self.open_video)
 
 
        #btn for palying
        self.playBtn = QPushButton()

        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # btn for pause
        self.pauseBtn = QPushButton("Pause")
        self.pauseBtn.clicked.connect(self.pause_video)
        self.clip = (VideoFileClip)

        #slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)

        #btn forward/backward
        self.plus_five = QPushButton("+5")
        self.minus_five = QPushButton("-5")

        self.label_time = QLabel("0")
 
 
 
 
 
        self.hbox = QHBoxLayout()
 
        self.hbox.addWidget(self.openBtn)
        self.hbox.addWidget(self.playBtn)
        self.hbox.addWidget(self.pauseBtn)
        self.hbox.addWidget(self.plus_five)
        self.hbox.addWidget(self.minus_five)
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.label_time)

 
 
        self.vbox = QHBoxLayout()
 
        self.vbox.addWidget(self.videowidget)
        self.vbox.addLayout(self.hbox)
 
        self.linebox = QHBoxLayout()
        self.comline = QLineEdit()

        self.labelcom = QLabel("Eingaben: ")
        self.linebox.addWidget(self.labelcom)
        self.linebox.addWidget(self.comline)



        self.setLayout(self.vbox)

        self.person_groupbox = QGroupBox('The buttons')
        self.person_groupbox.setLayout(self.vbox)

        self.input_groupbox = QGroupBox()
        self.input_groupbox.setLayout(self.linebox)

 
        self.mediaplayer.setVideoOutput(self.videowidget)
        self.mediaplayer.setAudioOutput(self.audio)
 
 
        #media player signals
        self.plus_five.clicked.connect(self.go_five_forward)
        self.minus_five.clicked.connect(self.go_five_backward)
        self.mediaplayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.positionChanged.connect(self.update_position)
        self.mediaplayer.durationChanged.connect(self.duration_changed)

        #lineedit signals
        self.comline.returnPressed.connect(partial(self.execute_input,self.statistic_frame))

    def hhmmss(self,ms):
        # s = 1000
        # m = 60000
        # h = 3600000
        s = round(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

    def update_position(self, position):
        if position >= 0:
            self.label_time.setText(self.hhmmss(self.mediaplayer.position()))

        self.slider.blockSignals(True)
        self.slider.setValue(position)
        self.slider.blockSignals(False)

    def go_five_forward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() + 9000)

    def go_five_backward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() - 9000)

    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.file_name = filename

            self.mediaplayer.setSource(QUrl.fromLocalFile(filename))
            self.playBtn.setEnabled(True)
 
    def play_video(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()
 
        else:
            self.mediaplayer.play()
 

    def pause_video(self):
        self.mediaplayer.pause()


    def mediastate_changed(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )
 
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )
 
 
 
    def position_changed(self, position):
        self.slider.setValue(position)
 
 
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
 
 
    def set_position(self,position):
        self.mediaplayer.setPosition(position)

    def execute_input(self, statistic_frame):
        f = open("./Data/Database_name.txt")
        database_name = f.read()
        sets = ["Satz 1", "Satz 2", "Satz 3", "Satz 4", "Satz 5"]
        if self.comline.text() in sets:
            self.set_set(self.comline.text())
        else:
            formated_command = self.comline.text().replace(" ", "")
            commands = formated_command.split(",")

            if self.bool_match(commands):

                for command in commands:
                    players_update = PlayersUpdate(command,statistic_frame,str(int(self.mediaplayer.position()/1000)), database_name)
                    players_update.start()

        self.comline.clear()

    def set_set(self, current_set : str):
        with open("./Data/Current_Set.txt", "w") as f:  # in write mode
            f.write(current_set )

    def bool_match(self, commands):
        for t in commands:
            if re.fullmatch(r"(\d\d?[SRBDAZ]([+0-]|(--)|(\+\+))((\(.*)?(:)?(.*\)))?)|\d\d?AB((\(.*)?(:)?(.*\)))?", t) is None:
                print("Fehler bei:" + t)
                return False
                break

        return True



#app = QApplication(sys.argv)
#window = Window()
#window.show()
#sys.exit(app.exec())