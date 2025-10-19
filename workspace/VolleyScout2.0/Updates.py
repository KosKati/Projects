import os.path
from pathlib import Path
import MainWindow


class Update:

    def __init__(self, file_path):
        self.gamename = None
        self.file_path = file_path


    def write_to_gamefile(self, gamename):
        self.gamename = gamename
        script_dir = Path(__file__)
        script_dir = Path(__file__).parent
        print(script_dir)
        path = Path(script_dir, "Games")
        print(path)
        directory = '.\\Games\\'
        filename = self.gamename
        file_path = os.path.join(path, filename)
        with open(file_path, "a") as f:
            f.write("Now the file has more content! Yeah GameTme")


    def update_attack(self, player, value ):
        label_attack = MainWindow.statistic_frame_players
        label_a = label_attack.get_attack_label





update = Update(Path(__file__))
update.write_to_gamefile("testgame.txt")