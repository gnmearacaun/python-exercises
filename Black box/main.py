# use the function blackbox(lst) that is already defined
my_list = list()
new_lst = blackbox(my_list)
if id(new_lst) == id(my_list):
    print("modifies")
else:
    print("new")
