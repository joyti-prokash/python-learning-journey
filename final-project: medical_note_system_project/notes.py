
def add_note():
    name = input("Enter patient name: ")
    symptom = input("Enter symptom: ")

    with open("patient_notes.txt", "a") as file:
        file.write(f"{name}: {symptom}\n")
    
    print("Note added")

def view_notes():
    try:
        with open("patient_notes.txt", "r") as file:
            notes = file.readlines()
        
        if not notes:
            print("No notes available.")
            return
        
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")

        return notes

    except FileNotFoundError:
        print("No file found")
        return[]

def edit_note():
    notes = view_notes()

    if not notes:
        return

    notes = open("patient_notes.txt", "r").readlines()

    note_number = int(input("\nEnter note number to edit: "))

    if 1 <= note_number <= len(notes):
        new_note = input("Enter updated note: ")

        notes[note_number - 1] = new_note + "\n"
        
        with open("patient_notes.txt", "w") as file:
            file.writelines(notes)

        print("Note updated")
    
    else:
        print("Invalid note number")

def delete_note():
    notes = view_notes()

    if not notes:
        return
    
    note_number = int(input("Enter note number to delete: "))

    if 1 <= note_number <= len(notes):
        del notes[note_number-1]

        with open("patient_notes.txt", "w") as file:
            file.writelines(notes)

        print("Note deleted")
    else:
        print("Invalid note number")
    

    