# DATA 
from os import system

m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titanic  2"

m_1_ticket_cost_a = 100
m_1_ticket_cost_b = 120
m_1_time_a = "18:00"
m_1_time_b = "20:00"

m_2_ticket_cost_a = 100
m_2_ticket_cost_b = 120
m_2_time_a = "20:00"
m_2_time_b = "23:00"

m_3_ticket_cost_a = 100
m_3_ticket_cost_b = 120
m_3_time_a = "18:00"


system("clear")

# MOVIE BOARD
print(
f"""
1. {m_title_1}
2. {m_title_2} 
3. {m_title_3}

"""
)
movie_number = input('Choose a movie: ') 

if movie_number == "1":
    print(f"You've chosen '{m_title_1}'")
    time = input('Choose time: ')

    if time == m_1_time_a:
        print(f'time: 18:00, ticket cost {m_1_ticket_cost_a}')
        cost = m_1_ticket_cost_a

    if time == m_1_time_b:
        print(f'time: 20:00, ticket cost {m_1_ticket_cost_b}')
        cost = m_1_ticket_cost_b

    amount = int(input('How many tickets: '))
    total = amount * cost
    print(f'{amount} x {cost} = {total}')

if movie_number == "2":
    print(f"You've chosen '{m_title_2}'")
    time = input('Choose time: ')
    if time == m_2_time_a:
        print(f'time: 18:00, ticket cost {m_2_ticket_cost_a}')
        cost = m_2_ticket_cost_a

    if time == m_2_time_b:
        print(f'time: 23:00, ticket cost {m_2_ticket_cost_b}')
        cost = m_2_ticket_cost_b

    amount = int(input('How many tickets: '))
    total = amount * cost
    print(f'{amount} * {cost} = {total}')

if movie_number == "3":
    print(f"You've chosen '{m_title_3}'")
    time = input('Choose time: ')
    if time == m_3_time_a:
        print(f'time: 18:00, ticket cost {m_3_ticket_cost_a}')
        cost = m_3_ticket_cost_a
    amount = int(input('How many tickets: '))
    total = amount * cost
    print(f'{amount} * {cost} = {total}')
