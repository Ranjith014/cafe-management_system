# define the menu of the restuarant
menu={
    "Burger": 20,
    "Pizza": 100,
    "Pasta": 50,
    "Salad": 70,
    "Fries": 60,
    "Drink": 40,
}

#Greet
print("Welcome to our restaurant")
print("Burger:Rs20\nPizza:Rs100\nPasta:Rs50\nSalad:Rs70\nFries:Rs60\nDrink:Rs40\n")

order_total =0

item_1=input("Enter your 1st item:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your {item_1} is added to your order")
else:
    print("Ordered item {item_1} is not available in our menu")
    
item_2=input("Do you want to order another item? (yes/no):")
if item_2=="yes":
    item_2=input("Enter your 2nd item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your {item_2} is added to your order")
    else:
        print("Ordered item {item_2} is not available in our menu")

item_3=input("Do you want to order another item? (yes/no):")
if item_3=="yes":
    item_3=input("Enter your 3rd item:")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"your {item_3} is added to your order")
    else:
        print("Ordered item {item_3} is not available in our menu")
                
item_4=input("Do you want to order another item? (yes/no):")
if item_4=="yes":
    item_4=input("Enter your 4th item:")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"your {item_4} is added to your order")
    else:
        print("Ordered item {item_4} is not available in our menu")
print(f"the total amount of items to pay is {order_total}")
print("Thank you,visit again")