
# GitHub Repository:  https://github.com/HananeAhamadizade/Fruit-Shop 

def shopping_list(**fruits):
    total = sum(fruits.values())
    count = len(fruits)

    expensive = max(fruits, key=fruits.get)
    cheap = min(fruits, key=fruits.get)

    print(f"You have {count} fruits in your shopping list")
    print(f"The total cost of the shopping list is {total}")
    print(f"The most expensive fruit is {expensive} with the price of {fruits[expensive]}")
    print(f"The cheapest fruit is {cheap} with the price of {fruits[cheap]}")


fruits = {}

while True:
    user_input = input()

    if user_input == "finish":
        break

    name, price = user_input.split()
    fruits[name] = int(price)

shopping_list(**fruits)
