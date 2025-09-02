license=input("do you have license\n")
age=int(input("entre your age\n"))
if license.lower()=="yes" and age>=18:
    print("yes you cant drive")
else:
    print("sorry you dont drive")
