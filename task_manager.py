yes = []
no = []
tasks_list = input("Enter the tasks you have today (separated by commas):\n").split(",")

for task in tasks_list:
    check = input(f"\n{task.strip()}\nDid you complete this task? (yes/no)\n").lower()
    if check in ["yes", "y"]:
        yes.append(task.strip())
        print("Good job ✅")
    else:
        no.append(task.strip())
        print("Try not to postpone it ✊")
    print("---------")

check1 = input("\nDo you want to see today's program summary? (yes/no) ").lower()
if check1 in ["yes", "y"]:
    print("\n✅ Completed Tasks:")
    for task in yes:
        print("-", task)

    print("\n❌ Unfinished Tasks:")
    for task in no:
        print("-", task)