"""def tallest_people(**kwargs):
    most_tall = max(kwargs.values())
    for key, values in kwargs.items():
        if key[values] == most_tall:
            print(key, values)"""
def tallest_people(**kwargs):
    for key, value in sorted(kwargs.items()):
        if value == max(kwargs.values()):
            print('{} : {}'.format(key, value))


# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
