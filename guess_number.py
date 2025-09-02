import random 
number=random.randint(1000,1001)
guess=input("Choose a number from 4 numbers\n")
num=len(guess)
if num!=4 :
    print("Please enter 4 numbers")
elif guess==str(number):
    print(f"Good guessed number is {number}")
else:
    print(f"The guess is incorrect. The correct number is {number}")
    
