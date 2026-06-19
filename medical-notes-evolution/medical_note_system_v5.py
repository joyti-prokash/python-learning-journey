def add_note():
    name = input("Enter patient name: ")
    symptom = input("Enter symptom: ")

    with open("patient_notes.txt", "a") as file:
        file.write(f"{name}: {symptom}\n")

    print("Patient note added")

def view_notes():
    try:
        with open("patient_notes.txt", "r") as file:
            notes = file.readlines()
        
        if not notes:
            print("No notes available")
            return []

        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note.strip()}")
        
        return notes
    
    except FileNotFoundError:
        print("No notes found")
        return[]

def edit_note():
    notes = view_notes()

    if not notes:
        return
    
    note_number = int(input("\nEnter note number to edit: "))

    if 1 <= note_number <= len(notes):
        new_note = input("Enter updated note: ")

        notes[note_number - 1] = new_note + "\n"
        
        with open("patient_notes.txt", "w") as file:
            file.writelines(notes)
        
        print("Note updated")
    
    else:
        print("Invalid note number")

while True:
    print("\n--- Medical Note System V5 ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()
    
    elif choice == "3":
        edit_note()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option")