from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QGroupBox, QFrame, QLineEdit, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
import sys
from PlayerLabels import NewTeamWidgets


class NewTeamWindow(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setGeometry(200,200, 300, 500)
        final_window = NewTeamWidgets()
        self.final_layout = final_window.layout_window

        self.setLayout(self.final_layout)
app = QApplication(sys.argv)
window = NewTeamWindow()
window.show()
app.exec()