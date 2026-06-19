name = input("Enter patient name: ")
note = input("Enter patient note: ")

with open("patient_notes.txt", "a") as file:
    file.write(f"{name}: {note}\n")

print("Patient note saved.")