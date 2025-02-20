
from restaurant import *

# contains order data
order = {
    "items": []
}

def printOrder(order):
    """Display current order details."""
    if not order["items"]:
        print("\nYour order is empty.")
    else:
        print("\nYour Order:")
        for idx, item in enumerate(order["items"], 1):
            print(f"{idx}. {item['name']} x {item['quantity']} = {item['total']['amount']:.2f} {item['total']['currency']}")
        total_sum = sum(item["total"]["amount"] for item in order["items"])
        currency = order["items"][0]["total"]["currency"]  
        print(f"\nTotal: {total_sum:.2f} {currency}")
    input("\nHit ENTER to continue")

#########################
food = loadFood()
while True:
    option = printMenu()

    if option == 0 :
        break
    
    if option == 1 :
        printFood(food)
        input("Hit ENTER to continue")

    if option == 2 :
        selected_i = int(input("which item: ")) -1
        selected_item = food[selected_i]
        #Hw1: if+else -> check "avail"
        if selected_item['avail'] <= 0:
            print(f"Sorry,<<{selected_item['name']}>> is currently unvailable.")
            input("Hit ENTER to continue")
            continue
        else:
            print(f"You've selected <<{food[selected_i]['name']}>>")
            quantity = int(input("How many:"))
            if quantity > selected_item['avail']:
                print(f"Sorry, you can only order up to {selected_item['avail']} items of <<{selected_item['name']}>>.")
                input("Hit ENTER to continue")
                continue

        price_per_item = quantity * food[selected_i]['price']['amount']
        print(
            f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}")
        #HW2: ask for confirmation(yes/no)?
        confirmation = input("Confirm your order? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            print(f"Order for <<{selected_item['name']}>> confirmed!")

            order["items"].append({
                "name": selected_item["name"],
                "quantity": quantity,
                "total": {"amount": price_per_item, "currency": "MDL"}
            })
        else:
            print("Order canceled.")
            
        input("Hit ENTER to continue")
    if option == 3:
        printOrder(order)
        
        #HW3: add in order["items"] (.append())
        #{
        # "name": "Soup", "quantity": 10, "total": {"amount": 450, "currency": "MDL"}
        # }
        