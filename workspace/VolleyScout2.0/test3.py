import re

list = ["","1"]

for i in range(0,len(list)):
    print(list[i].isdigit())

"""
string = "0/0/0/0/0/0"

def update(command, input_string):
    list_input = list(input_string)
    values = input_string.split("/")
    eval_dict = {"++": 1, "+": 2, "0": 3, "-": 4, "--": 5}
    eval_dict_write = {"++": 2, "+": 4, "0": 6, "-": 8, "--": 10}

    print("inner")
    print(values)
    counter_all = int(values[0]) + 1

    counter_success = int(values[eval_dict[command]]) + 1

    counter_percent = int(counter_success / counter_all * 100)

    list_input[0] = str(counter_all)
    list_input[eval_dict_write[command]] = str(counter_success)
    result = "".join(list_input)

    return result



print(update("+",update("++",string)))






txt =["1Z0++(h32:8iu)", "1A++", "1D--(AD)"]

match = re.fullmatch(r"(\d\d?[SRDABZ]([+0-]|(--)|(\+\+))(\(.*\))? (\):?(\(.*\))?))", txt[0])

def bool_match(commands):
    for t in commands:
        if re.fullmatch(r"(\d\d?[SRDABZ]([+0-]|(--)|(\+\+))((\(.*)?(:)?(.*\)))?)", t) is None :
            print("Fehler bei:" +t)
            return False
            break

    return True

def extract_details(command):
        command_left = command.split("(")[0]
        print(command_left)
        detail = command.split("(")[1][:-1]

        return command_left, detail

extract_details(txt[0])
s,a = extract_details(txt[0])
print(s)
print(a)
print(bool_match(txt))

from XMLFunctions import XMLFuctions
player_numbers = {"1","2","3","4","5","6","7","8","9"}
xml = XMLFuctions("")
xml.create_new_game("EW1", player_numbers)
"""