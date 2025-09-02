line=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print(f"{line[0]},\n{line[1]},\n{line[2]}")
choose=input("chose where want the rabbit go?")
lin=int(choose[0])
cho=int(choose[1])
line[lin-1][cho-1]="🐇"
print()
print(f"{line[0]},\n{line[1]},\n{line[2]}")
