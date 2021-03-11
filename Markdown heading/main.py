def heading(my_title, n=1):
    if n == 2:
        final = 2
    elif n == 3:
        final = 3
    elif n == 4:
        final = 4
    elif n == 5:
        final = 5
    elif n >= 6:
        final = 6
    else:
        final = 1
    return final * "#" + " " + my_title
# print(heading("Vunderbar", 7))

"""def heading(my_title, n=1):
    if 1 <= n <= 6:
        return n * "#" + " " + my_title
    elif n > 6:
        return 6 * "#" + " " + my_title
    else:
        return "#" + " " + my_title"""

#print(heading("Vunderbar", 7))
