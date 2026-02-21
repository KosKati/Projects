from XMLFunctions import XMLFuctions
from DBFunctions import *
import DBFunctions
import re
import json
import os
from icecream import ic
import JsonFunctions

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
            self.set_so_or_db_value()

        if self.action == "R":
            self.set_possible_rotation()
            self.update_db_stats_reception()
            self.update_label_reception()
            self.set_situation_to_json()
            self.set_so_or_db_value()
        if self.action == "D":
            self.set_rotation_to_defense()
            self.set_situation_to_json()

        if self.action == "A":
            self.set_possible_rotation()
            self.update_db_stats_attack()
            self.update_label_attack()
            self.update_label_points()
            self.update_set_stat("A")
            if self.rating in ["++", "--"]:
                self.set_possible_rotation_state()
                self.set_new_rotation_points_value()
            self.update_db_points_reception_defense()
            self.update_labels_points_reception_defense()
            self.update_db_so_or_db_value()
            self.update_db_or_so_labels()
        self.insert_action_db()
        if self.action in ["S", "A", "B"] and self.rating == "++":
            self.update_db_set_stats_points()
            self.update_set_stat(self.action)
        if self.action == "GgFhl":
            self.update_db_set_stats_points()
            self.update_set_stat(self.action)
        if not self.action in ["Z", "D"]:
            db_string = f"{self.action}{self.rating}"
            if db_string in ["S++", "S--", "R++", "R+", "R--", "A++", "A--", "A-", "B++"]:
                self.update_db_stats_action()
                self.update_label_set_stats()

    def update_db_or_so_labels(self):
        so_or_bp_value = JsonFunctions.get_so_or_bp()
        ic(so_or_bp_value)
        db_value_so_or_bp = DBFunctions.get_so_or_bp_value(self.table_name, so_or_bp_value)
        ic(db_value_so_or_bp)
        labels_so_or_bp = None
        string_label_3_1 = ""
        string_label_3_2 = ""
        if so_or_bp_value == "so":
            labels_so_or_bp = self.players_label.rece_window[1]
        if so_or_bp_value == "bp":
            labels_so_or_bp = self.players_label.serv_window[1]
        db_value_so_or_bp = db_value_so_or_bp.split("/")
        labels_so_or_bp[0].setText(db_value_so_or_bp[1])
        if int(db_value_so_or_bp[0]) > 0 :
            label3_value = str(round( (int(db_value_so_or_bp[1])/int(db_value_so_or_bp[0])),2))
        else:
            label3_value = "0.00"
        ic(label3_value)
        labels_so_or_bp[1].setText(db_value_so_or_bp[0])
        if so_or_bp_value == "bp":
            string_label_3_1 = "Auf"
            string_label_3_2 = "BP"

        if so_or_bp_value == "so":
            string_label_3_1 = "Ann"
            string_label_3_2 = "P"
        string_label_3 = f"Pro {label3_value} {string_label_3_1} \n 1 {string_label_3_2}"
        labels_so_or_bp[2].setText(string_label_3)

    def update_db_so_or_db_value(self):
        so_or_bp_value = JsonFunctions.get_so_or_bp()
        old_value = DBFunctions.get_so_or_bp_value(self.table_name,so_or_bp_value)
        attack_rating_value = f"{self.action}{self.rating}"
        ic(attack_rating_value)
        old_value = old_value.split("/")
        if attack_rating_value == "A++":
            old_value[0] = str(int(old_value[0]) + 1)
            old_value[1] = str(int(old_value[1]) + 1)
        if attack_rating_value in ["A+", "A--", "A-", "A0"]:
            old_value[1] = str(int(old_value[1]) + 1)

        new_value = "/".join(old_value)

        DBFunctions.update_values_so_bp_stats(self.table_name, so_or_bp_value, new_value)


    def set_so_or_db_value(self):
        if self.action == "S":
            JsonFunctions.set_so_or_bp("bp")
        if self.action == "R":
            JsonFunctions.set_so_or_bp("so")

    def update_labels_points_reception_defense(self):
        labels = None
        situation = JsonFunctions.get_situation()
        ic(situation)
        db_column_name = f"points_{situation}"
        ic(db_column_name)
        old_value = DBFunctions.get_game_stat_value(self.table_name,db_column_name)
        ic(old_value)
        old_value = old_value.split("/")
        ic(old_value)
        if situation == "good_reception":
            labels = self.players_label.game_stats.good_reception_labels
        if situation == "bad_reception":
            labels = self.players_label.game_stats.bad_reception_labels
        if situation == "defense":
            ic(situation)
            labels = self.players_label.game_stats.defense_labels
        for i in [0,1,3]:
            labels[i].setText(old_value[i])
        label2_value = str(int(int(old_value[2])/int(old_value[3])*100))
        labels[2].setText(label2_value)



    def update_db_points_reception_defense(self):
        situation = JsonFunctions.get_situation()
        db_column_name = f"points_{situation}"
        old_value = DBFunctions.get_game_stat_value(self.table_name,db_column_name)
        old_value = old_value.split("/")
        ic(old_value)
        if self.rating == "++":
            old_value[3] = str(int(old_value[3]) + 1)
            old_value[2] = str(int(old_value[2]) + 1)
        if self.rating == "--":
            old_value[3] = str(int(old_value[3]) + 1)
            old_value[0] = str(int(old_value[0]) + 1)

        if self.rating == "-":
            old_value[3] = str(int(old_value[3]) + 1)
            old_value[1] = str(int(old_value[1]) + 1)

        if self.rating in ["0", "+"]:
            old_value[3] = str(int(old_value[3]) + 1)

        new_value = "/".join(old_value)
        DBFunctions.update_game_stat_value(self.table_name, db_column_name, new_value)


    def set_situation_to_json(self):
        current_situation = ""
        if self.action == "R":
            if self.rating == "++" or self.rating == "+":
                current_situation = "good_reception"
            if self.rating == "-" or self.rating == "0":
                current_situation = "bad_reception"

        if self.action == "D":
            current_situation = "defense"

        JsonFunctions.set_situation(current_situation)

    def set_new_rotation_points_value(self):
        db_value = f"{self.rotation}_difference"
        label_position_list = {"rotation1" : 0, "rotation2" : 1, "rotation3" : 2, "rotation4" : 3, "rotation5" : 4, "rotation6" : 5}
        # For the test value = DBFunctions.get_rotation_difference_value(self.table_name, db_value)
        value = DBFunctions.get_game_stat_value(self.table_name, db_value)
        difference_rotation_points = str(int(value[0]) - int(value[2]))
        id(self.players_label.rotation_window[1])
        self.players_label.rotation_window[1][label_position_list[self.rotation]].setText(difference_rotation_points)

    def set_possible_rotation_state(self):
        rotations = ["rotation1", "rotation2", "rotation3", "rotation4", "rotation5", "rotation6"]
        new_value = None
        if self.rotation in rotations:
            db_value = f"{self.rotation}_difference"
            #For the test old_value = DBFunctions.get_rotation_difference_value(self.table_name, db_value)
            old_value = DBFunctions.get_game_stat_value(self.table_name, db_value)
            if self.rating == "++":
                new_value = str(int(old_value[0]) + 1) +"/" + old_value[2]
            if self.rating == "--":
                new_value = old_value[0] + "/" + str(int(old_value[2]) + 1)
            DBFunctions.update_rotation_difference_value(self.table_name, db_value, new_value)

    def set_rotation_to_defense(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)
        data["rotation"] = "defense"
        file_path = "./Data/Line_up_data.json"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        with open("./Data/Line_up_data.json", "w") as f:
            json.dump(data, f)

    def set_possible_rotation(self):
        with open("./Data/Line_up_data.json", "r+") as f:
            data = json.load(f)

        line_up = data["line_up"]
        setter = data["setter"]

        idx = line_up.index(setter)
        file_path = "./Data/Line_up_data.json"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")


        idx = idx + 1
        self.rotation ="rotation"+str(idx)
        data["rotation"] = "rotation"+str(idx)
        with open("./Data/Line_up_data.json", "w") as f:
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
        rating_values = {"++" : "plusplus", "+" : "plus", "0": "zero", "-" : "minus", "--" : "minusminus"}
        ic()
        ic([self.player_number, dict_values[self.action], self.rating])
        if self.detail:
            DBFunctions.insert_action_in_table(self.table_name, self.player_number, dict_values[self.action], rating_values[self.rating], self.time_stamp, self.detail)
        else:
            DBFunctions.insert_action_in_table(self.table_name, self.player_number, dict_values[self.action],
                                               rating_values[self.rating], self.time_stamp)

        ic()
    def update_db_stats_attack(self):
        #Format Ges/Fhl/Blo/Pkt/Pkt%

        result_values = DBFunctions.select_stat(self.table_name, self.player_number, "Attack_Data").split("/")
        ic("attack")
        ic(result_values)
        tmp_value = str(int(result_values[0]) + 1)
        result_values[0] = tmp_value
        if self.rating == "--":
            tmp_value = str(int(result_values[1]) + 1)
            result_values[1] = tmp_value
        if self.rating == "-":
            tmp_value = str(int(result_values[2]) + 1)
            result_values[2] = tmp_value
        if self.rating == "++":
            tmp_value = str(int(result_values[3]) + 1)
            result_values[3] = tmp_value
            ic()
        result_values[4] = str(int((int(result_values[3]) / int(result_values[0]) * 100)))
        ic()
        ic(result_values)
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
                player.result_labels_attack[4].setText(value_total[4])
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
        ic("labels")
        ic(value_total)
        for player in self.players_label.player_frame.stat_list:
            if player.result_labels_number[0].text() == self.player_number:
                player.result_labels_reception[0].setText(value_total[0])
                player.result_labels_reception[1].setText(value_total[1])
                player.result_labels_reception[2].setText(value_total[4])
                player.result_labels_reception[3].setText(value_total[5])
                break

    def update_db_stats_reception(self):
        #Liste reception = [Ges/Fehler/Pos/Perf]
        result_values = DBFunctions.select_stat(self.table_name, self.player_number, "Reception_Data").split("/")
        ic("go")
        ic(result_values)
        tmp_value = str(int(result_values[0]) + 1)
        result_values[0] = tmp_value

        ic(result_values[0])
        if self.rating == "+":
            result_values[2] = str(int(result_values[2]) + 1)

        if self.rating == "++":
            result_values[2] = str(int(result_values[2]) + 1)
            result_values[3] = str(int(result_values[3]) + 1)
        if self.rating == "--":
            tmp_value = str(int(result_values[1]) + 1)
            result_values[1] = tmp_value
        tmp_value_pos = str(int(int(result_values[2]) / int(result_values[0]) * 100))
        result_values[4] = tmp_value_pos
        tmp_value_per = str(int(int(result_values[3]) / int(result_values[0]) * 100))
        result_values[5] = tmp_value_per

        result_values = "/".join(result_values)
        ic(result_values)
        DBFunctions.update_stat(self.table_name, self.player_number, "Reception_Data", str(result_values))
        ic("ende")

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
        self.rating = str(self.command[0:])
