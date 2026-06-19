from notes import add_note, view_notes, edit_note, delete_note

while True:
    print("\n---Medical Note System Project ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()
    
    elif choice == "3":
        edit_note()

    elif choice == "4":
        delete_note()
    
    elif choice == "5":
        print("Exiting...")
        break
    
    else:
        print("Invalid option")