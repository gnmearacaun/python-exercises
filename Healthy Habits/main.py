# the list "walks" is already defined
# your code here

summation: int = 0
# average: int = 0
days: int = 0
# walks = dict()
walks = [
    {"day": "Monday", "distance": 2000},
    {"day": "Tuesday", "distance": 3000},
    {"day": "Wednesday", "distance": 3500},
    {"day": "Thursday", "distance": 2500},
    {"day": "Friday", "distance": 2500},
    {"day": "Saturday", "distance": 1000},
    {"day": "Sunday", "distance": 5600}]

for i in walks:
    summation += walks[i.get()]
    days = days + 1
average = summation // days
print(average)

# I gave up on this one. Some results:
#

# the list "walks" is already defined
# your code here
sum_walk = sum([i['distance'] for i in walks])
print(int(round(sum_walk / len(walks), 0)))


# the list "walks" is already defined
# your code here
print(round((sum(x['distance'] for x in walks) / 7)))

# the list "walks" is already defined
# your code here

f = 0
g = 0
for s in walks:
    f += s.get('distance')
    g += 1
print(f // g)
