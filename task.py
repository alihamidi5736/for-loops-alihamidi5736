from random import randrange

def task_1(): # Lottery ticket generator

    ticket = []
while len(ticket) < 6:
    number = random.randint(1, 49)
    if number not in ticket:
        ticket.append(number)
   
    
    return ticket

def task_2(): # Countdown

    output = []
    user_number = int(input("enter a number less than 100"))
    if user_number >= 100 
    print("enter a number less than 100")
    else for i in range(100, number_user - 1, -1)
    print(i)
   

    return output

def task_3():
    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = ()

    for car_make in people_car.values():
        car_make_lengths.add(len(car_make))


    return print(f"there will be {len(car_make_lengths)} diffrent sizes of rings.")
