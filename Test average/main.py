def average_mark(*args):
    list_ = []
    total = 0
    for arg in args:
        total += arg
        list_.append(arg)
    return round((total / len(list_)), 1)
