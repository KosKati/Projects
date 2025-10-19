from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel,  QFormLayout, QPushButton, QGroupBox, QLineEdit, QDateEdit,QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
import os.path


class CourtWidgets(QWidget):

    def __init__(self):
        super().__init__()

        self.left_side = QGroupBox()
        left_side_layout = QGridLayout()
        label_1 = QLabel("Position1")
        label_1.setStyleSheet("padding-bottom: 200 px; text-align: top;")
        label_2 = QLabel("Position2")
        label_2.setStyleSheet("padding-bottom: 50 px; text-align: top;")
        label_3 = QLabel("Position3")
        label_3.setStyleSheet("padding-bottom: 50 px; text-align: top;")
        label_4 = QLabel("Position4")
        label_4.setStyleSheet("padding-bottom: 50 px; text-align: top;")
        label_5 = QLabel("Position5")
        label_5.setStyleSheet("padding-bottom: 200 px; text-align: top;")
        label_6 = QLabel("Position6")
        label_6.setStyleSheet("padding-bottom: 200 px; text-align: top;")
        left_side_layout.addWidget(label_1, 1, 2)
        left_side_layout.addWidget(label_2, 0, 2)
        left_side_layout.addWidget(label_3, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        left_side_layout.addWidget(label_4, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        left_side_layout.addWidget(label_5, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        left_side_layout.addWidget(label_6, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        label = QLabel("")
        label.setStyleSheet("background-color: lightgreen")
        self.left_side.setLayout(left_side_layout)

        self.team_window = QGroupBox()
        team_layout = QGridLayout()

        btn_rotation =QPushButton("Rotieren")
        btn_sub = QPushButton("Spielerwechsel")
        btn_libero = QPushButton("Libero in/out")
        btn_libero_chng = QPushButton("Libero wechseln/ersetzen")

        label_plyr_1 = QLabel("14 Dumpfbacke 123")
        label_plyr_2 = QLabel("P2")
        label_plyr_3 = QLabel("P3")
        label_plyr_4 = QLabel("P4")
        label_plyr_5 = QLabel("P5")
        label_plyr_6 = QLabel("P6")
        label_plyr_7 = QLabel("P7")
        label_plyr_8 = QLabel("P8")
        label_plyr_9 = QLabel("P9")
        label_plyr_10 = QLabel("P10")
        label_plyr_11 = QLabel("P11")
        label_plyr_12 = QLabel("P12")
        label_plyr_13 = QLabel("P13")
        label_plyr_14 = QLabel("P14")
        label_plyr_15 = QLabel("P15")
        label_plyr_16 = QLabel("P16")
        team_layout.addWidget(label_plyr_1, 0, 0)
        team_layout.addWidget(label_plyr_2, 0, 1)
        team_layout.addWidget(label_plyr_3, 0, 2)
        team_layout.addWidget(label_plyr_4, 0, 3)
        team_layout.addWidget(label_plyr_5, 0, 4)
        team_layout.addWidget(label_plyr_6, 1, 0)
        team_layout.addWidget(label_plyr_7, 1, 1)
        team_layout.addWidget(label_plyr_8, 1, 2)
        team_layout.addWidget(label_plyr_9, 1, 3)
        team_layout.addWidget(label_plyr_10, 1, 4)
        team_layout.addWidget(label_plyr_11, 2, 0)
        team_layout.addWidget(label_plyr_12, 2, 1)
        team_layout.addWidget(label_plyr_13, 2, 2)
        team_layout.addWidget(label_plyr_14, 2, 3)
        team_layout.addWidget(label_plyr_15, 2, 4)
        team_layout.addWidget(label_plyr_16, 3, 0)
        team_layout.addWidget(btn_rotation, 3, 1)
        team_layout.addWidget(btn_sub, 3, 2)
        team_layout.addWidget(btn_libero, 3, 3)
        team_layout.addWidget(btn_libero_chng, 3, 4)


        self.team_window.setLayout(team_layout)

