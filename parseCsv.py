import csv
file_name = "IDAndName.csv"

with open(file_name, "r") as std:
    csv_reader = csv.reader(std)
    header = next(csv_reader)
    for row in csv_reader:
        row[0] = int(row[0])
        print(row)