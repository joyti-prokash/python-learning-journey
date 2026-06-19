text = input("Enter some text: ")

file = open("notes.txt", "w")

file.write(text)

file.close()

print("Text saved to notes.txt")