import csv

total_age = 0
count = 0

with open("people.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        age = int(row[1])

        total_age += age
        count += 1

average = total_age / count

print("Average age: ", average)