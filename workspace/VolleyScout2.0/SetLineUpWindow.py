from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import Rotations

class SetLineUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, court_labels):
        super().__init__()
        self.court_labels = court_labels
        self.resize(210, 270)
        self.setWindowTitle("Startaufstellung")
        self.layout = QVBoxLayout()
        self.all_line_edits = []
        self.starting_six =[]
        for i in range(1,7):
            self.tmp_layout = QHBoxLayout()
            self.tmp_line_edit = QLineEdit()
            self.tmp_line_edit.setText(str(i + 3))
            self.all_line_edits.append(self.tmp_line_edit)
            self.tmp_layout.addWidget(QLabel("Position: " + str(i) ))
            self.tmp_layout.addWidget(self.tmp_line_edit)
            self.layout.addLayout(self.tmp_layout)

        for i in range(1,3):
            self.tmp_layout = QHBoxLayout()
            self.tmp_line_edit = QLineEdit()
            self.tmp_line_edit.setText(str(i + 10))
            self.all_line_edits.append(self.tmp_line_edit)
            self.tmp_layout.addWidget(QLabel("Libero: " + str(i) ))
            self.tmp_layout.addWidget(self.tmp_line_edit)
            self.layout.addLayout(self.tmp_layout)

        self.setter_layout = QHBoxLayout()
        self.label_setter = QLabel("Zuspieler (Nummer):")
        self.line_edit_setter = QLineEdit()
        self.line_edit_setter.setText("9")
        self.line_edit_setter.setFixedWidth(40)
        self.setter_layout.addWidget(self.label_setter)
        self.setter_layout.addWidget(self.line_edit_setter)
        self.setLayout(self.layout)
        self.buttons_layout = QHBoxLayout()
        self.button_confirm = QPushButton("Bestätigen")
        self.button_abort = QPushButton("Abbrechen")
        self.buttons_layout.addWidget(self.button_confirm)
        self.buttons_layout.addWidget(self.button_abort)
        self.layout.addLayout(self.setter_layout)
        self.layout.addLayout(self.buttons_layout)
        #self.layout.addWidget(self.button_confirm)
        #self.layout.addWidget(self.button_abort)


        self.button_confirm.clicked.connect(self.set_line_up)

    def set_line_up(self):
        tmp_numbers = []
        for i in range(0,6):
            self.court_labels[i].setText(self.all_line_edits[i].text())
            tmp_numbers.append(self.all_line_edits[i].text())
        Rotations.write_current_positions(tmp_numbers)
        Rotations.write_setter_number_to_file((self.line_edit_setter.text()))
        Rotations.write_liberos(self.all_line_edits[6].text(), self.all_line_edits[7].text(), tmp_numbers[0:6],self.line_edit_setter.text())
        self.close()

