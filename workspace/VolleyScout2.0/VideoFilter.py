from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QComboBox
import JsonFunctions
from icecream import ic
import  DBFunctions


class VideoFilter(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        ic()
        self.resize(270, 250)
        self.setWindowTitle("Video Filter")
        self.layout = QVBoxLayout()
        self.label_games = QLabel("Wählen Sie ein Spiel aus :")
        self.games_box = QComboBox()
        self.confirm_game_button = QPushButton("Spiel wählen")
        self.label_parameters = QLabel("Videos filtern mit den Parametern :")
        self.player_number_label = QLabel("Spielernummer : ")
        self.player_number_cb = QComboBox()
        self.action_label = QLabel("Aktion : ")
        self.action_cb = QComboBox()
        self.action_cb.addItems(["Aufschlag", "Annahme", "Abwehr", "Zuspiel", "Angriff", "Block"])
        self.rating_label = QLabel("Rating : ")
        self.rating_cb = QComboBox()
        self.rating_cb.addItems(["Alle","++", "+", "0", "-", "--"])
        self.situation_label = QLabel("Annahme/Abwehr/Läufer ")
        self.situation_cb = QComboBox()
        self.situation_cb.addItems(["Alle","Annahme", "Abwehr", "Läufer1", "Läufer2", "Läufer3", "Läufer4", "Läufer5", "Läufer6"])
        self.label_detail = QLabel("Detail :")
        self.detail_le = QLineEdit()
        names = DBFunctions.get_all_table_names("VolleyScout2.db")
        for name in names:
            self.games_box.addItem(name[0])

        self.layout_header = QHBoxLayout()
        self.layout_header.addWidget(self.label_games)
        self.layout_header.addWidget(self.games_box)
        self.layout_header.addWidget(self.confirm_game_button)
        self.layout_numbers = QHBoxLayout()
        self.layout_numbers.addWidget(self.player_number_label)
        self.layout_numbers.addWidget(self.player_number_cb)
        self.layout_action = QHBoxLayout()
        self.layout_action.addWidget(self.action_label)
        self.layout_action.addWidget(self.action_cb)
        self.layout_rating = QHBoxLayout()
        self.layout_rating.addWidget(self.rating_label)
        self.layout_rating.addWidget(self.rating_cb)
        self.layout_situation = QHBoxLayout()
        self.layout_situation.addWidget(self.situation_label)
        self.layout_situation.addWidget(self.situation_cb)
        self.layout_detail = QHBoxLayout()
        self.layout_detail.addWidget(self.label_detail)
        self.layout_detail.addWidget(self.detail_le)
        self.layout.addLayout(self.layout_header)
        self.layout.addWidget(self.label_parameters )
        self.layout.addLayout(self.layout_numbers)
        self.layout.addLayout(self.layout_action)
        self.layout.addLayout(self.layout_rating)
        self.layout.addLayout(self.layout_situation)
        self.layout.addLayout(self.layout_detail)
        self.setLayout(self.layout)

        self.confirm_game_button.clicked.connect(self.insert_player_numbers)

    def insert_player_numbers(self):
        self.player_number_cb.clear()
        numbers = DBFunctions.get_all_numbers("VolleyScout2.db",self.games_box.currentText())
        for number in numbers:
            ic(number[0])
            if number[0] is None:
               break
            else:
                self.player_number_cb.addItem(number[0])



