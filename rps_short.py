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
one=input("Click next to play, or type (more)to know the game rules.").lower()
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
user=input("Choose rock, paper or scissors\n").lower()
if user not in ["rock","paper","scissors"]:
    print("invalide choice❗")
else:
    if user=="rock":
        print(f"your choice {rock}")
    elif user=="paper":
        print(f"your choice {paper}")
    else :
        print(f"your choice {scissors}")
computer=random.choice(["rock","paper","scissors"])
if computer=="rock":
    print(f"computer choice {rock}")
elif computer=="paper":
    print(f"computer choice {paper}")
else:
    print(f"computer choice {scissors}")
if computer==user:
    print("is a tie 🟰")

elif(user=="rock" and
computer=="scissors" or user=="paper" and computer=="rock" or user=="scissors" and computer=="paper"):
    print(f"you win because {user} Wins the {computer}")
else:
    print(f"you lose because {computer} wins the {user}")

