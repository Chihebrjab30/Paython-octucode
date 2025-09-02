door=input("choose a red door 🚪 or blue door 🚪\n").lower()
if door=="red":
    box=input("select a box 1 or 2 or 3\n")
    if box=="1":
        print("you die ☠️")
    elif box=="2":
        print("your die ☠️")
    elif box=="3":
        print("you win 🎉")
    else:
        print("please entre true choose")
elif door=="blue":
    print("you die ☠️🤫")
else:
    print("❌select the true choose")
