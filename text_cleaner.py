import string

text_input = input("Enter text to synthesize: ")
clean_text = ""

for char in text_input:
    if char not in string.punctuation:
        clean_text += char

print(f"\n\n***Text without symbols is***\n\n{clean_text}")