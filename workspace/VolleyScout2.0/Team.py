import os.path
from pathlib import Path

script_dir  = Path(__file__)
script_dir  = Path(__file__).parent
path  = Path(script_dir, "Teams")
directory = '.\\Teams\\'
filename = "demofile.txt"
file_path = os.path.join(path, filename)
with open(file_path, "a") as f:
  f.write("Now the file has more content! Yeah 123")