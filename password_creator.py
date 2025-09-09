import random
import string

password_length = int(input("Enter the length of the password you want to generate: "))

letters_pass = int(input("Enter the number of letters you want in your password: "))
numbers_pass = int(input("Enter the number of numbers you want in your password: "))
symbols_pass = int(input("Enter the number of symbols you want in your password: "))

if password_length != letters_pass + numbers_pass + symbols_pass:
    print("The numbers are not compatible ❗")
else:
    lp = random.choices(string.ascii_letters, k=letters_pass)
    np = random.choices(string.digits, k=numbers_pass)
    sp = random.choices(string.punctuation, k=symbols_pass)
    mix = lp + np + sp
    random.shuffle(mix)
    print("Password is:", "".join(mix))