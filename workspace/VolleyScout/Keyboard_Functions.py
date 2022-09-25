from PyQt5.QtWidgets import QMessageBox


class Keyboard_func():
    def __init__(self):
        self.data = []

    def get_pos_four(self, lineUp, ist_laufer_eins):
        for i in lineUp:
            if ist_laufer_eins:
                if i[1] == 'Diagonal':
                    return i[0]
            else:
                if i[1] == 'Aussen' and (i[2] == '2' or i[2] == '3' or i[2] == '4'):
                    return i[0]


    def get_pos_two(self, lineUp, ist_laufer_eins):

        for i in lineUp:
            if  not ist_laufer_eins:
                if ((i[1] == 'Diagonal') and (i[2] == '2' or i[2] == '3' or i[2] == '4')) or ((i[1] == 'Zuspiel') and (i[2] == '2' or i[2] == '3' or i[2] == '4')) :
                    return i[0]
            else:
                if i[1] == 'Aussen' and (i[2] == '2' or i[2] == '3' or i[2] == '4'):
                    return i[0]


    def get_pos_one(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Diagonal') and (i[2] == '1' or i[2] == '6' or i[2] == '5') or (i[1] == 'Zuspiel') and (i[2] == '1' or i[2] == '6' or i[2] == '5') :
                    return i[0]


    def get_pos_three(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Mitte') and (i[2] == '2' or i[2] == '3' or i[2] == '4'):
                    return i[0]


    def get_pos_six(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Aussen') and (i[2] == '1' or i[2] == '6' or i[2] == '5'):
                    return i[0]

    def get_pos_five(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Mitte') and (i[2] == '1' or i[2] == '6' or i[2] == '5'):
                    return i[0]
                else:
                    for j in lineUp:
                        if(i[1] == 'Libero'):
                            return i[0]

    def get_zuspieler(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Zuspiel'):
                    return i[0]

    def get_diagonal(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Diagonal'):
                    return i[0]

    def get_front_outside(self, lineUp):
        for i in lineUp:
                if (i[1] == 'Aussen') and (i[2] == '2' or i[2] == '3' or i[2] == '4'):
                    return i[0]





