
def hotel_cost (nights):
    return nights * 140 # in rands
#def plane_ride cost


def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return  2000
    elif city == "BFN":
        return



def rental_car_cost(days):
    cost = 40*days
    if days >= 7:
        cost -= 50
    elif days >= 3 and days <= 7:
        cost = cost - 30
    return cost

def new_sum(*numbers):
    return sum(numbers)


def trip_cost(city,days,spending_money):
    return new_sum(plane_ride_cost(city), hotel_cost(days), rental_car_cost(days))

print(trip_cost("Cape Town", 6, 600))



