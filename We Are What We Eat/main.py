# the list "meals" is already defined
# your code here
total_cals = 0
total_cals = sum(cals['kcal'] for cals in meals)
print(total_cals)
