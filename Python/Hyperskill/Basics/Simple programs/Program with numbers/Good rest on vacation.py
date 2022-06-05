total_days = int(input())
total_food = int(input())
flight_cost = int(input())
hotel_cost = int(input())

total_expenses1 = total_food * total_days
total_expenses2 = (total_days - 1) * hotel_cost
total_expenses3 = flight_cost * 2
sum_of_costs = total_expenses1 + total_expenses2 + total_expenses3
print(sum_of_costs)
