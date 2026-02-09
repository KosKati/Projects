import os.path
from pathlib import Path






class Update:

    def __init__(self, file_path):
        self.gamename = None
        self.file_path = file_path


    def write_to_gamefile(self, gamename):
        self.gamename = gamename
        script_dir = Path(__file__)
        script_dir = Path(__file__).parent
        path = Path(script_dir, "Games")
        directory = '.\\Games\\'
        filename = self.gamename
        file_path = os.path.join(path, filename)
        with open(file_path, "a") as f:
            f.write("Now the file has more content! Yeah GameTme")

    def update_attack(self, player_number, value, label_attack):
        for player in label_attack:
            if player_number == player.text():
                player.update_label("++", "5/1(100%)")


update = Update(Path(__file__))
update.write_to_gamefile("testgame.txt")