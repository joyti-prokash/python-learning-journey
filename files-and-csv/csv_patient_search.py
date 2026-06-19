import csv

search_name = input("Enter name to search: ")

with open("people.csv", "r") as file:
    reader = csv.reader(file)

    found = False

    for row in reader: 
        if row[0] == search_name:
            print("Record found:", row)
            found = True
    
    if not found:
        print("No record found")