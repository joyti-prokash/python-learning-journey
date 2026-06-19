import csv

file_name = "patient_notes.csv"

patient_name = input("Enter patient name: ")
diagnosis = input("Enter diagnosis: ")

rows = []
new_id = 1 # dafault value ALWAYS defined

try:
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # convert old format if needed
    if rows and not rows[0][0].isdigit():
        rows = [[str(i), row[0], row[1]] for i, row in enumerate(rows, start=1)]
    
    if rows:
        new_id = int(rows[-1][0]) + 1

except FileNotFoundError:
    rows = []
    new_id = 1

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([new_id, patient_name, diagnosis])

print(f"Note saved with ID {new_id}")


with open(file_name, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
