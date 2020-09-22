# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_val = min(test_dict, key=test_dict.get)
max_val = max(test_dict, key=test_dict.get)
print("min: " + min_val)
print("max: " + max_val)
