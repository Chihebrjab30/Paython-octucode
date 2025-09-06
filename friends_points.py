print("Welcome to Points Bank")
list_names = ["chiheb","hamza","mohamed"]
point = [50,40,35]

print("Select a process")
choice = int(input("1: add a new friend\n2: update list\n3: view friends list\n4: delete a friend\n5: exit\n"))

if choice == 1:
    add = input("\nEnter the name: ")
    list_names.append(add)
    point.append(0)
    print("done ✅")
    check = input("Do you want to see the list? ")
    if check.lower() == "yes":
        for i in range(len(list_names)):
            print(list_names[i])
            print(point[i])
            print("——————————")

elif choice == 2:
    name = input("Enter name: ")
    if name not in list_names:
        print("Invalid choice ❌")
    else:
        action = input("Do you want to add or subtract? ").lower()
        if action not in ("add", "subtract"):
            print("Invalid choice ❌")
        else:
            val = int(input(f"Enter the number you want to {action}: "))
            index = list_names.index(name)
            if action == "add":
                point[index] += val
            else:
                point[index] -= val
            print("done ✅")
            for i in range(len(list_names)):
                print(list_names[i])
                print(point[i])
                print("——————————")

elif choice == 3:
    print("Friends list ✅")
    for i in range(len(list_names)):
        print(list_names[i])
        print(point[i])
        print("———————")

elif choice == 4:
    delete = input("Enter the name: ")
    if delete not in list_names:
        print("Invalid choice ❌")
    else:
        index = list_names.index(delete)
        list_names.pop(index)
        point.pop(index)
        print("done ✅")
        for i in range(len(list_names)):
            print(list_names[i])
            print(point[i])
            print("—————————")

elif choice == 5:
    input("Press Enter to exit")

else:
    print("Invalid choice ❌")