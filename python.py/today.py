import csv 

with open("suri.csv", mode='r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)