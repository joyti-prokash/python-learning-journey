with open("patient_notes.txt", "r") as file:
    notes = file.readlines()

for note in notes:
    print(f"\n{note.strip()}\n")