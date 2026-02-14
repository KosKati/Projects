from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
import JsonFunctions
from icecream import ic


class PlayerSubWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, court_labels):
        super().__init__()
        self.court_labels = court_labels
        self.resize(250, 150)
        self.setWindowTitle("Spielerwechsel")
        self.layout = QVBoxLayout()
        self.label_player_in = QLabel("Spieler rein:")
        self.label_player_out = QLabel("Spieler raus:")
        self.new_setter_label = QLabel("Neuer Zuspieler:")
        self.edit_player_in = QLineEdit()
        self.edit_player_out = QLineEdit()
        self.edit_new_setter = QLineEdit()
        self.layout_player_in = QHBoxLayout()
        self.layout_player_out = QHBoxLayout()
        self.layout_setter_change = QHBoxLayout()
        self.layout_setter_change.addWidget(self.new_setter_label)
        self.layout_setter_change.addWidget(self.edit_new_setter)
        self.layout_player_in.addWidget(self.label_player_in)
        self.layout_player_in.addWidget(self.edit_player_in)
        self.layout_player_out.addWidget(self.label_player_out)
        self.layout_player_out.addWidget(self.edit_player_out)
        self.layout.addLayout(self.layout_player_in)
        self.layout.addLayout(self.layout_player_out)
        self.layout.addLayout(self.layout_setter_change)
        self.button_confirm = QPushButton("OK")
        self.button_cancel = QPushButton("Abbrechen")
        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.button_confirm)
        self.layout_button.addWidget(self.button_cancel)
        self.layout.addLayout(self.layout_button)
        self.setLayout(self.layout)

        self.button_confirm.clicked.connect(self.confirm_clicked)
        self.button_cancel.clicked.connect(self.cancel_clicked)

    def confirm_clicked(self):
        ic()
        player_in = self.edit_player_in.text()
        player_out = self.edit_player_out.text()

        line_up = JsonFunctions.get_line_up()
        ic()
        for i in range(0,len(line_up)):
            if line_up[i] == player_out:
                line_up[i] = player_in
                JsonFunctions.set_line_up(line_up)
                break
        sub_1_value = JsonFunctions.get_sub_1()
        sub_2_value = JsonFunctions.get_sub_2()
        ic(sub_1_value)
        if player_out == sub_1_value:
            JsonFunctions.set_sub1(player_in)
        ic()
        if player_out == sub_2_value:
            JsonFunctions.set_sub1(player_in)
        ic()
        for i in range(0, len(self.court_labels)):
            if self.court_labels[i].text() == player_out:
                self.court_labels[i].setText(player_in)
                break

        if self.edit_new_setter.text():
            JsonFunctions.set_setter(self.edit_new_setter.text())
        ic()

    def cancel_clicked(self):
        self.close()