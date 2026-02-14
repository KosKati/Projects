import json
import os

from icecream import ic


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
        return data["sub1"]

def get_sub_2():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["sub2"]

def get_situation():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["situation"]

def get_so_or_bp():
    with open("./Data/Line_up_data.json", "r") as f:
        data = json.load(f)
        return data["so_or_bp"]

def set_so_or_bp(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["so_or_bp"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data, f)

def set_situation(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["situation"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)

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

def set_sub1(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["sub1"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)

def set_setter(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["setter"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)

def set_sub2(value):
    with open("./Data/Line_up_data.json", "r+") as f:
        data = json.load(f)
        data["sub2"] = value
    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(data,f)

def delete_old_json_file():
    file_path = "./Data/Line_up_data.json"
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


def delete_old_file():
    file_path = "./Data/Line_up_data.json"
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

