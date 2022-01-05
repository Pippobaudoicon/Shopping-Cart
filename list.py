item_list = []
item_list_price = []
def invalid_answer():
    print()
    print("Your input was not a valid answer!")
    menu()

def menu():
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Please select an action: ").lower()
    if choice == "1" or choice == "add item":
        addItem()
    elif choice == "2" or choice == "view cart":
        viewCart()
    elif choice == "3" or choice == "remove item":
        removeItem()
    elif choice == "4" or choice == "compute total":
        computeTotal()
    elif choice == "5" or choice == "quit":
        end()    
    else:
        invalid_answer()

def addItem():
    item = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item}' (in US dollar)? "))
    item_list.append(item)
    item_list_price.append(item_price)
    print(f"'{item}' has been addded to the cart.")
    print()
    menu()

def viewCart():
    print("The contents of the shopping cart are: ")
    print()
    num_order = 0
    for item1, item2 in zip(item_list, item_list_price) :
        num_order += 1
        item2 = "${:,.2f}".format(item2)
        print(f"{num_order}. {item1} -> {str(item2)}")
    print()
    menu()

def removeItem():
    print("The contents of the shopping cart are: ")
    print()
    num_order = 0
    for item1, item2 in zip(item_list, item_list_price) :
        num_order += 1
        item2 = "${:,.2f}".format(item2)
        print(f"{num_order}. {item1} -> {str(item2)}")
    print()
    removed_item = int(input("Which item (number) would you like to remove? "))     
    if removed_item-1 < len(item_list):
        print()
        print(f"The item '{item_list[removed_item-1]}' has been removed correctly!")
        item_list.pop(removed_item-1)
        item_list_price.pop(removed_item-1)
    else:
        print()
        print(f"Please select a number present in your cart")
        removeItem()
    print()
    menu()

def computeTotal():
    item_total = 0
    for total in item_list_price:
        item_total += total
        total_currency = "${:,.2f}".format(item_total)
    print(f"The total price of the items in the shopping cart is {total_currency}")
    print()
    menu()

def end():
    item_list = []
    print("Thank you. Goodbye.")

print("Welcome to the Shopping Cart Program!")
menu()