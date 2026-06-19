import csv

total_age = 0
count = 0

with open("people.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        total_age += int(row[1])
        count += 1
    
average_age = total_age / count


with open("summary.csv", "w") as summary:
    summary.write(f"Total records: {count}\n")
    summary.write(f"Average age: {average_age}")


print("Summary exported to the summary.csv")