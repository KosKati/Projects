import sys
from functools import partial
import re
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
    QSlider, QWidget, QLineEdit, QMessageBox, QLabel
)
from PyQt6.QtCore import QTimer, Qt
import vlc
from icecream import ic
import DBFunctions
from UpdatePlayers import PlayersUpdate

from StatsWindow import StatsWindow

class CustomLineEdit(QLineEdit):
    def __init__(self, media_player):
        super().__init__()

        self.mediaplayer = media_player
    def keyPressEvent(self, event):

        # Beispiel: Prüfen, ob die Eingabetaste (Enter) gedrückt wurde
        if event.key() == Qt.Key.Key_O:
            ic()
            self.skip(5000)

        if event.key() == Qt.Key.Key_P:
            ic()
            self.play_or_pause()

        if event.key() == Qt.Key.Key_I:
            ic()
            self.skip(-5000)


        # WICHTIG: Basis-Implementierung aufrufen, damit man weiterhin tippen kann
        super().keyPressEvent(event)

    def skip(self, milliseconds):
        current_time = self.mediaplayer.get_time()
        total_time = self.mediaplayer.get_length()
        new_time = max(0, min(total_time, current_time + milliseconds))
        ic(int(new_time))
        self.mediaplayer.set_time(int(new_time))

    def skip_neg(self, milliseconds):
        current_time = self.mediaplayer.get_time()
        total_time = self.mediaplayer.get_length()
        new_time = max(0, min(total_time, current_time - milliseconds))
        ic(int(new_time))
        self.mediaplayer.set_time(int(new_time))

    def go_five_forward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() + 9000)

    def go_five_backward(self):
        self.mediaplayer.setPosition(self.mediaplayer.position() - 9000)

    def play_or_pause(self):
        ic()
        if self.mediaplayer.is_playing():
            ic()
            self.mediaplayer.set_pause(1)
        else:
            ic()
            self.mediaplayer.play()


class VideoPlayer(QMainWindow):
    def __init__(self,statistic_frame, court):
        super().__init__()
        self.setWindowTitle("PyQt6 VLC Media Player")
        self.setGeometry(100, 100, 1000, 800)
        self.statistic_frame = statistic_frame
        self.court = court
        self.filename = ""

        # Create a VLC instance and a media player.
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

        # Flag to detect if slider is being moved manually.
        self.slider_is_pressed = False

        # Set up the main widget and layout.
        self.widget = QFrame(self)
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        # Create the video frame where VLC will render the video.
        self.video_frame = QFrame()
        self.video_frame.setStyleSheet("background: black;")
        self.layout.addWidget(self.video_frame, stretch=3)

        # Create a horizontal layout for control buttons and progress slider.
        self.controls_layout = QHBoxLayout()
        self.layout.addLayout(self.controls_layout)

        # Open button: Open a video file.
        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_file)
        self.controls_layout.addWidget(self.open_button)

        # Pause button: Pause or resume video playback.
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_video)
        self.controls_layout.addWidget(self.pause_button)

        # Stop button: Stop video playback.
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)
        self.controls_layout.addWidget(self.stop_button)

        self.comline = CustomLineEdit(self.mediaplayer)
        self.comline.textChanged.connect(self.check_last_char)
        self.controls_layout.addWidget(self.comline)
        self.comline.returnPressed.connect(partial(self.execute_input, self.statistic_frame))

        # Progress slider: Display and control the playback progress.
        self.progress_slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_slider.setRange(0, 1000)
        # Connect slider events for manual movement.
        self.progress_slider.sliderPressed.connect(self.slider_pressed)
        self.progress_slider.sliderReleased.connect(self.slider_released)
        self.controls_layout.addWidget(self.progress_slider)

        self.label_time = QLabel("Test")
        self.controls_layout.addWidget(self.label_time)
        self.progress_slider.valueChanged.connect(self.update_position)

        #self.mediaplayer.positionChanged.connect(self.update_position)
        # Timer to update the slider based on the video's current position.
        self.timer = QTimer(self)
        self.timer.setInterval(100)  # Update every 100 milliseconds.
        self.timer.timeout.connect(self.update_ui)

    def set_videofile_path(self, file_path : str):
        with open("./Data/Videofile.txt", "w") as f:  # in write mode
            f.write(file_path )

    def check_last_char(self):
        if self.comline.text():
            string = self.comline.text()
            if string[-1] in ["i", "o", "p"]:
                string = string[:-1]
                self.comline.setText(string)

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
            self.label_time.setText(self.hhmmss(self.mediaplayer.get_time()))

        self.progress_slider.blockSignals(True)
        self.progress_slider.setValue(position)
        self.progress_slider.blockSignals(False)

    def open_file(self):
        # Open a file dialog to select a video file.
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if self.filename:
            media = self.instance.media_new(self.filename)
            self.set_videofile_path(self.filename)
            self.mediaplayer.set_media(media)
            # Embed the VLC video output into our video frame.
            if sys.platform.startswith('linux'):
                self.mediaplayer.set_xwindow(self.video_frame.winId())
            elif sys.platform == "win32":
                self.mediaplayer.set_hwnd(self.video_frame.winId())
            elif sys.platform == "darwin":
                self.mediaplayer.set_nsobject(int(self.video_frame.winId()))
            self.mediaplayer.play()
            # Start the timer to update the progress slider.
            self.timer.start()

    def execute_input(self, statistic_frame):
        f = open("./Data/Database_name.txt")
        database_name = f.read()
        sets = ["Satz 1", "Satz 2", "Satz 3", "Satz 4", "Satz 5"]
        if self.comline.text() in sets:
            self.set_set(self.comline.text())
        elif self.comline.text() =="r":
            self.court.rotieren()
            self.comline.clear()

        elif self.comline.text() =="ggfhl":

            DBFunctions.update_stats_points_values("VolleyScout2.db", database_name , "GgFhl")
            self.update_set_stat("GgFhl", database_name,statistic_frame)
            self.comline.clear()

        else:

            formated_command = self.comline.text().replace(" ", "")
            commands = formated_command.split(",")
            ic(commands)
            ic(self.bool_match(commands))
            if self.bool_match(commands):
                ic()
                for i in range(0,len(commands)):
                    ic()
                    #players_update = PlayersUpdate(commands[i],statistic_frame,str(int(self.mediaplayer.position()/1000)+i), database_name)
                    players_update = PlayersUpdate(commands[i], statistic_frame,str(int(self.mediaplayer.get_time() / 1000) + i), database_name)
                    ic()
                    players_update.start()
                    ic()
            self.comline.clear()

    def update_set_stat(self, action, database_name,statistic_frame):
        values = DBFunctions.get_stats_points_values("VolleyScout2.db", database_name).split("/")
        values_index = {"S" : 0, "A" : 1, "B" : 2, "GgFhl" : 3 }
        set_index = {"Satz 1" : 0, "Satz 2" : 1, "Satz 3" : 2, "Satz 4" : 3, "Satz 5" : 4}
        f = open("./Data/Current_Set.txt")
        statistic_frame.player_frame.all_labels_set[set_index[f.read()]].result_labels_points[values_index[action]].setText(values[values_index[action]])

    def set_set(self, current_set : str):
        with open("./Data/Current_Set.txt", "w") as f:  # in write mode
            f.write(current_set )



    def show_warning(self, input_le):
        QMessageBox.warning(
            self,
            "Fehler",  # Title of the window
            f"Fehler bei {input_le}",  # Content text
            QMessageBox.StandardButton.Ok  # Buttons to show
        )

    def bool_match(self, commands):
        for t in commands:
            if re.fullmatch(r"(\d\d?[SRBDAZ]([+0-]|(--)|(\+\+))((\(.*)?(:)?(.*\)))?)|\d\d?AB((\(.*)?(:)?(.*\)))?",
                            t) is None:
                print("Fehler bei:" + t)
                self.show_warning(t)
                return False
                break
        return True


    def pause_video(self):
        # Pause or resume video playback.
        self.mediaplayer.pause()

    def stop_video(self):
        # Stop video playback and reset the progress slider.
        self.mediaplayer.stop()
        self.timer.stop()
        self.progress_slider.setValue(0)

    def slider_pressed(self):
        # Set the flag when the slider is being dragged manually.
        self.slider_is_pressed = True

    def slider_released(self):
        # Clear the flag when the slider is released.
        self.slider_is_pressed = False
        self.set_position()
        # If the slider was moved manually and the video isn't playing (ended or stopped),
        # start playing again.
        if self.progress_slider.value() < self.progress_slider.maximum() and not self.mediaplayer.is_playing():
            media = self.instance.media_new(self.filename)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play()
            self.set_position()

    def set_position(self):
        # Seek to the position in the video based on the slider's value.
        pos = self.progress_slider.value() / 1000.0
        self.mediaplayer.set_position(pos)

    def update_ui(self):
        # Update the slider to reflect the current playback position.
        # Only update if the slider is not being moved manually.
        if self.mediaplayer.is_playing() and not self.slider_is_pressed:
            pos = self.mediaplayer.get_position()
            self.progress_slider.setValue(int(pos * 1000))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stats_window = StatsWindow()
    stats_window.show()
    player = VideoPlayer(stats_window.statistic_frame, stats_window.court)
    player.show()


    sys.exit(app.exec())
