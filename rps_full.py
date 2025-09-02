import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""" 
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
one=input("Click next to play, or type (more)to know the game rules. ")

if "more" in one:
    
    print("""
1:
.Rock defeats scissors: because rock breaks scissors.
.Scissors defeat paper: because scissors cut paper.
.Paper defeats rock: because paper covers rock.
3:
Determine the winner:
The player whose symbol defeats the other player's symbol wins that round.
    """)
user=input("\nchoose rock paper scissors\n").lower()

if user not in ["rock","paper","scissors"]:
    
    print("Incorrect entry ❗")
    
else:
    
    if   user =="rock":
        
        print(f"your choice,\n{rock}")
    
    elif user=="paper":
        
        print(f"your choice,\n{paper}")
    
    elif user=="scissors":
        
        print(f"your choice,\n{scissors}")
    
    else:
        
        print("soory your choice not in the list")

cumputer=random.choice(["rock","paper","scissors"])

if   cumputer=="rock":
    
    print(f"cumputer choice,\n{rock}")

elif cumputer =="paper":
    
    print(f"cumputer choice,\n{paper}")

elif cumputer =="scissors":
    
    print(f"cumputer choice,\n{scissors}")

if user==cumputer:
    
    print(f"draw cumputer 🟰 choice{cumputer} and your choice {user}")

elif user=="rock" and cumputer=="scissors":
    
    print("you won✅ because the stone breaks the iron")

elif user=="paper" and cumputer=="rock":
    
    print("You won✅ because the paper wraps around the stone ")

elif user=="scissors" and cumputer=="paper":
    
    print("You won✅ because scissors cut paper")

else:
    
    print(f"You lost ❌because {user} loses to {cumputer}")
