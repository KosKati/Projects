from PyQt5 import Combobox


class Player_combobox(Combobox):
    def __init__(self, parent, startvalue):
        Combobox.__init__(self, parent)
        self.startvlaue = startvalue
    