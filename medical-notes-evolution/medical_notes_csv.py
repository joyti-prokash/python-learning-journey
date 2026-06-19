import csv

patient_name = input("Enter patient name: ")
diagnosis = input("Enter diagnosis: ")

with open("patient_notes.csv", "a", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([patient_name, diagnosis])

print("Note saved successfully.")