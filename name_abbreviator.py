names = input("Enter the first and last names, separated by commas: ").split(",")
abbreviations = []

for full_name in names:
    name_parts = full_name.strip().split()
    if len(name_parts) >= 2:  # نتأكد من وجود اسم ولقب
        first = name_parts[0][0]
        last = name_parts[1][0]
        mix = first + "." + last + "."
        abbreviations.append(mix)
    else:
        print(f"Skipping '{full_name}' because it does not have both first and last name.")

print("The abbreviations are:")
for abbr in abbreviations:
    print(abbr)