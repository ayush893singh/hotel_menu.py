menu = {"pizza":99,
    "pasta":70,
    "burger":60,
    "salad":40,
    "coffee":60,
    "cold drink":120,
    "water":30,}

print("-----Welcome to Restaurant-----")
print("pizza: Rs:99\npasta: Rs:70\nburger: Rs:60\nsalad: Rs40\ncoffee: Rs60\ncold drink: Rs:120\nwater: Rs30")

Order_Total = 0
item_1 = input("Enter your first item name : ")
if item_1 in menu:
    Order_Total += menu[item_1]
    print(f"-----Your item {item_1} has been added to your Order-----")
else:
    print(f"Orderd item {item_1} is not avaialable yet!")
Another_Order = input("\nDo you want to add another item? (yes/no) :- ")

if Another_Order == "yes":
    item_2 = input("\nEnter the name of second item : ")
    if item_2 in menu:
        Order_Total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Orderd item {item_2} is not avaialable!")

print(f"\nThe total amount of items to pay is : {Order_Total} Rupees")
print("-----Thank You-----")
