def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def reverse_text(text):
    return text[::-1]


text = input("Enter text: ")

print("Word count:", word_count(text))
print("Character count:", char_count(text))
print("Reversed text:", reverse_text(text))