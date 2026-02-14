from functools import partial
import re

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QGroupBox, QFrame, QLineEdit, QLabel, QMessageBox
from PyQt6.QtGui import QIcon, QKeyEvent
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl, QEvent, QObject
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtMultimediaWidgets import QVideoWidget
from icecream import ic

from Updates import Update
import os.path
from pathlib import Path
from UpdatePlayers import PlayersUpdate
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy import *
 



class ModifiedLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent, media_player):
        super().__init__(parent)
        self.media_player = media_player
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(QLineEdit, self).keyPressEvent(event)
        if event.key() == Qt.Key.Key_O:
            print("Tab Key pressed")

        if event.key() == Qt.Key.Key_I:
            print("Space Key pressed")

        if event.key() == Qt.Key.Key_P:
            print("Return Key pressed")


    """ 

class ModifiedLineEdit(QLineEdit):
    def __init__(self,parent, media_player):
        QLineEdit.__init__(self, parent)
        self.mediaplayer = media_player
        self.textChanged.connect(self.keyPressEvent)


    def keyPressEvent(self, e):
        if e[-1] == Qt.Key.Key_O:
            print("1")
            self.go_five_forward()

        if e.key() == Qt.Key.Key_I:
            print("2")
            self.go_five_backward()

        if e.key() == Qt.Key.Key_P:
            print("3")
            self.play_or_pause()

       def keyPressEvent(self, event):
        super(QLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Tab:
            print("Tab Key pressed")

        if event.key() == QtCore.Qt.Key_Space:
            print("Space Key pressed")

        if event.key() == QtCore.Qt.Key_Return:
            print("Return Key pressed")
    
    
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_O:
            print("1")
            self.go_five_forward()

        if e.key() == Qt.Key.Key_I:
            print("2")
            self.go_five_backward()

        if e.key() == Qt.Key.Key_P:
            print("3")
            self.play_or_pause()


    def play_or_pause(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()

        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PausedState:
            self.mediaplayer.play()



    def go_five_forward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() + 9000)

    def go_five_backward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() - 9000)
    """
class CustomLineEdit(QLineEdit):
    def __init__(self, media_player):
        super().__init__()

        self.media_player = media_player
    def keyPressEvent(self, event):

        # Beispiel: Prüfen, ob die Eingabetaste (Enter) gedrückt wurde
        if event.key() == Qt.Key.Key_O:
            self.go_five_forward()

        if event.key() == Qt.Key.Key_P:
            ic()
            self.play_or_pause()

        if event.key() == Qt.Key.Key_I:
            self.go_five_backward()


        # WICHTIG: Basis-Implementierung aufrufen, damit man weiterhin tippen kann
        super().keyPressEvent(event)

    def go_five_forward(self):
        self.media_player.setPosition(self.media_player.position() + 9000)

    def go_five_backward(self):
        self.media_player.setPosition(self.media_player.position() - 9000)

    def play_or_pause(self):
        ic()
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            ic()
            self.media_player.pause()
        else:
            self.media_player.play()



class VideoWindow(QWidget):
    def __init__(self, video_widget,label_console, console_line, player_groupbox, media_player):
        super().__init__()
        self.mediaplayer = media_player
        self.resize(800, 600)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(video_widget, stretch=3)
        self.layout_console = QHBoxLayout()
        self.console_widget = console_line
        self.console_widget.textChanged.connect(self.check_last_char)
        self.layout_console.addWidget(label_console)
        self.layout_console.addWidget(self.console_widget)
        self.layout_console.addLayout(player_groupbox)
        self.layout.addLayout(self.layout_console)
        self.setLayout(self.layout)

        self.video_widget = video_widget
        self.label_console = label_console

        #self.filter = EventFilter()
       # self.console_widget.installEventFilter(self.filter)

    def check_last_char(self):
        if self.console_widget.text():
            string = self.console_widget.text()
            if string[-1] in ["i", "o", "p"]:
                string = string[:-1]
                self.console_widget.setText(string)







    def go_five_forward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() + 9000)




class ConsoleWindow(QWidget):
    def __init__(self, label_console, console_widget):
        super().__init__()
        self.resize(400, 100)
        self.layout = QHBoxLayout()
        self.layout.addWidget(label_console)
        self.layout.addWidget(console_widget)
        self.setLayout(self.layout)

 
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
        #self.vbox.addLayout(self.hbox)
 
        self.linebox = QHBoxLayout()
        #self.comline = QLineEdit()



        self.labelcom = QLabel("Eingaben: ")
        self.linebox.addWidget(self.labelcom)
        #self.linebox.addWidget(self.comline)



        self.setLayout(self.vbox)

        self.person_groupbox = QGroupBox('The buttons')
        self.person_groupbox.setLayout(self.vbox)

        self.input_groupbox = QGroupBox()
        #self.input_groupbox.setLayout(self.linebox)

        #self.console_window = ConsoleWindow(self.labelcom, self.comline)
        #self.console_window.show()
 
        self.mediaplayer.setVideoOutput(self.videowidget)
        #self.mediaplayer.setAudioOutput(self.audio)

        self.videowidget2 = QVideoWidget()
        self.mediaplayer.setVideoOutput(self.videowidget2)
        self.comline = CustomLineEdit(self.mediaplayer)
        #self.comline = ModifiedLineEdit(self, self.mediaplayer)
        self.second_window = VideoWindow(self.videowidget2,self.labelcom, self.comline,self.hbox, self.mediaplayer)
        self.second_window.show()
 
        #media player signals
        self.plus_five.clicked.connect(self.go_five_forward)
        self.minus_five.clicked.connect(self.go_five_backward)
        self.mediaplayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.positionChanged.connect(self.update_position)
        self.mediaplayer.durationChanged.connect(self.duration_changed)

        #lineedit signals
        self.comline.returnPressed.connect(partial(self.execute_input,self.statistic_frame))

        ic()
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