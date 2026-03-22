# read files
# .json, .csv, .text
file_path = "/Users/nishigandha/Desktop/NP_HARD.pdf"

try:
    with open(file_path, "r") as file: #open fn gives an object which we call as file
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("That file was not found")
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("Permission denied")

import json
file_path = "op.json"

try:
    with open(file_path, "r") as file: #open fn gives an object which we call as file
        content = json.load(file)
        print(content)
except UnicodeDecodeError:
    print("That file was not found")
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("Permission denied")

import csv
file_path = "csvf.csv"

try:
    with open(file_path, "r") as file: #open fn gives an object which we call as file
        content = csv.reader(file)
        print(content) # gives memory address-->  <_csv.reader object at 0x100d09460>
        for line in content:
            print(line)
            print(line[0])
except UnicodeDecodeError:
    print("That file was not found")
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("Permission denied")