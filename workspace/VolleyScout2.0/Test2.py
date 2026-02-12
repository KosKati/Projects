import sqlite3
import sys
import JsonFunctions

import DBFunctions
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QWidget
from UpdatePlayers import PlayersUpdate
import MainWindow
#DBFunctions.create_table("Testgame2")
#DBFunctions.insert_start_values("Testgame")
#ps = DBFunctions.select_stat("Testgame", "4", "Points_Data")
#DBFunctions.insert_numbers("Testgame",[4,5,6])
#DBFunctions.update_stat("Testgame", "4", "Points_Data" , "1/0/1")
#val =DBFunctions.select_stat("Testgame", "4", "Points_Data")
#pl = PlayersUpdate("4B++(Diagonal)", "4", "3.45", "Testgame")
#pl.start()
import Rotations
#print(ps)
import json
#DBFunctions.update_stat("Testgame", 1, "Points_Data", "0/0/0")
#print("Max ID" + DBFunctions.select_max_id("Testgame2"))
#DBFunctions.insert_action_in_table("Testgame2", "2", "Service", "--", "4:15")
connection = sqlite3.connect('Teams.db', isolation_level=None)
#cursor = connection.cursor()
#cursor.execute("INSERT INTO prod_mast(prod_id, prod_name, prod_rate, prod_qc)VALUES(1, 'Pancakes', 75, 'OK');")
#cursor.execute(f"AlTER TABLE Testgame ADD Score TEXT")
#cursor.execute(f"AlTER TABLE Testgame ADD SO_Total_Points TEXT")
#cursor.execute(f"AlTER TABLE Testgame ADD BP_Total_Points TEXT")
#cursor.execute(f"AlTER TABLE Testgame ADD LineUp_LiberoSubs TEXT")
connection.close()
"""
numbers = []
rows = DBFunctions.get_all_numbers('Volleyscout2.db','game_data__k_e_1')
for i in range(0, len(rows) - 1):
    numbers.append(rows[i][0])

print(numbers)

connection = sqlite3.connect("VolleyScout2.db")
cursor = connection.cursor()
#listOfTables = []

listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for i in range(0,len(listOfTables)):
    cursor.execute(f"DROP TABLE {listOfTables[i][0]}")
print(listOfTables)
connection.close()

with open("./Data/Database_name.txt","w") as f: #in write mode
    f.write("{database}")


f = open("./Data/Database_name.txt")
database_name = f.read()
print(database_name)




connection = sqlite3.connect("Teams.db")
cursor = connection.cursor()
#listOfTables = []


cursor.execute(f"DROP TABLE EW_Dam1")
connection.close()

connection = sqlite3.connect("VolleyScout2.db")
cursor = connection.cursor()
#listOfTables = []

listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for i in range(0,len(listOfTables)):
    cursor.execute(f"DROP TABLE {listOfTables[i][0]}")
connection.close()

action_list = {"Satz 1": "Set1_points", "Satz 2": "Set2_points", "Satz 3": "Set3_points", "Satz 4": "Set4_points", "Satz 5": "Set5_points"}
with open("./Data/Current_Set.txt") as f:  # in write mode
    current_set = f.read()
print(current_set)
print(action_list[current_set])

cur_set = "Set1"
connection = sqlite3.connect("VolleyScout2.db")
cursor = connection.cursor()
cmd = f"UPDATE game_data_1_1_1 SET Set1_points = '1/0/0/0' WHERE Current_Set = '{cur_set}'"
#cmd = "Select Set1_points from game_data_1_1_1 WHERE Current_Set = 'Set1'"
cursor.execute(cmd)
connection.commit()
#rows = cursor.fetchall()
#print(rows)
connection.close()

#rows = DBFunctions.get_stats_points_values("VolleyScout2.db","game_data_1_1_1")
#print(rows[0][0])

#DBFunctions.update_stats_action_values("game_data_564_56_56", "S", "++")

#Rotations.write_current_positions(["2", "3", "4", "5", "6", "7"])

line_up = ["1","2", "3", "4", "5", "6"]
tmp = line_up.pop(0)
print(line_up)
line_up.append(tmp)
print(line_up)


tmp = line_up.pop(0)
print(line_up)
line_up.append(tmp)
print(line_up)

tmp = line_up.pop(0)
print(line_up)
line_up.append(tmp)
print(line_up)
"""
connection = sqlite3.connect("VolleyScout2.db")
cursor = connection.cursor()
#listOfTables = []

listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for i in range(0,len(listOfTables)):
    cursor.execute(f"DROP TABLE {listOfTables[i][0]}")
print(listOfTables)
connection.close()