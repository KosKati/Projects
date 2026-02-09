
import sys
from argparse import Action

from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel,  QFormLayout, QPushButton, QGroupBox, QLineEdit, QDateEdit,QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
import os.path
import sqlite3


connection = sqlite3.connect('VolleyScout2.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS  game_data_EW1_VCW2 (
                    Number TEXT,
                    Action TEXT,
                    Evaluation TEXT,
                    Rotation TEXT,
                    Timestamp TEXT)''')

connection.close()


def insert_in_table(table_name, number, action, evaluation, rotation, timestamp):
    label = QLabel(table_name)
    connection_insert = sqlite3.connect('VolleyScout2.db')
    cursor_insert = connection_insert.cursor()
    cmd = "INSERT INTO "+ table_name+ " VALUES (?, ?, ?, ?, ?)"
    cursor_insert.execute(cmd , (number,action,evaluation,rotation,timestamp))
    connection_insert.commit()
    connection_insert.close()


def select_in_table(table, target, **kwargs):
    result =[]
    connection_insert = sqlite3.connect('VolleyScout2.db')
    cursor_insert = connection_insert.cursor()
    base = "SELECT " + target + " FROM " + table
    counter = len(kwargs)
    if len(kwargs) > 0:
        base = base + " WHERE"
        counter = len(kwargs)

        for key,value in kwargs.items():

            if counter > 1:
                base = base + " " + str(key) + "= '" + str(value) + "' AND"
                counter = counter - 1
            else:
                base = base + " " + str(key) + " = '" + str(value)+ "'"
                #base = base + " " + str(value) + " = " + str(key)
    cursor_insert.execute(base)
    for row in cursor_insert.fetchall():
        result.append(row[0])


    _SQL = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor_insert.execute(_SQL)
    results = cursor_insert.fetchall()
    print('All existing tables:', results)

    connection_insert.commit()
    connection_insert.close()

select_in_table("game_data_EW1_VCW2", "Timestamp",Action="Reception")
"""
insert_in_table(
    "game_data_EW1_VCW2","5","Servive", "-", "1", "19")
insert_in_table(
    "game_data_EW1_VCW2","1","Reception", "+", "2", "21")




p = "++"

if p == "++" or p == "+":
    print("yes")

from pathlib import Path
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

xml_file = Path("./Games/testgame.xml")
tree = ET.parse(xml_file)
root = tree.getroot()
players = root.find("players")
player = players.find("number_1")
value = player.find("attack").text

print(value)

player.find("attack").text = "2"
tree.write("./Games/testgame.xml")

xml_file = Path("./Games/testgame.xml")
tree = ET.parse(xml_file)
root = tree.getroot()
players = root.find("players")
player = players.find("number_1")
value = player.find("attack").text

print(value)



a = "12a++"


print(a[0].isdigit())
print(a[0].isdigit() and a[1].isdigit())
print(a[0].isdigit() and a[1].isdigit() and a[2].isdigit())
print(a[0:2])
a = a[2:]
print(a)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        
        script_dir  = Path(__file__)
        script_dir  = Path(__file__).parent
        print(script_dir)
        path  = Path(script_dir, "Images")
        print(path)
        directory = '.\\Teams\\'
        filename = "Volleyball_Half_Court.png"
        file_path = os.path.join(path, filename)
        
        label = QLabel(self)
        pixmap = QPixmap( "Pics/Volleyball_Half_Court.png")
        label.setPixmap(pixmap)
        parentlayout = QGridLayout()
        label0 = QLabel("")
        label1 = QLabel("Pos 1")
        parentlayout.addWidget(label0, 0, 0)
        parentlayout.addWidget(label1, 0,1)
        label2 = QLabel("Pos 2")
        label.setLayout(parentlayout)


        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
    

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
    
    

"""