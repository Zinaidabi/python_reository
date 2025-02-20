
from pprint import pp

order1 = {
    'items' : [
        {
            'price': 100,
            'quantity': 2
        },
        {
            'price': 50,
            'quantity': 1
        },
        {
            'price': 200,
            'quantity': 10
        },  
    ],
    'delivery': 100
       
}
order2 = {
    'items' : [
        {
            'price': 200,
            'quantity': 2
        },
        {
            'price': 150,
            'quantity': 1
        },
        {
            'price': 100,
            'quantity': 10
        },
    ]
}
####################

def calculateTotal(order_data):
    total = 0
    for item in order_data['items']:
        total += item['price'] * item['quantity'] 
    if 'delivery' in order_data:
        total += order_data['delivery']
    order_data['total'] = total
####################
calculateTotal(order1)
calculateTotal(order2)
####################
pp(order1)
pp(order2)
####################

# HW1: take delivery into account