# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
new_dict = {focal.upper(): focal.lower() for focal in some_iterable}
print(new_dict)
