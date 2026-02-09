import json

def write_setter_number_to_file(number:str):
    with open("./Data/Current_Setter.txt", "w") as f:  # in write mode
        f.write(number)

def write_current_positions(numbers:list[str]):
    with open("./Data/Current_line_up.txt", "w") as f:  # in write mode
        result = numbers[0]
        for i in range(1, len(numbers)):
            result += ("/"+numbers[i])


        f.write(result)


def write_liberos(libero1:str, libero2:str, line_up, zuspieler:str):
    liberos_dict = {"line_up" : line_up, "libero1": libero1, "libero2" : libero2, "warte": "", "setter" : zuspieler, "rotation" : "", "sub1" : "" , "sub2" : "", "libero_io" : "out"}

    with open("./Data/Line_up_data.json", "w") as f:
        json.dump(liberos_dict, f)