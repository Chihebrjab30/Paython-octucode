import random 
print("Welcome to choose who will pay for dinner at random. ")
name=input("\nEnter the names and put a comma after each name ,\n").split(",")
print("Who will pay for dinner is",random.choice(name))
