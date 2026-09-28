import csv
import json

 
with open("students.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    # Convert each row into a dictionary
    data = []
    for row in reader:
        data.append(row)

 
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")