import csv
import os


class ComboBoxMethods:

    def filenamesToCombobox(self, box):
        box.addItem("---")
        dir = os.path.dirname(__file__)
        dir = dir + "/Teams"
        names = os.listdir(dir)
        for f in names:
            box.addItem(f)
"""
    def selectionchange(self, box):
        dir = os.path.dirname(__file__)
        dir = dir + "/Teams/" + box.currentText()
        print(dir)
        with open(dir) as csvfile:
            csv_reader_object = csv.reader(csvfile)
            for row in csv_reader_object:
                print()

"""
dir = os.path.dirname(__file__)
dir = dir + "/Teams"
print(dir)
