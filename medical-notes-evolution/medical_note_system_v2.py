def add_note():
    name = input("Enter patient name: ")
    symptom = input("Enter symptom: ")

    with open("patient_notes.txt", "a") as file:
        file.write(f"\n {name}: {symptom}\n")

    print("Patient note added")

def view_notes():
    try:
        with open("patient_notes.txt", "r") as file:
            notes = file.readlines()
        
        print("\n ---- Patient Notes ---")

        for note in notes:
            print("\n"+ note.strip())

    except FileNotFoundError:
        print ("No notes found")

def search_notes():
    keyword = input("Enter keyword to search: ").lower()

    try: 
        with open("patient_notes.txt", "r") as file:
            notes = file.readlines()
        
        found = False

        for note in notes:
            if keyword in note.lower():
                print("\n" + note.strip())
                found = True
        if not found:
            print("No matching records")
    
    except FileNotFoundError:
        print("No notes file found")

while True:
    print("\n --- Medical Note System V2 ---")
    print("1. Add Patient Note")
    print("2. View Patient Notes")
    print("3. Search Notes")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        print("Exiting system")
        break

    else:
        print("Invalid option")
