import sqlite3
from operator import index
import json


def connect_db(function):
    def con(table_name, *args):
        connection = sqlite3.connect("VolleyScout2.db", isolation_level=None)
        cursor = connection.cursor()
        try:
            result = function(cursor, table_name, *args)
            connection.commit()
            return result
        finally:
            connection.close()

    return con


@connect_db
def update_stat(cursor, table_name, number:str, stat_value:str  , new_value:str):
    cmd = f"UPDATE {table_name} SET {stat_value} = '{new_value}' WHERE Number = {number}"
    cursor.execute(cmd)

@connect_db
def select_stat(cursor, table_name, number:str, stat_value:str):
    cmd = f"SELECT {stat_value} FROM {table_name} WHERE Number = {number}"
    cursor.execute(cmd)
    row = cursor.fetchone()
    return row[0]

@connect_db
def set_new_id(cursor, table_name):
    cmd = "SELECT MAX(ID) FROM " + table_name
    cursor.execute(cmd)
    row = cursor.fetchone()
    if row[0] == None:
        return "1"
    else:
        return str(int(row[0])+1)

@connect_db
def insert_action_in_table(cursor, table_name, number, action, evaluation, timestamp, details = ""):
    new_id = set_new_id(table_name)
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)

        rotation = data["rotation"]
    print("rotation")
    print(rotation)
    cmd = "INSERT INTO " + table_name + " (NUMBER, ACTION, EVALUATION, ROTATION, TIMESTAMP, DETAILS, ID) VALUES (?, ?, ?, ?, ? ,?, ?)"
    cursor.execute(cmd, (number, action, evaluation, rotation, timestamp, details, new_id))



def get_all_table_names(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    rows = cursor.fetchall()
    connection.close()

    return rows

def get_all_numbers(db_name, table_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"SELECT NUMBER FROM {table_name}")
    rows = cursor.fetchall()
    connection.close()

    return rows

def get_team_values(db_name, team_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {team_name}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def check_table_exists(database:str, table_name: str) -> bool:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    listOfTables = []
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        listOfTables = cursor.execute(f"SELECT * FROM {table_name};").fetchall()

    except sqlite3.OperationalError:
        pass
    connection.close()
    if listOfTables == []:

        return False
    else:
        return True


def create_new_team(team_name):
    connection = sqlite3.connect('Teams.db')
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {team_name} (NAME TEXT,NUMBER TEXT)")
    connection.close()

def insert_player_in_table(team_name, number, player_name):
    connection = sqlite3.connect('Teams.db', isolation_level=None)
    cursor = connection.cursor()
    #cmd = "INSERT INTO " + team_name + " (NUMBER, NAME) VALUES (?, ?)"
    cmd = f"INSERT INTO {team_name} (NUMBER, NAME) VALUES ('{number}', '{player_name}')"
    #cursor.execute(cmd, (number, player_name))
    cursor.execute(cmd)
    print("Ende")
    connection.close()



def instert_points(table_name):
    connection = sqlite3.connect('VolleyScout2.db')





def create_table(table_name):
    connection = sqlite3.connect('VolleyScout2.db')
    cursor = connection.cursor()
    cmd = f"CREATE TABLE IF NOT EXISTS {table_name} (Number TEXT,Action TEXT,Evaluation TEXT,Rotation TEXT,Timestamp TEXT, Points_Data TEXT, Service_Data TEXT, Reception_Data TEXT, Attack_Data TEXT, Block_Data TEXT, Details TEXT, ID TEXT)"
    cursor.execute(cmd)

    connection.close()

@connect_db
def insert_start_values(cursor, table_name, number):

    cmd = f"UPDATE {table_name} SET Points_Data = '0/0/0', Service_Data = '0/0/0', Reception_Data = '0/0/0/0', Attack_Data = '0/0/0/0/0', Block_Data = '0' WHERE Number = {number}"
    cursor.execute(cmd)

def get_stats_points_values(db_name, table_name):
    set_list = {"Satz 1": "Set1_points", "Satz 2": "Set2_points", "Satz 3": "Set3_points", "Satz 4": "Set4_points", "Satz 5": "Set5_points"}
    with open("./Data/Current_Set.txt") as f:  # in write mode
        current_set = f.read()
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"SELECT {set_list[current_set]} FROM {table_name} WHERE {set_list[current_set]} IS NOT NULL")
    rows = cursor.fetchall()
    connection.close()
    return rows[0][0]

def update_stats_points_values(db_name, table_name, action):
    set_list = {"Satz 1": "Set1_points", "Satz 2": "Set2_points", "Satz 3": "Set3_points", "Satz 4": "Set4_points",
                "Satz 5": "Set5_points"}
    current_set_list = {"Satz 1": "Set1", "Satz 2": "Set2", "Satz 3": "Set3", "Satz 4": "Set4",
                "Satz 5": "Set5"}
    with open("./Data/Current_Set.txt") as f:  # in write mode
        current_set = f.read()

    action_list = {"S" : 0, "A" : 1, "B" : 2, "GgFhl" : 3}
    old_values = get_stats_points_values(db_name, table_name).split("/")
    print(old_values)
    new_value = int(old_values[action_list[action]]) + 1
    old_values[action_list[action]] = str(new_value)
    old_values = "/".join(old_values)
    print(old_values)
    connection = sqlite3.connect('VolleyScout2.db')
    cursor = connection.cursor()
    cmd = f"UPDATE {table_name} SET {set_list[current_set]} = '{old_values}' WHERE Current_Set = '{current_set_list[current_set]}'"
    print(type(old_values))
    print(cmd)
    cursor.execute(cmd)
    connection.commit()
    connection.close()
@connect_db
def update_stats_action_values(cursor,table_name, action, rating):
    current_set_list = {"Satz 1": "Set1", "Satz 2": "Set2", "Satz 3": "Set3", "Satz 4": "Set4",
                        "Satz 5": "Set5"}
    index_list = {"S++" : [0,2], "S--" : [0,1],"R++" : [0,2,3], "R+" : [0,2], "R--" : [0,1], "A++" : [0,3], "A--" : [0,1], "A-":[0,2], "B++":[0]}
    action_list = {"S" : "_service", "A" : "_attack", "B" : "_block", "R": "_reception"}
    with open("./Data/Current_Set.txt") as f:  # in write mode
        current_set = f.read()
    column_name = f"{current_set_list[current_set]}{action_list[action]}"
    cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {column_name} IS NOT NULL")
    rows = cursor.fetchall()
    old_values = rows[0][0]
    action_rating = f"{action}{rating}"
    idx = index_list[action_rating]
    result = increase_value_stats_string(old_values, idx)
    cmd = f"UPDATE {table_name} SET {column_name} = '{result}' WHERE Current_Set = '{current_set_list[current_set]}'"
    cursor.execute(cmd)







def increase_value_stats_string(stats_string:str, idx):
    if not idx:
        return stats_string
    else:

        stats_string = stats_string.split("/")
        new_value = int(stats_string[idx[0]]) + 1
        stats_string[idx[0]] = str(new_value)
        stats_string = "/".join(stats_string)
        idx.pop(0)


        return increase_value_stats_string(stats_string, idx)



@connect_db
def insert_start_values_set(cursor, table_name):
    cmd = f"INSERT INTO {table_name} (Current_Set) VALUES ('Set1')"
    cursor.execute(cmd)
    cmd = f"INSERT INTO {table_name} (Current_Set) VALUES ('Set2')"
    cursor.execute(cmd)
    cmd = f"INSERT INTO {table_name} (Current_Set) VALUES ('Set3')"
    cursor.execute(cmd)
    cmd = f"INSERT INTO {table_name} (Current_Set) VALUES ('Set4')"
    cursor.execute(cmd)
    cmd = f"INSERT INTO {table_name} (Current_Set) VALUES ('Set5')"
    cursor.execute(cmd)

@connect_db
def insert_start_values_sets_stats(cursor, table_name):
    cmd = f"UPDATE {table_name} SET Set1_points = '0/0/0/0', Set1_service = '0/0/0', Set1_reception = '0/0/0/0', Set1_attack = '0/0/0/0/0', Set1_block = '0' WHERE Current_Set = 'Set1'"
    cursor.execute(cmd)

    cmd = f"UPDATE {table_name} SET Set2_points = '0/0/0/0', Set2_service = '0/0/0', Set2_reception = '0/0/0/0', Set2_attack = '0/0/0/0/0', Set2_block = '0' WHERE Current_Set = 'Set2'"
    cursor.execute(cmd)
    cmd = f"UPDATE {table_name} SET Set3_points = '0/0/0/0', Set3_service = '0/0/0', Set3_reception = '0/0/0/0', Set3_attack = '0/0/0/0/0', Set3_block = '0' WHERE Current_Set = 'Set3'"
    cursor.execute(cmd)
    cmd = f"UPDATE {table_name} SET Set4_points = '0/0/0/0', Set4_service = '0/0/0', Set4_reception = '0/0/0/0', Set4_attack = '0/0/0/0/0', Set4_block = '0' WHERE Current_Set = 'Set4'"
    cursor.execute(cmd)
    cmd = f"UPDATE {table_name} SET Set5_points = '0/0/0/0', Set5_service = '0/0/0', Set5_reception = '0/0/0/0', Set5_attack = '0/0/0/0/0', Set5_block = '0' WHERE Current_Set = 'Set5'"
    cursor.execute(cmd)

@connect_db
def insert_start_values_game_stats(cursor, table_name):
    cmd = f"INSERT INTO {table_name} (game_stats) VALUES ('game_stats')"
    cursor.execute(cmd)

@connect_db
def insert_start_values_rotation_stats(cursor, table_name):

    cmd = f"UPDATE {table_name} SET rotation_1_difference = '0/0', rotation_2_difference = '0/0', rotation_3_difference = '0/0', rotation_4_difference = '0/0', rotation_5_difference = '0/0', rotation_6_difference = '0/0' WHERE game_stats = 'game_stats'"
    cursor.execute(cmd)

@connect_db
def update_stat_set(cursor, table_name, stat_value:str  , new_value:str):
    cmd = f"UPDATE {table_name} SET {stat_value} = '{new_value}'"
    cursor.execute(cmd)
"""
@connect_db
def get_stat_set(cursor, table_name, stat_value:str :
    cmd = f"UPDATE {table_name} SET {stat_value} = '{new_value}'"
    cursor.execute(cmd)
"""

def insert_number(table_name, number) -> None:
    connection = sqlite3.connect('VolleyScout2.db')
    cursor = connection.cursor()
    cmd = f"INSERT INTO {table_name} (Number) VALUES (?)"
    cursor.execute(cmd, [number])
    connection.commit()
    connection.close()

#@connect_db
def insert_starting_lines_stats(table_name, numbers) -> None:
    for number in numbers:
        number = str(number)
        insert_start_values(table_name, number)


def select_in_table(table, target, **kwargs):
    connection_insert = sqlite3.connect('VolleyScout2.db')
    cursor_insert = connection_insert.cursor()
    base = "SELECT " + target + " FROM " + table
    result = []
    counter = len(kwargs)
    if len(kwargs) > 0:
        base = base + " WHERE"
        counter = len(kwargs)

        for key, value in kwargs.items():

            if counter > 1:
                base = base + " " + str(key) + "= '" + str(value) + "' AND"
                counter = counter - 1
            else:
                base = base + " " + str(key) + " = '" + str(value) + "'"
                #base = base + " " + str(value) + " = " + str(key)
    cursor_insert.execute(base)
    for row in cursor_insert.fetchall():
        result.append(row[0])

    connection_insert.commit()
    connection_insert.close()
