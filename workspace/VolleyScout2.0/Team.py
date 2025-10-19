import os.path
from pathlib import Path

script_dir  = Path(__file__)
script_dir  = Path(__file__).parent
print(script_dir)
path  = Path(script_dir, "Teams")
print(path)
directory = '.\\Teams\\'
filename = "demofile.txt"
file_path = os.path.join(path, filename)
with open(file_path, "a") as f:
  f.write("Now the file has more content! Yeah 123")