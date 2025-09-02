import random
print("choose (random or randint)")
choose=input("1 or 2\n")
if choose=="1":
    if random.random()>=0.5:
        computer="heads"
    else:
        computer="tails"
elif choose=="2":
    if random.randint(0,1)==0:
        computer="heads"
    else:
        computer="tails"
else:
    print("❗Sorry, I didn't pick you on the list.")      

choose2=input("choose heads or tails\n").lower()
if choose2!="heads" and choose2!="tails":
    print("Your choice is incorrect❗")

elif choose2==computer.lower():
    print("I won ✅")
else :
    print("I lost ❌")