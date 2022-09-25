import os
import subprocess
import sys
import datetime
from functools import partial
from random import randint

from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QStyle, QSlider, QLabel, QSizePolicy, QHBoxLayout, \
    QVBoxLayout, QFileDialog, QDialog, QLineEdit, QComboBox, QScrollArea, QMessageBox, QFrame
from PyQt5.QtCore import Qt, QUrl, QRegExp
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from KeyFunct import keyFunktionen
from XMLFunctions import *
import csv
import keyboard
import Keyboard_Functions
import re
import xml.etree.cElementTree as ET
from ExtQlineEdit import *
import glob
import os

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, lineup, islaufer1, time, counter, cur_game, pos1, pos2, pos3, pos4, pos5, pos6, libero, mp):
        super().__init__()
        self.setGeometry(1000, 700, 400, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Eingabefenster')
        # self.lineup = lineup
        layout_line = QHBoxLayout()
        layout = QVBoxLayout()
        self.line_ed = myQlineEdit(self, lineup, time, counter, cur_game, pos1, pos2, pos3, pos4, pos5, pos6, libero,
                                   mp)
        # self.line_ed.textChanged.connect(partial(self.repl_qle, self.line_ed))
        # self.line_ed.setEnabled(False)
        self.label = QLabel("Eingaben")
        self.btn_close = QPushButton('Schliessen')
        layout_line.addWidget(self.label)
        layout_line.addWidget(self.line_ed)
        layout_line.addWidget(self.btn_close)
        layout.addLayout(layout_line)
        self.setLayout(layout)

    def repl_qle(self, qle):
        tmp = qle.text()[:-1]
        qle.setText(tmp)


class WindowVideo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Scout")
        self.setGeometry(100, 100, 1800, 800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon("Soden.png"))
        self.set_Ui()
        self.counter = '0'
        self.current_game = ''
        self.current_game_path = ''
        self.ist_laufer_eins = False
        self.currentLineUp = []
        self.video_filepath = ''

    def dlg_queue(self):
        self.w = AnotherWindow(self.currentLineUp, self.ist_laufer_eins, str(self.mediaPlayer.position()),
                               self.key_counter, self.current_game + '.xml', self.pos1, self.pos2, self.pos3, self.pos4,
                               self.pos5, self.pos6, self.libero1, self.mediaPlayer)
        self.w.show()

    def set_Ui(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        # nonlocal self.self.pos1
        """
        self.pos1 = QLabel("Pos1")

        self.pos1.setText("Pos1")
        self.pos1.setFixedSize(100, 200)
        self.pos1.setAlignment(Qt.AlignCenter)
        self.pos1.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")

        

        self.pos2 = QLabel("Pos2")
        self.pos2.setFixedSize(100, 200)
        self.pos2.setAlignment(Qt.AlignCenter)
        self.pos2.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
        self.pos3 = QLabel("Pos3")
        self.pos3.setFixedSize(100, 200)
        self.pos3.setAlignment(Qt.AlignCenter)
        self.pos3.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
        self.pos4 = QLabel("Pos4")
        self.pos4.setFixedSize(100, 200)
        self.pos4.setAlignment(Qt.AlignCenter)
        self.pos4.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
        self.pos5 = QLabel("Pos5")
        self.pos5.setFixedSize(100, 200)
        self.pos5.setAlignment(Qt.AlignCenter)
        self.pos5.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
        self.pos6 = QLabel("Pos6")
        self.pos6.setFixedSize(100, 200)
        self.pos6.setAlignment(Qt.AlignCenter)
        self.pos6.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
        """
        self.libero1 = QLabel()
        self.libero1.setFixedSize(50, 100)
        self.libero1.setText("Libero")
        self.libero1.setAlignment(Qt.AlignCenter)
        self.libero1.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")

        self.label_game = QLabel('Aktuelles Spiel :')
        """
        self.backRow = QHBoxLayout()

        self.backRow.addWidget(self.pos5)
        self.backRow.addWidget(self.pos6)
        self.backRow.addWidget(self.pos1)
        self.backRow.setContentsMargins(30, 10, 30, 80)
        # self.backRow.setGeometry(0, 0, 300, 300)

        self.frontRow = QHBoxLayout()
        self.frontRow.addWidget(self.pos4)
        self.frontRow.addWidget(self.pos3)
        self.frontRow.addWidget(self.pos2)
        self.frontRow.setContentsMargins(30, 130, 30, 10)
        """


        self.liberoBox = QVBoxLayout()
        self.liberoBox.addWidget(self.libero1)
        self.liberoBox.setContentsMargins(280, 0, 0, 50)

        self.last_entrees = QVBoxLayout()
        self.label_title = QLabel('Letzte Aktionen')
        self.label_last = QLabel('')
        self.label_last_but_one = QLabel('')
        self.label_third_last = QLabel('')
        self.last_entrees.addWidget(self.label_title)
        self.last_entrees.addWidget(self.label_last)
        self.last_entrees.addWidget(self.label_last_but_one)
        self.last_entrees.addWidget(self.label_third_last)

        #self.court = QVBoxLayout()
        self.container = QWidget()
        self.frame = QFrame()
        #self.frame.setStyleSheet("background-repeat:no-repeat;background-position: center;background-image: url(Volleyball_Half_Court.png);")

        self.pos1 = QLabel("Pos1", self.frame)
        self.pos1.setFixedSize(60, 60)
        self.pos1.move(250, 180)
        self.pos1.setAlignment(Qt.AlignCenter)
        self.pos1.setStyleSheet("font: bold 16px;")
        #self.pos1.setAttribute(Qt.WA_TranslucentBackground)

        self.pos2 = QLabel("Pos2", self.frame)
        self.pos2.setFixedSize(60, 60)
        self.pos2.move(250, 50)
        self.pos2.setAlignment(Qt.AlignCenter)
        self.pos2.setStyleSheet("font: bold 16px;")
        #self.pos2.setAttribute(Qt.WA_TranslucentBackground)

        self.pos3 = QLabel("Pos3", self.frame)
        self.pos3.setFixedSize(60, 60)
        self.pos3.move(170, 50)
        self.pos3.setAlignment(Qt.AlignCenter)
        self.pos3.setStyleSheet("font: bold 16px;")
        #self.pos3.setAttribute(Qt.WA_TranslucentBackground)

        self.pos4 = QLabel("Pos4", self.frame)
        self.pos4.setFixedSize(60, 60)
        self.pos4.move(90, 50)
        self.pos4.setAlignment(Qt.AlignCenter)
        self.pos4.setStyleSheet("font: bold 16px;")
        #self.pos4.setAttribute(Qt.WA_TranslucentBackground)

        self.pos5 = QLabel("Pos5", self.frame)
        self.pos5.setFixedSize(60, 60)
        self.pos5.move(90, 180)
        self.pos5.setAlignment(Qt.AlignCenter)
        self.pos5.setStyleSheet("font: bold 16px;")
        #self.pos5.setAttribute(Qt.WA_TranslucentBackground)

        self.pos6 = QLabel("Pos6", self.frame)
        self.pos6.setFixedSize(60, 60)
        self.pos6.move(170, 180)
        self.pos6.setAlignment(Qt.AlignCenter)
        self.pos6.setStyleSheet("font: bold 16px;")
        #self.pos6.setAttribute(Qt.WA_TranslucentBackground)

        self.all_pos_labels = []
        self.all_pos_labels.append(self.pos1)
        self.all_pos_labels.append(self.pos2)
        self.all_pos_labels.append(self.pos3)
        self.all_pos_labels.append(self.pos4)
        self.all_pos_labels.append(self.pos5)
        self.all_pos_labels.append(self.pos6)
        self.all_pos_labels.append(self.libero1)

        self.frame.setStyleSheet(
            "background-repeat:no-repeat;background-position: center;background-image: url(Volleyball_Half_Court.png);")
        self.frame.setFixedSize(400, 400)
        self.court = QVBoxLayout()
        self.inner_court = QVBoxLayout()
        #self.inner_court.addWidget(self.container)
        # self.court.setGeometry(10, 10, 200, 300 )
        self.court.addWidget(self.label_game)
        #self.inner_court.addLayout(self.frontRow)
        #self.inner_court.addLayout(self.backRow)
        #self.inner_court.addLayout(self.liberoBox)
        #self.court.addLayout(self.inner_court)
        self.court.addWidget(self.frame)
        self.court.addLayout(self.liberoBox)
        self.court.addLayout(self.last_entrees)

        self.container.setStyleSheet("background-repeat:no-repeat;background-position: center;background-image: url(Volleyball_Half_Court.png);")



        button_newgame = QPushButton("Neues Spiel")
        button_load_del_game = QPushButton("Spiel laden/entf.")
        buttonLineUp = QPushButton("Aufstellung")
        buttonRotation = QPushButton("Manuelle Eingabe")
        buttonInput = QPushButton("Eingabe löschen")
        buttonInput.setEnabled(False)
        button_sub = QPushButton('Spielerwechsel')
        button_sub.setEnabled(False)
        button_libchange = QPushButton('Libero wechsel')
        buttonFilter = QPushButton("Filtern")
        label_holder = QLabel('')
        label_holder.setFixedHeight(80)
        button_close = QPushButton("Programm schließen")
        btnBox = QVBoxLayout()
        btnBox.addWidget(button_newgame)
        btnBox.addWidget(button_load_del_game)
        btnBox.addWidget(buttonLineUp)
        btnBox.addWidget(button_sub)
        btnBox.addWidget(button_libchange)
        btnBox.addWidget(buttonRotation)
        btnBox.addWidget(buttonInput)
        btnBox.addWidget(buttonFilter)
        btnBox.addWidget(label_holder)
        btnBox.addWidget(button_close)
        btnBox.setContentsMargins(80, 180, 80, 180)

        buttonLineUp.clicked.connect(partial(self.setLineUp, button_sub))
        button_libchange.clicked.connect(self.libero_change)
        button_newgame.clicked.connect(self.set_newgame)
        button_load_del_game.clicked.connect(partial(self.set_load_del_game, buttonInput))
        buttonInput.clicked.connect(self.del_Node)
        button_sub.clicked.connect(self.subs)
        buttonFilter.clicked.connect(self.filter_dlg)
        coreVBox = QHBoxLayout()

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videoWidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        coreVBox.addLayout(vboxLayout, 3)
        coreVBox.addLayout(self.court, 1)
        #coreVBox.addWidget(self.container, 1)
        coreVBox.addLayout(btnBox, 1)

        # self.setLayout(vboxLayout)
        self.setLayout(coreVBox)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        self.key_counter = '0'


    def dia_warn(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Eingabefehler!")
        msg.setInformativeText(text)
        msg.setWindowTitle("Fehler")
        msg.exec_()

    def libero_change(self):
        print('1')
        dir = os.path.dirname(__file__)
        dir = dir + "/Gamedata/CurrentTeam"
        allLiberos = []
        with open(dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if len(row) == 2:
                    if row[1] == 'Libero':
                        allLiberos.append(row[0])

            if len(allLiberos) == 0:
                self.dia_warn("Keine Liberos/Liberas eingetragen")
            elif len(allLiberos) == 1:
                self.dia_warn("Nur ein Libero/eine Libera eingetragen")
            elif len(allLiberos) == 2:
                for i in self.currentLineUp:
                    if i[1] == 'Libero':
                        print('2')
                        if i[0] == allLiberos[0]:
                            i[0] = allLiberos[1]
                            for l in self.all_pos_labels:
                                if l.text() == allLiberos[0]:
                                    l.setText(allLiberos[1])
                                print('3')
                        else:
                            i[0] = allLiberos[0]
                            for l in self.all_pos_labels:
                                if l.text() == allLiberos[1]:
                                    l.setText(allLiberos[0])
                                    print('4')
            else:
                self.dia_warn("Sonstiger Fehler. Vielleicht mehr als drei Liberos/Liberas")


    def filter_dlg(self):
        dlg_load_del_game = QDialog(self)
        dlg_load_del_game.setFixedSize(400, 300)
        dlg_load_del_game.setWindowTitle("Filtern")
        game_name_label = QLabel("Spieler wählen :", dlg_load_del_game)
        game_name_label.move(20, 40)
        game_name_edit = QComboBox(dlg_load_del_game)
        game_name_edit.addItem('')
        game_name_edit.move(120, 40)
        dir = os.path.dirname(__file__)
        dir = dir + "/Gamedata/CurrentTeam"
        with open(dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if len(row) == 2:
                    game_name_edit.addItem(row[0])

        del_game_label = QLabel("Aktion wählen :", dlg_load_del_game)
        del_game_label.move(20, 80)
        del_combobox = QComboBox(dlg_load_del_game)
        del_combobox.move(120, 80)
        del_combobox.addItems(
            ['', 'Aufschlag', 'Annahme', 'Zuspiel', 'Angriff', 'Abwehr', 'Block', 'Doppelblock', 'Dreierblock'])
        rating_label = QLabel('Bewertung wählen', dlg_load_del_game)
        rating_label.move(20, 120)
        rating_cmbx = QComboBox(dlg_load_del_game)
        rating_cmbx.move(120, 120)
        rating_cmbx.addItems(['', '++', '+', '0', '-', '--', 'E'])

        firstball_label = QLabel('Ersten Ball wählen', dlg_load_del_game)
        firstball_label.move(20, 160)
        firstball_cmbx = QComboBox(dlg_load_del_game)
        firstball_cmbx.move(120, 160)
        firstball_cmbx.addItems(['', 'Läufer1', 'Läufer6', 'Läufer5', 'Läufer4', 'Läufer3', 'Läufer2', 'Verteidigung'])

        btn_del_game = QPushButton('Filtern', dlg_load_del_game)
        btn_del_game.move(250, 200)
        btn_abort = QPushButton('Schließen', dlg_load_del_game)
        btn_abort.move(150, 200)
        btn_del_game.clicked.connect(
            partial(self.create_videos, game_name_edit, del_combobox, rating_cmbx, firstball_cmbx, self.video_filepath))
        btn_abort.clicked.connect(dlg_load_del_game.close)
        dlg_load_del_game.exec()

    def create_videos(self, cb_pl, cb_act, cb_rat, cb_fb, videopath):
        print('Start')
        player = str(cb_pl.currentText())
        print(player)
        aktion = str(cb_act.currentText())
        print(aktion)
        firstball = str(cb_fb.currentText())
        print(firstball)
        if len(firstball) > 0 :
            firstball = firstball[-1]
        print('erster Ball')
        print(firstball)
        rating = str(cb_rat.currentText())

        if cb_act.currentText() == '':
            aktion = '*'

        if rating != '':
            rating = "[@rating='" + rating + "']"
        if firstball != '':
            firstball = "[@Laufer='" + firstball + "']"
        if player != '':
            player = "[.='" + player + "']"

        print(player + ' ' + aktion + ' ' + firstball + ' ' + rating + ' ' + videopath)

        dir = os.path.dirname(__file__)
        dir = dir + "/Games/" + 'Test.xml'

        tree = ET.parse(self.current_game_path)
        all_timestamps = []

        for i in tree.findall(".//Timestamp//" + aktion + rating + firstball + player + "/.."):
            all_timestamps.append(i.get('time'))
        saving_path = self.file_save()

        if not saving_path.endswith('.mp4'):
            saving_path = saving_path + '.mp4'
        clips = []
        # path = "C:/videos/Paula_Angriff_final.mp4"
        path_tmp = saving_path.replace(".mp4", "tmp.mp4")
        self.concatenate(all_timestamps, saving_path, videopath)





    def concatenate(self, all_timestamps, saving_path, videopath):

        dir = os.path.dirname(__file__)
        dir = dir + "/Videofiles/"
        files_to_delete = []
        print(all_timestamps)
        for i in range(len(all_timestamps)):
            cliptmp = ffmpeg_extract_subclip(videopath, float(all_timestamps[i]) - 4, float(all_timestamps[i]) + 6,
                                         targetname=dir + "cutfinal" + str(i) + ".mp4")
            files_to_delete.append(dir + "cutfinal" + str(i) + ".mp4")
        print('Checkpoint')
        stringa = "ffmpeg -i \"concat:"
        elenco_video = glob.glob(dir + "*.mp4")
        elenco_file_temp = []
        for f in elenco_video:
            file = dir + "temp" + str(elenco_video.index(f) + 1) + ".ts"
            files_to_delete.append(dir + "temp" + str(elenco_video.index(f) + 1) + ".ts")
            os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
            elenco_file_temp.append(file)
        #print(elenco_file_temp)
        tmp_end_file = dir + saving_path[-5:]
        print(tmp_end_file)
        for f in elenco_file_temp:
            stringa += f
            if elenco_file_temp.index(f) != len(elenco_file_temp) - 1:
                stringa += "|"
            else:
                stringa += "\" -c copy  -bsf:a aac_adtstoasc " + tmp_end_file
                #stringa += "\" -c copy  -bsf:a " + saving_path
        #print(stringa)
        #os.system(stringa)


        dir = os.path.dirname(__file__) + "/FFMPEG static/ffmpeg.exe"
        cmd = stringa.replace('ffmpeg', dir)
        #print(cmd)
        subprocess.call(cmd, shell=False)
        os.system("ffmpeg -i " + tmp_end_file + " -c copy -an " + saving_path)
        #for i in files_to_delete:
            #os.remove(i)


    def file_save(self):
        # file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        file = QFileDialog.getSaveFileName(self, 'Save File', 'C:\\videos', "Video Files (*.mp4)")
        return file[0]

    def on_press(self, key):

        kb_f = Keyboard_Functions.Keyboard_func()
        keyboard.add_hotkey('q', kb_f.sag_Hallo('Was geht'))

    def del_Node(self):
        dlg_load_del_game = QDialog(self)
        dlg_load_del_game.setFixedSize(500, 600)
        dlg_load_del_game.setWindowTitle("Aktion löschen")
        game_name_label = QLabel("Id eingeben:", dlg_load_del_game)
        game_name_label.move(20, 80)
        game_name_edit = QLineEdit(dlg_load_del_game)
        game_name_edit.move(120, 80)
        btn_del_action = QPushButton('Löschen', dlg_load_del_game)
        btn_del_action.move(280, 80)
        all_actions = QScrollArea(dlg_load_del_game)
        all_actions.move(20, 120)
        all_actions.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        all_actions.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        all_actions.setWidgetResizable(True)
        btn_abort = QPushButton('Schließen', dlg_load_del_game)
        btn_abort.move(300, 550)
        btn_abort.clicked.connect(dlg_load_del_game.close)
        widget = QWidget()

        vbox = tree_to_labels(self.current_game)
        widget.setLayout(vbox)
        all_actions.setWidget(widget)
        btn_del_action.clicked.connect(partial(delete_node, game_name_edit, self.current_game_path))
        # btn_del_action.clicked.connect(partial(self.reload_labels, self.widget, self.vbox, self.all_actions, dlg_load_del_game))
        dlg_load_del_game.exec()

    def reload_labels(self, widget, box, scroll, dialog):
        pass

    def subs(self):
        sub_dlg = QDialog(self)
        sub_dlg.setFixedSize(400, 250)
        sub_dlg.setWindowTitle('Spielerwechsel')
        label_player_out = QLabel('Spieler der rausgeht: ', sub_dlg)
        label_player_out.move(20, 80)
        cbx_players_out = QComboBox(sub_dlg)
        for player in self.currentLineUp[:6]:
            cbx_players_out.addItem(player[0])
        cbx_players_out.move(150, 80)
        label_player_in = QLabel('Spieler der reingeht: ', sub_dlg)
        label_player_in.move(20, 120)
        cbx_players_in = QComboBox(sub_dlg)
        btn_sub = QPushButton('Wechseln', sub_dlg)
        btn_sub.move(300, 200)
        whole_team = []
        dir = os.path.dirname(__file__)
        dir = dir + "/Gamedata/CurrentTeam"
        with open(dir) as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if (row != '') and (len(row) == 2):
                    if row[1] != 'Libero':
                        whole_team.append(row[0])

        on_court = []
        print("2")
        for i in self.currentLineUp[:6]:
            on_court.append(i[0])
        rest_team = self.Diff(whole_team, on_court)

        cbx_players_in.addItems(rest_team)
        cbx_players_in.move(150, 120)
        label_as = QLabel(' als ', sub_dlg)
        label_as.move(250, 120)
        cbx_positions = QComboBox(sub_dlg)
        cbx_positions.move(280, 120)
        cbx_positions.addItems(['Mitte', 'Aussen', 'Zuspiel', 'Diagonal'])
        print("3")
        btn_sub.clicked.connect(
            partial(self.sub_players, cbx_players_out, cbx_players_in, cbx_positions, self.currentLineUp, rest_team))
        sub_dlg.exec()

    def sub_players(self, combox1, combox2, combox3, cur_team_list, rest_team_list):
        # words = [word.replace('[br]', '<br />') for word in words]
        for i in range(len(cur_team_list)):
            if cur_team_list[i][0] == str(combox1.currentText()):
                cur_team_list[i][0] = str(combox2.currentText())
                cur_team_list[i][1] = str(combox3.currentText())
                """
                Für Morgen
                
                """
                print(cur_team_list[i][2])
                if (cur_team_list[i][2] == '1') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos1.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '1'):
                        self.pos1.setText(str(combox2.currentText()) + '\n (Z)')

                if (cur_team_list[i][2] == '2') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos2.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '2'):
                        self.pos2.setText(str(combox2.currentText()) + '\n (Z)')

                if (cur_team_list[i][2] == '3') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos3.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '3'):
                        self.pos3.setText(str(combox2.currentText()) + '\n (Z)')

                if (cur_team_list[i][2] == '4') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos4.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '4'):
                        self.pos4.setText(str(combox2.currentText()) + '\n (Z)')

                if (cur_team_list[i][2] == '5') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos5.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '5'):
                        self.pos5.setText(str(combox2.currentText()) + '\n (Z)')

                if (cur_team_list[i][2] == '6') and (str(combox3.currentText()) != 'Zuspiel'):
                    self.pos6.setText(str(combox2.currentText()))
                else:
                    if (cur_team_list[i][2] == '6'):
                        self.pos6.setText(str(combox2.currentText()) + '\n (Z)')

        print(cur_team_list)
        for j in range(len(rest_team_list)):
            if rest_team_list[j] == str(combox2.currentText()):
                rest_team_list[j] = str(combox1.currentText())

    def Diff(self, li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif

    def set_load_del_game(self, btn1):
        dlg_load_del_game = QDialog(self)
        dlg_load_del_game.setFixedSize(400, 300)
        dlg_load_del_game.setWindowTitle("Spiel laden / entfernen")
        game_name_label = QLabel("Spiel laden :", dlg_load_del_game)
        game_name_label.move(20, 80)
        game_name_edit = QComboBox(dlg_load_del_game)
        game_name_edit.move(120, 80)
        self.games_to_combobox(game_name_edit)
        btn_load_game = QPushButton('Laden', dlg_load_del_game)
        btn_load_game.move(250, 80)
        del_game_label = QLabel("Spiel entfernen :", dlg_load_del_game)
        del_game_label.move(20, 140)
        del_combobox = QComboBox(dlg_load_del_game)
        del_combobox.move(120, 140)
        self.games_to_combobox(del_combobox)
        btn_del_game = QPushButton('Entfernen', dlg_load_del_game)
        btn_del_game.move(250, 140)
        btn_abort = QPushButton('Schließen', dlg_load_del_game)
        btn_abort.move(150, 200)
        btn_load_game.clicked.connect(partial(self.load_game, game_name_edit))
        btn_load_game.clicked.connect(partial(self.enable_btn, btn1))
        btn_del_game.clicked.connect(partial(self.del_game, del_combobox, del_combobox, game_name_edit))
        btn_abort.clicked.connect(dlg_load_del_game.close)
        dlg_load_del_game.exec()

    def enable_btn(self, btn):
        btn.setEnabled(True)

    def load_game(self, load_box):
        dir = os.path.dirname(__file__)
        dir = dir + "/Games/" + str(load_box.currentText()) + '.xml'
        self.current_game_path = dir
        self.current_game = str(load_box.currentText())
        self.label_game.setText('Aktuelles Spiel : \n' + self.current_game)
        tree = ET.parse(self.current_game_path)
        root = tree.getroot()
        try:
            self.key_counter = root.find('Timestamp[last()]').get('id')
            self.key_counter = self.increase_counter(self.key_counter)
        except:
            self.key_counter = '1'

    def increase_counter(self, key_c):
        key_c = int(key_c) + 1
        result = str(key_c)
        return result

    def del_game(self, del_box, box1, box2):
        dir = os.path.dirname(__file__)
        dir = dir + "/Games/" + str(del_box.currentText()) + '.xml'
        os.remove(dir)
        box1.clear()
        box2.clear()
        self.games_to_combobox(box1)
        self.games_to_combobox(box2)

    def games_to_combobox(self, box):
        dir = os.path.dirname(__file__)
        dir = dir + "/Games"
        names = os.listdir(dir)
        for f in names:
            box.addItem(f.split('.')[0])

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):

        self.slider.setValue(position)

        # cur_time = str(datetime.timedelta(self.mediaPlayer.position()))
        # self.label.setText(cur_time)

        self.label.setText(self.hhmmss(self.mediaPlayer.position()))

    def hhmmss(self, ms):
        # s = 1000
        # m = 60000
        # h = 3600000
        s = round(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def liberoInOut(self, lineup):
        for outer in lineup:
            if outer[2] == '0':
                outerpos = lineup.index(outer)

        k = keyFunktionen()
        if k.liberodrin(lineup):
            print('drin')
            for p in lineup:
                if p[1] == 'Libero':
                    liberoposition = p[2]

            if liberoposition == '1':
                labelCourt = self.pos1
                self.pos1.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
            if liberoposition == '6':
                labelCourt = self.pos6
                self.pos6.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
            if liberoposition == '5':
                labelCourt = self.pos5
                self.pos5.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")

            for p in lineup:

                if p[1] == 'Libero':
                    tmp = lineup[outerpos][2]

                    lineup[outerpos][2] = p[2]
                    p[2] = tmp
            tmp = self.libero1.text()
            self.libero1.setText(labelCourt.text())
            self.libero1.setStyleSheet("background-color: blue; border: 2px; font: bold 14px;")
            print('style1')
            labelCourt.setText(tmp)
            labelCourt.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
            print('style2')
            #labelCourt.setAttribute(Qt.WA_NoSystemBackground)

        elif not k.liberodrin(lineup):
            print('nicht drin')
            for p in lineup:
                if (p[1] == 'Mitte') and ((p[2] == '1') or (p[2] == '6') or (p[2] == '5')):
                    mittePosition = p[2]

            if mittePosition == '1':
                labelCourt = self.pos1
            if mittePosition == '6':
                labelCourt = self.pos6
            if mittePosition == '5':
                labelCourt = self.pos5

            for p in lineup:
                if (p[1] == 'Mitte') and ((p[2] == '1') or (p[2] == '5') or (p[2] == '6')):
                    tmp = lineup[outerpos][2]
                    lineup[outerpos][2] = p[2]
                    p[2] = tmp
            tmp = self.libero1.text()
            self.libero1.setText(labelCourt.text())
            self.libero1.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")
            labelCourt.setText(tmp)
            #labelCourt.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
        else:
            None

    def showCurrentLineup(self, lineup):
        print(lineup)

    def setLineUp(self, btn):

        dlgLineUp = QDialog(self)
        dlgLineUp.setFixedSize(300, 300)
        dlgLineUp.setWindowTitle("Aufstellung bestimmen")
        playerlabel = QLabel("Spieler", dlgLineUp)
        playerlabel.move(10, 10)
        positionLabel = QLabel("Startposition", dlgLineUp)
        positionLabel.move(120, 10)
        player1 = QComboBox(dlgLineUp)
        player1.move(10, 40)
        player2 = QComboBox(dlgLineUp)
        player2.move(10, 70)
        player3 = QComboBox(dlgLineUp)
        player3.move(10, 100)
        player4 = QComboBox(dlgLineUp)
        player4.move(10, 130)
        player5 = QComboBox(dlgLineUp)
        player5.move(10, 160)
        player6 = QComboBox(dlgLineUp)
        player6.move(10, 190)
        liberos = QComboBox(dlgLineUp)
        liberos.move(200, 70)
        dir = os.path.dirname(__file__)
        dir = dir + "/Gamedata/CurrentTeam"
        allnumbers = []

        result2 = []
        with open(dir) as csv_file:
            csv_reader_object = csv.reader(csv_file)

            for row in csv_reader_object:
                if len(row) == 2:
                    result2.append(row)

                    if row[1] != 'Libero':
                        player1.addItem(row[0])
                        player2.addItem(row[0])
                        player3.addItem(row[0])
                        player4.addItem(row[0])
                        player5.addItem(row[0])
                        player6.addItem(row[0])
                    if row[1] == 'Libero':
                        liberos.addItem(row[0])
        positionLabel1 = QLabel("Pos 1", dlgLineUp)
        positionLabel1.move(120, 40)
        positionLabel2 = QLabel("Pos 2", dlgLineUp)
        positionLabel2.move(120, 70)
        positionLabel3 = QLabel("Pos 3", dlgLineUp)
        positionLabel3.move(120, 100)
        positionLabel4 = QLabel("Pos 4", dlgLineUp)
        positionLabel4.move(120, 130)
        positionLabel5 = QLabel("Pos 5", dlgLineUp)
        positionLabel5.move(120, 160)
        positionLabel6 = QLabel("Pos 6", dlgLineUp)
        positionLabel6.move(120, 190)
        liberoLabel = QLabel("Startlibero", dlgLineUp)
        liberoLabel.move(200, 40)

        buttonsetLineUp = QPushButton("Aufstellung bestätigen", dlgLineUp)
        buttonsetLineUp.move(120, 250)
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos1, player1, result2, self.currentLineUp, '1'))
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos2, player2, result2, self.currentLineUp, '2'))
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos3, player3, result2, self.currentLineUp, '3'))
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos4, player4, result2, self.currentLineUp, '4'))
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos5, player5, result2, self.currentLineUp, '5'))
        buttonsetLineUp.clicked.connect(partial(self.set_lineup, self.pos6, player6, result2, self.currentLineUp, '6'))
        buttonsetLineUp.clicked.connect(
            partial(self.set_lineup, self.libero1, liberos, result2, self.currentLineUp, '0'))
        buttonsetLineUp.clicked.connect(partial(self.enable_btn, btn))
        buttonsetLineUp.clicked.connect(dlgLineUp.close)
        buttonsetLineUp.clicked.connect(self.dlg_queue)
        btn_rndlineup = QPushButton('Aufstellung', dlgLineUp)
        btn_rndlineup.move(50, 250)
        btn_rndlineup.clicked.connect(partial(self.lineup_rnd, player1, player2, player3, player4, player5, player6))
        dlgLineUp.exec()


    def set_lineup(self, labelcourt, comboboxdialog, playerlist, lineup, pos):

        tmp = []
        tmp.append(comboboxdialog.currentText())
        print('lineup')
        print(lineup)
        for item in playerlist:
            print('for')
            print(item[0])
            print(comboboxdialog.currentText())
            if item[0] == comboboxdialog.currentText():
                tmp.append(item[1])
        tmp.append(pos)
        lineup.append(tmp)
        print('lineup')
        print(lineup)
        for item in playerlist:

            if item[0] == comboboxdialog.currentText() and item[1] == 'Zuspiel':
                text = comboboxdialog.currentText() + "\n (Z)"
                labelcourt.setText(text)
                # lineup.append(tmp)
                break

            elif item[0] == comboboxdialog.currentText() and item[1] == 'Libero':
                text = comboboxdialog.currentText()
                labelcourt.setText(text)
                # lineup.append(tmp)
                break

            else:
                labelcourt.setText(comboboxdialog.currentText())


    def lineup_rnd(self, cb1, cb2, cb3, cb4, cb5, cb6):
        cb1.setCurrentIndex(5)
        cb2.setCurrentIndex(0)
        cb3.setCurrentIndex(1)
        cb4.setCurrentIndex(4)
        cb5.setCurrentIndex(3)
        cb6.setCurrentIndex(6)

    def enable_btn(self, btn):
        btn.setEnabled(True)

    def set_newgame(self):
        dlgnewgame = QDialog(self)
        dlgnewgame.setFixedSize(300, 300)
        dlgnewgame.setWindowTitle("Aufstellung bestimmen")
        game_name_label = QLabel("Spielname :", dlgnewgame)
        game_name_label.move(20, 20)
        game_name_edit = QLineEdit(dlgnewgame)
        game_name_edit.move(120, 20)
        opponentsname_label = QLabel("Gegner :", dlgnewgame)
        opponentsname_label.move(20, 80)
        opponentsname_edit = QLineEdit(dlgnewgame)
        opponentsname_edit.move(120, 80)
        btn_newgame = QPushButton('Neues Spiel erstellen', dlgnewgame)
        btn_newgame.move(20, 150)
        btn_abort = QPushButton('Abbrechen', dlgnewgame)
        btn_abort.move(150, 150)
        btn_newgame.clicked.connect(partial(self.create_new_game, game_name_edit, opponentsname_edit))
        btn_newgame.clicked.connect(dlgnewgame.close)
        btn_abort.clicked.connect(dlgnewgame.close)
        dlgnewgame.exec()

    def create_new_game(self, filename, rootname):
        print(filename.text())
        dir = os.path.dirname(__file__)
        dir = dir + "/Games/" + filename.text() + ".xml"
        file = open("copy.txt", "w")
        create_root(dir, rootname.text())
        file.close()
        self.current_game = filename.text() + ".xml"
        self.current_game_path = dir

    def rotieren(self, label1, label2, label3, label4, label5, label6):
        for item in self.currentLineUp:
            if item[2] == '1':
                item[2] = '6'
            elif item[2] == '6':
                item[2] = '5'
            elif item[2] == '5':
                item[2] = '4'
            elif item[2] == '4':
                item[2] = '3'
            elif item[2] == '3':
                item[2] = '2'
            elif item[2] == '2':
                item[2] = '1'
        else:
            None

        for player in self.currentLineUp:
            if (player[1] == 'Libero') and (player[2] != 0):
                if player[2] == '6':
                    label1.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")
                    label6.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
                if player[2] == '5':
                    label6.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")
                    label5.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")

        tmp = label1.text()
        label1.setText(label2.text())
        label2.setText(label3.text())
        label3.setText(label4.text())
        label4.setText(label5.text())
        label5.setText(label6.text())
        label6.setText(tmp)

        for outer in self.currentLineUp:
            if outer[2] == '0':
                outerpos = self.currentLineUp.index(outer)

        for i in self.currentLineUp:
            if (i[1] == 'Libero') and (i[2] == '4'):
                tmp = i[2]
                i[2] = self.currentLineUp[outerpos][2]
                self.currentLineUp[outerpos][2] = tmp
                tmp = self.libero1.text()
                self.libero1.setText(label4.text())
                self.libero1.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
                label4.setText(tmp)
                label4.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")
                label5.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")


                # tmp.append(comboboxdialog.currentText())
        # lineup = lineup[:4]

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.video_filepath = filename


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    # app = QApplication(sys.argv)
    # window = WindowVideo()
    # sys.exit(app.exec())
