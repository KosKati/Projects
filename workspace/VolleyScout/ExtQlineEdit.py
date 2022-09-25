from functools import partial
from random import randint

from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QStyle, QSlider, QLabel, QSizePolicy, QHBoxLayout, \
    QVBoxLayout, QFileDialog, QDialog, QLineEdit, QComboBox, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QRegExp
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from KeyFunct import keyFunktionen
from XMLFunctions import *
import csv
import keyboard
import Keyboard_Functions
import re
import xml.etree.cElementTree as ET


class MediaPl():
    def __init__(self, mp):
        self.mp = mp

    def get_time(self):
        return self.mp.position()


class myQlineEdit(QLineEdit):
    def __init__(self, parent, lineup, time, counter, cur_game, pos1, pos2, pos3, pos4, pos5, pos6, libero, mp):
        QLineEdit.__init__(self, parent)
        self.lineup = lineup
        self.islaufer1 = False
        self.ist_aufschlag = False
        self.time = str(mp.position())
        self.counter = counter
        self.cur_game = cur_game
        self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6 = pos1, pos2, pos3, pos4, pos5, pos6
        self.libero1 = libero
        self.laufer = ''
        self.mediaPlayer = mp

    def check_position(self):
        print(self.lineup)
        zuspieler_drin = False
        zuspieler_diagonal_vorne = False
        mitte_vorne = False
        aussen_vorne = False

        positions = []
        for k in self.lineup:
            if (k[1] == 'Zuspiel') and ((k[2] == '1') or (
                    (k[2] == '2') or (k[2] == '3') or (k[2] == '4') or (k[2] == '5') or (k[2] == '6'))):
                zuspieler_drin = True

        for k in self.lineup:
            if ((k[1] == 'Zuspiel') or (k[1] == 'Diagonal')) and ((k[2] == '2') or (k[2] == '3') or (k[2] == '4')):
                positions.append(k[2])
                zuspieler_diagonal_vorne = True
        for k in self.lineup:
            if (k[1] == 'Mitte') and ((k[2] == '2') or (k[2] == '3') or (k[2] == '4')):
                positions.append(k[2])
                mitte_vorne = True
        for k in self.lineup:
            if (k[1] == 'Aussen') and ((k[2] == '2') or (k[2] == '3') or (k[2] == '4')):
                positions.append(k[2])
                aussen_vorne = True

        vorne_pos_korrekt = aussen_vorne and mitte_vorne and zuspieler_diagonal_vorne
        contains_duplicates = any(positions.count(element) > 1 for element in positions)
        if (len(positions) != 3) and contains_duplicates:
            return False
        else:
            return vorne_pos_korrekt

    def get_zuspiel_pos(self):
        for i in self.lineup:
            if i[1] == 'Zuspiel':
                self.laufer = i[2]

    def inc_counter(self):
        self.counter = int(self.counter)
        self.counter = self.counter + 1
        self.counter = str(self.counter)

    def dia_warn(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Eingabefehler!")
        msg.setInformativeText(text)
        msg.setWindowTitle("Fehler")
        msg.exec_()

    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        kb_f = Keyboard_Functions.Keyboard_func()
        if (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_Q):
            if self.check_position():
                self.setText(self.text() + "" + kb_f.get_pos_four(self.lineup, self.islaufer1))
                self.setText(self.text() + "&" + kb_f.get_pos_three(self.lineup) + '#B')
            else:
                self.dia_warn(
                    'Positionen auf dem Feld entsprechen nicht der Norm. Benutzen Sie ggf. die Manuelle Engabe')
        elif event.key() == Qt.Key_Q:
            if self.check_position():
                #self.setText(self.text() + "" + kb_f.get_pos_four(self.lineup, self.islaufer1))
                self.setText(self.text() + "" + kb_f.get_front_outside(self.lineup))
            else:
                self.dia_warn(
                    'Positionen auf dem Feld entsprechen nicht der Norm. Benutzen Sie ggf. die Manuelle Engabe')
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_W):
            if self.check_position():
                self.setText(self.text() + "" + kb_f.get_pos_four(self.lineup, self.islaufer1))
                self.setText(self.text() + "&" + kb_f.get_pos_three(self.lineup))
                self.setText(self.text() + "&" + kb_f.get_pos_two(self.lineup, self.islaufer1) + '#B')
            else:
                self.dia_warn(
                    'Positionen auf dem Feld entsprechen nicht der Norm. Benutzen Sie ggf. die Manuelle Engabe')
        elif event.key() == Qt.Key_W:
            if self.check_position():
                self.setText(self.text() + "" + kb_f.get_pos_three(self.lineup))
            else:
                self.dia_warn(
                    'Positionen auf dem Feld entsprechen nicht der Norm. Benutzen Sie ggf. die Manuelle Engabe')
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_E):
            if self.check_position():
                self.setText(self.text() + "" + kb_f.get_pos_three(self.lineup))
                self.setText(self.text() + "&" + kb_f.get_pos_two(self.lineup, self.islaufer1) + '#B')
            else:
                self.dia_warn(
                    'Positionen auf dem Feld entsprechen nicht der Norm. Benutzen Sie ggf. die Manuelle Engabe')
        elif event.key() == Qt.Key_D:
            self.setText(self.text() + "" + kb_f.get_zuspieler(self.lineup))
        elif event.key() == Qt.Key_A:
            self.setText(self.text() + "" + kb_f.get_pos_five(self.lineup))
        elif event.key() == Qt.Key_S:
            self.setText(self.text() + "" + kb_f.get_pos_six(self.lineup))
        elif event.key() == Qt.Key_E:
            self.setText(self.text() + "" + kb_f.get_diagonal(self.lineup))
        elif event.key() == Qt.Key_Backspace:
            self.setText(self.text()[:-1])

        # Aktionen

        elif event.key() == Qt.Key_H:
            self.ist_aufschlag = True
            self.islaufer1 = False
            for i in self.lineup:
                if (i[2] == '1') and (i[1] != 'Libero') and (self.text() == ''):
                    self.setText(i[0] + "#S")
        elif event.key() == Qt.Key_M:
            self.ist_aufschlag = False
            for i in self.lineup:
                if i[2] == '1' and (i[1] == 'Zuspiel'):
                    self.islaufer1 = True
                    print('Wir haben Läufer 1')
            self.setText(self.text() + "#R")
        elif event.key() == Qt.Key_N:
            self.ist_aufschlag = False
            self.setText(self.text() + "#D")
        elif event.key() == Qt.Key_J:
            self.ist_aufschlag = False
            self.setText(self.text() + "#A")
        elif event.key() == Qt.Key_K:
            self.ist_aufschlag = False
            self.setText(self.text() + "#B")
        elif event.key() == Qt.Key_L:
            self.ist_aufschlag = False
            self.setText(self.text() + "#Z")

        # Bewertungen
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_U):
            if self.ist_aufschlag:
                self.setText(self.text() + "++, ")
            else:
                self.setText(self.text() + "++, ")
        elif event.key() == Qt.Key_U:
            self.setText(self.text() + "+, ")
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_I):
            self.setText(self.text() + "0, ")
        elif event.key() == Qt.Key_I:
            self.setText(self.text() + "-, ")
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_O):
            self.setText(self.text() + "--, ")
        elif event.key() == Qt.Key_O:
            self.setText(self.text() + "E, ")

        # Rest

        elif event.key() == Qt.Key_R:
            self.islaufer1 = False
            self.rotieren(self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6)

        elif event.key() == Qt.Key_V:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() + 9000)

        elif event.key() == Qt.Key_C:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() - 9000)

        elif event.key() == Qt.Key_X:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() + 500)

        elif event.key() == Qt.Key_Y:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() - 500)

        elif event.key() == Qt.Key_T:
            if self.mediaPlayer.isMuted():
                self.mediaPlayer.setMuted(False)
            else:
                self.mediaPlayer.setMuted(True)


        elif event.key() == Qt.Key_F:

            self.liberoInOut(self.lineup)

        elif event.key() == Qt.Key_Space:

            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()

            else:
                self.mediaPlayer.play()

        elif event.key() == Qt.Key_Return:
            s = self.text()
            if re.fullmatch(r"[0-9A-Za-z]+((&([0-9A-Za-z]+)){0,2})#[SRDABZ]([+0E/-]|(--)|(\+\+)),?\s?( [0-9A-Za-z]+#[SRDABZ]([+0E/-]|(--)|(\+\+)),\s?)*",
                            s):
                s_l = s.split(',')
                sec_back = len(s_l)
                for i in s_l:
                    if i.strip() != '':
                        i = i.strip()
                        i_list = i.split('#')
                        for j in i_list:
                            if (j.count('&') > 0) and (j.count('&') < 3):
                                players = j.split('&')
                                if i_list[1][0] == 'B':
                                    print(len(players))
                                    if len(players) == 2:
                                        med = MediaPl(self.mediaPlayer)
                                        zeit = str((med.get_time() / 1000) - sec_back)
                                        try:
                                            add_two_node(self.cur_game, players[0], players[1], 'Doppelblock', zeit,
                                                         self.counter, i_list[1][1:])
                                        except:
                                            print('Fehler beim Doppelblock: Werte: ' + self.cur_game + ' ' + players[
                                                0] + ' ' + players[1] + ' ' + zeit + ' ' + self.counter + ' ' +
                                                  i_list[1][1:])
                                        sec_back = sec_back - 1
                                        # self.clear()
                                        self.inc_counter()
                                        break

                                    if len(players) == 3:
                                        med = MediaPl(self.mediaPlayer)
                                        zeit = str((med.get_time() / 1000) - sec_back)
                                        try:
                                            add_three_node(self.cur_game, players[0], players[1], players[2], 'Dreierblock', zeit,
                                                         self.counter, i_list[1][1:])
                                        except:
                                            print('Fehler beim Dreierblock: Werte: ' + self.cur_game + ' ' + players[
                                                0] + ' ' + players[1] + ' ' + players[1] + ' ' + zeit + ' ' + self.counter + ' ' +
                                                  i_list[1][1:])
                                        sec_back = sec_back - 1
                                        # self.clear()
                                        self.inc_counter()
                                        break

                            else:
                                if i_list[1][0] == 'D':

                                    med = MediaPl(self.mediaPlayer)
                                    zeit = str((med.get_time() / 1000) - sec_back)
                                    try:
                                        add_node(self.cur_game, i_list[0], 'Verteidigung', zeit, self.counter,
                                                 i_list[1][1:])
                                    except:
                                        print('Fehler bei Abwehr: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                              ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:])
                                    sec_back = sec_back - 1
                                    self.laufer = "Abwehr"
                                    self.inc_counter()

                                    break
                                elif i_list[1][0] == 'Z':
                                    med = MediaPl(self.mediaPlayer)
                                    zeit = str((med.get_time() / 1000) - sec_back)
                                    try:
                                        add_node(self.cur_game, i_list[0], 'Zuspiel', zeit, self.counter, i_list[1][1:])
                                    except:
                                        print('Fehler bei Zuspiel: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                              ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:])
                                    sec_back = sec_back - 1
                                    self.inc_counter()
                                    break
                                elif i_list[1][0] == 'A':
                                    med = MediaPl(self.mediaPlayer)
                                    zeit = str((med.get_time() / 1000) - sec_back)
                                    sec_back = sec_back - 1
                                    try:
                                        add_node_laufer(self.cur_game, i_list[0], 'Angriff', zeit, self.counter,
                                                        i_list[1][1:], self.laufer)
                                    except:
                                        print('Fehler bei Abwehr: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                              ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:] + ' ' + self.laufer)
                                    self.laufer = ''
                                    self.inc_counter()
                                    break
                                elif i_list[1][0] == 'B':
                                    if not ('&' in i_list[0]):

                                        med = MediaPl(self.mediaPlayer)
                                        zeit = str((med.get_time() / 1000) - sec_back)
                                        try:
                                            add_node(self.cur_game, i_list[0], 'Block', zeit, self.counter, i_list[1][1:])
                                        except:
                                            print('Fehler bei Block: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                                  ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:])

                                        sec_back = sec_back - 1
                                        self.inc_counter()
                                        break
                                elif i_list[1][0] == 'S':
                                    med = MediaPl(self.mediaPlayer)
                                    zeit = str((med.get_time() / 1000) - sec_back)
                                    try:
                                        add_node(self.cur_game, i_list[0], 'Aufschlag', zeit, self.counter, i_list[1][1:])
                                    except:
                                        print('Fehler bei Aufschlag: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                              ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:])
                                    sec_back = sec_back - 1
                                    self.inc_counter()
                                    self.laufer = ''
                                    break
                                elif i_list[1][0] == 'R':
                                    med = MediaPl(self.mediaPlayer)
                                    zeit = str((med.get_time() / 1000) - sec_back)
                                    sec_back = sec_back - 1
                                    self.get_zuspiel_pos()
                                    try:
                                        add_node_laufer(self.cur_game, i_list[0], 'Annahme', zeit, self.counter,
                                                        i_list[1][1:], self.laufer)
                                    except:
                                        print('Fehler bei Abwehr: Werte: ' + self.cur_game + ' ' + i_list[0] +
                                              ' ' + zeit + ' ' + self.counter + ' ' + i_list[1][1:] + ' ' + self.laufer)
                                    self.inc_counter()
                                    break
                self.clear()
            else:
                self.dia_warn('Bitte überprüfen sie Ihre Eingabe')

    def liberodrin(self, listen):
        for i in listen:
            if (i[1] == 'Libero') and (i[2] != '0'):
                return True
        return False

    def liberoInOut(self, lineup):
        for outer in lineup:
            if outer[2] == '0':
                outerpos = lineup.index(outer)
        if self.liberodrin(lineup):
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
            self.libero1.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
            labelCourt.setText(tmp)
            labelCourt.setStyleSheet("background-color: rgb(216,155,92); border: 2px; font: bold 14px;")

        elif not self.liberodrin(lineup):
            for p in lineup:
                if (p[1] == 'Mitte') and ((p[2] == '1') or (p[2] == '6') or (p[2] == '5')):
                    mittePosition = p[2]

            if mittePosition == '1':
                labelCourt = self.pos1
                print('label end2')
            if mittePosition == '6':
                labelCourt = self.pos6
                print('label end2')
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
            labelCourt.setStyleSheet("background: #9acd32; border-radius: 20px; font: bold 14px;")
            print('label end')
        else:
            None

    def rotieren(self, label1, label2, label3, label4, label5, label6):

        for item in self.lineup:
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

        for player in self.lineup:
            if (player[1] == 'Libero') and (player[2] != 0):
                if player[2] == '6':
                    label1.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
                    label6.setStyleSheet("background: #9acd32; border-radius: 20px; font: bold 14px;")
                if player[2] == '5':
                    label6.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
                    label5.setStyleSheet("background: #9acd32; border-radius: 20px; border: 2px; font: bold 14px;")

        tmp = label1.text()
        label1.setText(label2.text())
        label2.setText(label3.text())
        label3.setText(label4.text())
        label4.setText(label5.text())
        label5.setText(label6.text())
        label6.setText(tmp)

        for outer in self.lineup:
            if outer[2] == '0':
                outerpos = self.lineup.index(outer)

        for i in self.lineup:
            if (i[1] == 'Libero') and (i[2] == '4'):
                tmp = i[2]
                i[2] = self.lineup[outerpos][2]
                self.lineup[outerpos][2] = tmp
                tmp = self.libero1.text()
                self.libero1.setText(label4.text())
                self.libero1.setStyleSheet("background-color: lightGray; border: 2px; font: bold 14px;")
                label4.setText(tmp)
                label4.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
                label5.setStyleSheet("background-color: #ff9900; border: 2px; font: bold 14px;")
