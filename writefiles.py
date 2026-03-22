# ################### Write files (.txt, .json, .csv)

txt_data = "I like pizza"

file_path = "output.txt"
employees =["Eugene", "Squidward", "Spongebob", "Patrick"]

try:
    with open(file_path, "a") as f: # "w" to write, "r" to read, "a" to append
        for employee in employees:
            # f.write(txt_data)
            f.write(employee + "\n")
        print("The file 'output.txt' has been created")
except FileNotFoundError:
    print("The file 'output.txt' already exists")


# writing absolute file path

# ################### Read files

pdf_path = "/Users/nishigandha/Desktop/NP_HARD.pdf"

# write to JOSN file
import json
emp= {
    "name" : "Spongebob",
    "email" : "sponge@email.com",
    "job_title" : "director"
}

json_path = "op.json"

try:
    with open(json_path, "w") as json_f:
        json.dump(emp, json_f, indent=4)
        print("The file 'op.json' has been created")
except FileExistsError:
    print("The file 'op.json' already exists!")

# CSV files
import csv
empl = [["Name", "Age", "Job"], ["Spongebob", 30, "Cook"], ["Patrick", 20, "Chef"], ["Sandy", 32, "CEO"]]
csv_path = "csvf.csv"
try:
    with open(csv_path, "w") as csv_f:
        writer = csv.writer(csv_f) #writer is an object that provides methods from csv
        for row in empl:
            writer.writerow(row)
        print(f"csv file '{csv_path}' has been created")
except FileExistsError:
    print("The file 'csv' already exists!")
