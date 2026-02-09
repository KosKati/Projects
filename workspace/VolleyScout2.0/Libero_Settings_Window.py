import json

from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton
import os

class LiberoSubPlayerSettings(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, player_labels):
        super().__init__()
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)
        players_number = data["line_up"]
        self.player_labels = player_labels
        self.layout = QVBoxLayout()
        self.sub_player_1_label = QLabel("Spieler 1 zum Wechseln")
        self.sub_player_1_selection = QComboBox()
        self.sub_player_2_label = QLabel("Spieler 2 zum Wechseln")
        self.sub_player_2_selection = QComboBox()
        self.button_layout = QHBoxLayout()
        self.button_confirm = QPushButton("Spieler speichern")
        self.button_cancel = QPushButton("Abbrechen")
        self.button_layout.addWidget(self.button_confirm)
        self.button_layout.addWidget(self.button_cancel)
        self.player1_layout = QHBoxLayout()
        self.player1_layout.addWidget(self.sub_player_1_label)
        self.player1_layout.addWidget(self.sub_player_1_selection)
        self.player2_layout = QHBoxLayout()
        self.player2_layout.addWidget(self.sub_player_2_label)
        self.player2_layout.addWidget(self.sub_player_2_selection)
        self.layout.addLayout(self.player1_layout)
        self.layout.addLayout(self.player2_layout)
        self.layout.addLayout(self.button_layout)
        self.resize(200, 100)
        self.setLayout(self.layout)
        for player in players_number:
            self.sub_player_1_selection.addItem(player)
            self.sub_player_2_selection.addItem(player)


        self.button_confirm.clicked.connect(self.set_subs)


    def set_subs(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)
        data["sub1"] = self.sub_player_1_selection.currentText()
        data["sub2"] = self.sub_player_2_selection.currentText()

        file_path = "./Data/Line_up_data.json"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        with open("./Data/Line_up_data.json", "w") as f:
            json.dump(data, f)

        self.close()


