import math


# Modify this function in the shell and copy the new version here
def my_sqrt(value):
    if type(value) is not int and type(value) is not float:
        return None
    else:
        return(math.sqrt(value))