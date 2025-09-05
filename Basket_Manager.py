total_price = []
elements = []

print("Welcome to shop with me")
it = int(input("How many items are in the basket? "))

for i in range(1, it + 1):
    basket = input(f"What is element number {i}? ")
    elements.append(basket)
    price = float(input(f"How much for {basket}? "))
    total_price.append(price)
    print("———————————————————")

verification = input("Do you want to know the total shopping list? yes/no ").lower()
if verification == "yes":
    print("\nShopping List:")
    for item in elements:
        print("-", item)

verification2 = input("Do you want to know the total price of the materials? yes/no ").lower()
if verification2 == "yes":
    total = sum(total_price)
    print(f"Total price: {total}$")