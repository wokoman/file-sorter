import os
import shutil
from pathlib import Path

directory = '/path/to/files/'

for file in os.listdir(directory):
    if "." in file:
        Path(directory + str(file)[:4] + "/" + str(file)[4:6]).mkdir(parents=True, exist_ok=True)
        shutil.move(directory + file, directory + str(file)[:4] + "/" + str(file)[4:6] + "/" + file)