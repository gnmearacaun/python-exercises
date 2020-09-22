def add_viewer(name, fan_list=None):
    if fan_list is None:
        fan_list = [name]
        return fan_list
    else:
        fan_list.append(name)
        return fan_list
# print(add_viewer("Harry", ["Mark", "Joshua"]))
# print(add_viewer("Deborah"))
