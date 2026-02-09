from XMLFunctions import XMLFuctions
from DBFunctions import *
import DBFunctions
import re
import json
import os

from workspace.VolleyScout.Testing import result


class PlayersUpdate:
    def __init__(self, command, players_label, time_stamp, table_name):
        self.table_name = table_name
        self.player_number = None
        self.time_stamp = time_stamp
        self.action = None
        self.players_label = players_label
        self.command = command
        self.counter_success = None
        self.detail = None
        self.rating = None
        self.rotation = ""


    def start(self):

        self.extract_possible_details()
        self.extract_player_number()
        self.extract_action()
        self.extract_rating()

        if self.action == "B" and (self.rating == "++" or self.rating == "--"):
            self.update_db_stats_block()
            self.update_label_block()
            self.update_label_points()

        if self.action == "S":
            self.set_possible_rotation()
            self.update_db_stats_service()
            self.update_label_service()
            self.update_label_points()
            self.set_rotation_to_default()

        if self.action == "R":
            self.set_possible_rotation()
            self.update_db_stats_reception()
            self.update_label_reception()

        if self.action == "D":
            self.set_rotation_to_defense()

        if self.action == "A":
            self.set_possible_rotation()
            self.update_db_stats_attack()
            self.update_label_attack()
            self.update_label_points()
            self.update_set_stat("A")
        self.insert_action_db()

        if self.action in ["S", "A", "B"] and self.rating == "++":
            self.update_db_set_stats_points()
            self.update_set_stat(self.action)

        if self.action == "GgFhl":
            self.update_db_set_stats_points()
            self.update_set_stat(self.action)
        if not self.action in ["Z", "D"]:
            self.update_db_stats_action()
            self.update_label_set_stats()

    def set_rotation_to_defense(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)
        data["rotation"] = "defense"
        with open("./Data/Line_up_data.json", "r+") as f:
            json.dump(data, f)

    def set_possible_rotation(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

        line_up = data["line_up"]
        setter = data["setter"]

        idx = line_up.index(setter)


        idx = idx + 1
        self.rotation ="rotation"+str(idx)
        data["rotation"] = "rotation"+str(idx)
        with open("./Data/Line_up_data.json", "r+") as f:
            json.dump(data, f)

    def set_rotation_to_default(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

            data["rotation"] = ""

        file_path = "./Data/Line_up_data.json"
        try: os.remove(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        with open("./Data/Line_up_data.json", "w") as f:
            json.dump(data, f)

    def update_label_set_stats(self):

        connection = sqlite3.connect('VolleyScout2.db')
        cursor = connection.cursor()
        current_set_list = {"Satz 1": "Set1", "Satz 2": "Set2", "Satz 3": "Set3", "Satz 4": "Set4",
                            "Satz 5": "Set5"}
        set_index = {"Satz 1": 0, "Satz 2": 1, "Satz 3": 2, "Satz 4": 3, "Satz 5": 4}
        index_list = {"S++": [0, 2], "S--": [0, 1], "R++": [0, 2, 3], "R+": [0, 2], "R--": [0, 1], "A++": [0, 3],
                  "A--": [0, 1], "A-": [0, 2], "B++": [0]}
        action_list = {"S": "_service", "A": "_attack", "B": "_block", "R": "_reception"}
        with open("./Data/Current_Set.txt") as f:  # in write mode
            current_set = f.read()
        action_rating = f"{self.action}{self.rating}"
        column_name = f"{current_set_list[current_set]}{action_list[self.action]}"
        cursor.execute(f"SELECT {column_name} FROM {self.table_name} WHERE {column_name} IS NOT NULL")
        rows = cursor.fetchall()

        new_values = rows[0][0]


        connection.close()
        new_values = new_values.split("/")

        match self.action:
            case "S":
                for idx in index_list[action_rating]:
                    self.players_label.player_frame.all_labels_set[set_index[current_set]].result_labels_service[idx].setText(new_values[idx])
            case "A":
                for idx in index_list[action_rating]:
                    self.players_label.player_frame.all_labels_set[set_index[current_set]].result_labels_attack[idx].setText(new_values[idx])
            case "R":
                for idx in index_list[action_rating]:
                    self.players_label.player_frame.all_labels_set[set_index[current_set]].result_labels_reception[idx].setText(new_values[idx])
            case "B":
                for idx in index_list[action_rating]:
                    self.players_label.player_frame.all_labels_set[set_index[current_set]].result_labels_block[idx].setText(new_values[idx])

    def update_db_stats_action(self):
        action_rating = f"{self.action}{self.rating}"
        index_list = ["S++", "S--", "R++", "R+", "R--", "A++","A--", "A-", "B++"]
        if action_rating in index_list:
            DBFunctions.update_stats_action_values(self.table_name, self.action, self.rating)

    def update_db_set_stats_points(self):
        DBFunctions.update_stats_points_values("VolleyScout2.db", self.table_name, self.action)


    def insert_action_db(self):
        dict_values = {"S": "Service", "R": "Reception", "A": "Attack", "B": "Block", "Z":"Setting", "D":"Defense"}
        print("Yo")
        print(dict_values[self.action])
        DBFunctions.insert_action_in_table(self.table_name, self.player_number, dict_values[self.action], self.rating, self.time_stamp)
        print("Yo2")

    def update_db_stats_attack(self):
        #Format Ges/Fhl/Blo/Pkt/Pkt%

        result_values = DBFunctions.select_stat(self.table_name, self.player_number, "Attack_Data").split("/")
        tmp_value = str(int(result_values[0]) + 1)
        result_values[0] = tmp_value
        if self.rating == "--":
            tmp_value = str(int(result_values[1]) + 1)
            result_values[1] = tmp_value
        if self.rating == "B":
            tmp_value = str(int(result_values[2]) + 1)
            result_values[2] = tmp_value
        if self.rating == "++":
            tmp_value = str(int(result_values[3]) + 1)
            result_values[3] = tmp_value

        result_values = "/".join(result_values)
        DBFunctions.update_stat(self.table_name, self.player_number, "Attack_Data", str(result_values))
        self.update_db_points()

    def update_label_attack(self):
        value_total = DBFunctions.select_stat(self.table_name, self.player_number, "Attack_Data").split("/")
        for player in self.players_label.player_frame.stat_list:
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_attack[0].setText(value_total[0])
                player.result_labels_attack[1].setText(value_total[1])
                player.result_labels_attack[2].setText(value_total[2])
                player.result_labels_attack[3].setText(value_total[3])
                player.result_labels_attack[4].setText(str(int((int(value_total[3]) / int(value_total[0]) * 100))))
                break

    def update_set_stat(self, action):
        values = DBFunctions.get_stats_points_values("VolleyScout2.db", self.table_name).split("/")
        values_index = {"S" : 0, "A" : 1, "B" : 2, "GgFhl" : 3 }
        set_index = {"Satz 1" : 0, "Satz 2" : 1, "Satz 3" : 2, "Satz 4" : 3, "Satz 5" : 4}
        f = open("./Data/Current_Set.txt")
        self.players_label.player_frame.all_labels_set[set_index[f.read()]].result_labels_points[values_index[self.action]].setText(values[values_index[action]])



    def add_one_to_label(self, label):
        if label.text() == ".":
            label.setText("1")
        else:
            result = int(label.text()) + 1
            label.setText(str(result))


    def update_label_reception(self):
        value_total = DBFunctions.select_stat(self.table_name, self.player_number, "Reception_Data").split("/")
        for player in self.players_label.player_frame.stat_list:
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_reception[0].setText(value_total[0])
                player.result_labels_reception[1].setText(value_total[1])
                player.result_labels_reception[2].setText(str(int((int(value_total[2]) / int(value_total[0])*100))))
                player.result_labels_reception[3].setText(str(int((int(value_total[3]) / int(value_total[0])*100))))
                break

    def update_db_stats_reception(self):
        #Liste reception = [Ges/Fehler/Pos/Perf]
        result_values = DBFunctions.select_stat(self.table_name, self.player_number, "Reception_Data").split("/")
        tmp_value = str(int(result_values[0]) + 1)
        result_values[0] = tmp_value
        if self.rating == "+":
            tmp_value = str(int(result_values[2]) + 1)
            result_values[2] = tmp_value
        if self.rating == "++":
            tmp_value = str(int(result_values[2]) + 1)
            result_values[2] = tmp_value
            tmp_value = str(int(result_values[3]) + 1)
            result_values[3] = tmp_value
        if self.rating == "--":
            tmp_value = str(int(result_values[1]) + 1)
            result_values[1] = tmp_value

        result_values = "/".join(result_values)
        DBFunctions.update_stat(self.table_name, self.player_number, "Reception_Data", str(result_values))

    def update_db_stats_service(self):
        #result =  list(DBFunctions.select_stat(self.table_name, self.player_number, "Service_Data"))
        #print(result)
        result = DBFunctions.select_stat(self.table_name, self.player_number, "Service_Data").split("/")
        tmp_value = str(int(result[0]) + 1)
        result[0] = tmp_value
        if self.rating == "++":
            tmp_value = str (int(result[2]) + 1)
            result[2] = tmp_value
        if self.rating == "--":
            tmp_value = str(int(result[1]) + 1)
            result[1] = tmp_value

        result = "/".join(result)
        DBFunctions.update_stat(self.table_name, self.player_number, "Service_Data", str(result))
        self.update_db_points()


    def update_label_service(self):
        value_total = DBFunctions.select_stat(self.table_name, self.player_number, "Service_Data").split("/")
        for player in self.players_label.player_frame.stat_list:
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_service[0].setText(value_total[0])
                player.result_labels_service[1].setText(value_total[1])
                player.result_labels_service[2].setText((value_total[2]))
                break




    def update_db_stats_block(self):
        dict_values = {"S": "Service_Data", "R": "Reception_Data", "A": "Attack_Data", "B": "Block_Data"}
        if self.rating == "++":
            new_value = int (DBFunctions.select_stat(self.table_name, self.player_number, "Block_Data")) + 1

            DBFunctions.update_stat(self.table_name, self.player_number, "Block_Data", str(new_value))

        self.update_db_points()

    def update_label_block(self):
        value = DBFunctions.select_stat(self.table_name, self.player_number, "Block_Data")
        for player in self.players_label.player_frame.stat_list :
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_block[0].setText(value)
                break

    def update_label_points(self):
        value_total = DBFunctions.select_stat(self.table_name, self.player_number, "Points_Data").split("/")
        for player in self.players_label.player_frame.stat_list :
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_points[0].setText(value_total[0])

                player.result_labels_points[2].setText(str(int(value_total[0]) - int(value_total[2])))
                break

    def update_db_points(self):
        if self.rating == "++":
            result = DBFunctions.select_stat(self.table_name, self.player_number, "Points_Data").split("/")
            tmp_value = int (result[0]) + 1
            result[0] =str(tmp_value)
            result ="/".join(result)
            DBFunctions.update_stat(self.table_name, self.player_number, "Points_Data", str(result))
        if self.rating == "--":
            result = DBFunctions.select_stat(self.table_name, self.player_number, "Points_Data").split("/")
            new_value = int (result[2]) + 1
            result[2] =str(new_value)
            result ="/".join(result)
            DBFunctions.update_stat(self.table_name, self.player_number, "Points_Data", str(result))

    def extract_possible_details(self):
        if "(" in self.command:
            self.detail = self.command.split("(")[1][:-1]
            self.command = self.command.split("(")[0]


    def extract_player_number(self):
        if self.command[0].isdigit() and self.command[1].isdigit():
            self.player_number = str(self.command[0:2])
            self.command = self.command[2:]
        else:
            self.player_number = str(self.command[0:1])
            self.command = self.command[1:]

    def extract_action(self):
        self.action = self.command[0]
        self.command = self.command[1:]

    def extract_rating(self):
        self.rating = self.command[0:]








    def update_percent(self,action):
        pass




    def update_right_label(self,action :str, player_number :str):
        pass

    def update_values(self, command, action):
        pass