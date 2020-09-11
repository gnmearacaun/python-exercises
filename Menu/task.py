item = input()
choices = ["pizza", "salad", "soup"]
# choices = "pizza, salad, soup"
if item in choices:
   # if item == "pizza":
    if item == choices[0]:
        print("Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy")
   # elif item == "salad":
    elif item == choices[1]:
        print("Caesar salad, Green salad, Tuna salad, Fruit salad")
   # elif item == "soup":
    elif item == choices[2]:
        print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
else:
     print("Sorry, we don't have it in the menu")
