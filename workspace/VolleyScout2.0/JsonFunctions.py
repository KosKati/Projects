import json
import os


def get_line_up():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["line_up"]

def get_libero_1():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["libero1"]

def get_libero_2():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["libero2"]

def get_warte():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["warte"]

def get_sub_1():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["sub_1"]

def get_sub_2():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["sub_2"]

def set_line_up(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["line_up"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)

def set_warte(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["warte"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)


def delete_old_file():
    file_path = "./Data/Line_up_data.json"
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

