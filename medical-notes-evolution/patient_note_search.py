keyword = input("Enter keyword to search: ").lower()

with open("patient_notes.txt", "r") as file:
    notes = file.readlines()

found = False

for note in notes:
    if keyword in note.lower():
        print(note.strip())
        found = True
    
if not found:
    print("No matching notes found")