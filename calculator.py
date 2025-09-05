print("Welcome to the multiplication table")

number = int(input("Enter the number: "))
print(f"\nMultiplication table for the number {number} is\n")

for value in range(1, 11):
    result = number * value
    print(f"{number} x {value} = {result}")
    
print("\n—————— End of Table ——————")