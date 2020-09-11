# Sample Input 1: 7 30 100 40
# Sample Output 1: 650
# The program should calculate the total $ for a given duration.
# Read integer values from standard input and print the result.
# Hint: Do not forget to consider the flight back
# There are four parameters which have to be considered:
# duration in days
# total food cost per a day
# one-way flight cost
# cost of one night in a hotel (the number of nights = duration - one)
n_days = int(input())
food_day = int(input())
single_flight = int(input())
hotel_day = int(input())
n_nights = n_days - 1
total_cost = (n_days * food_day) + (n_nights * hotel_day) + (single_flight * 2)
print(total_cost)
