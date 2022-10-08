import csv
import os


class LineUpFunctions():

    def set_function(self, combobox_number, combobox_player):
        dir = os.path.dirname(__file__)
        dir = dir + "/Gamedata/CurrentTeam"
        allnumbers = []
        
        
        with open(dir) as csv_file:
            csv_reader_object = csv.reader(csv_file)

            for row in csv_reader_object:
                if len(row) == 2:
                    if(row[0] == combobox_number.currentText()):
                        combobox_player.setCurrentText(row[1])

    

    def set_lineup(self, labelcourt, comboboxdialog, playerlist, lineup, pos, player_functions):
        tmp = []
        tmp.append(comboboxdialog.currentText())
        for item in playerlist:
            if item[0] == comboboxdialog.currentText():
                tmp.append(player_functions.currentText())
        tmp.append(pos)
        lineup.append(tmp)
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
        