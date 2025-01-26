# Food order
order = {
    'client'   : 'John Doe',
    'item'     : 'Salad',
    'quantity' : 2,
    'price'    : 100.00
}
if order['quantity'] > 7:
    order['total'] = order['price'] * order['quantity'] * 0.8
else:
    order['total'] = order['price'] * order['quantity']
################################
# HW1: modify the code so -> order['total'] discount 20% when quantity is more than 7
# HW2: add code so the user -> input-> question: do you need delivery?
#      based on the answer: total > 300.00 and the user wants delivery
#      order['delivery'] -> 'free', otherwise if the user wants delivery
#      order['delivery'] -> 50.00 -> 'total' updated


delivery_choice = input('Do you need delivery? (Yes/ No):')

if delivery_choice == 'yes':
    if order['total'] > 300.00:
        order['delivery'] = 'Free'
    else: 
        order['delivery'] = 50.00
        order['total'] += order['delivery']
else:
    order['delivery'] = 'No'


print("Order for  :", order ['client'])
print("Food       :", order ['item'])
print("Price x qty:", order ['price'], 'x', order['quantity'])
print("Delivery   :", order['delivery'])
print("Total      :", order['total'])