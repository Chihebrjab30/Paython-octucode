color=[]
fav=input("what your color like\n")
print("do you want add any another color")
add=input("yes / no ")
if add=="yes":
    
    why=input("what color want add ")
    color.append(fav)
    color.append(why)
    print(f"color likes is {color} ")

elif add=="no":
    print("ok")

else:
    print("soory what ?")
