from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QGroupBox, QFrame, QLineEdit, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
import sys
 
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        #self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt Media Player")
        self.setWindowIcon(QIcon('player.ico'))

        self.frame = QFrame
 
 
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
 
 
        #slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
 
 
 
 
 
        self.hbox = QHBoxLayout()
 
        self.hbox.addWidget(self.openBtn)
        self.hbox.addWidget(self.playBtn)
        self.hbox.addWidget(self.slider)
 
 
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
        self.mediaplayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.durationChanged.connect(self.duration_changed)
 
 
    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.mediaplayer.setSource(QUrl.fromLocalFile(filename))
            self.playBtn.setEnabled(True)
 
    def play_video(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()
 
        else:
            self.mediaplayer.play()
 
 
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
 
#app = QApplication(sys.argv)
#window = Window()
#window.show()
#sys.exit(app.exec())