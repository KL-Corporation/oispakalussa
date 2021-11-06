### WINDOWS ONLY ###
# Does not work on Linux due to case-sensitive paths.

import os
from typing import List, Set

asset_folders = ("img", "snd")
urls = [f"oispakalussa.tk/{x}" for x in asset_folders]

files = []
def addFiles(path: str):
    global files
    for tmp_p in os.listdir(path):
        p = os.path.join(path, tmp_p)
        if os.path.isdir(p):
            if ".git" not in p:
                addFiles(p)
        elif os.path.isfile(p):
            files.append(p)
        else:
            assert False, "Could not determine path type"
addFiles(".")

file_not_found: Set[str] = set()
for file_index, file in enumerate(files):
    print(f"Processing file '{file}' ({file_index + 1} / {len(files)})")
    content: str
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"'{file}' is not a text file.")
        continue

    content = content.lower()
    for toFind in urls:
        toFind = toFind.lower()
        min_index: int = 0
        while content.find(toFind, min_index) != -1:
            found_pos = content.find(toFind, min_index)

            tmp_found_end_1 = content.find("\"", found_pos)
            tmp_found_end_2 = content.find("\'", found_pos)
            if tmp_found_end_1 == -1:
                tmp_found_end_1 = len(content) + 1
            if tmp_found_end_2 == -1:
                tmp_found_end_2 = len(content) + 1
            found_end = min(tmp_found_end_1, tmp_found_end_2)
            assert found_end != len(content) + 1

            url = content[found_pos:found_end]
            min_index = found_end

            path = url.replace("oispakalussa.tk", ".")
            if not os.path.isfile(path):
                file_not_found.add(path)

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
if len(file_not_found) < 1:
    print(GREEN + "No assets are missing." + RESET)
else:
    print(RED + "Found missing assets!" + RESET)
for file in sorted(file_not_found):
    print(YELLOW + f"'{file}' is missing!" + RESET)