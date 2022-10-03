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
        