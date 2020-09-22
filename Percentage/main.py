def get_percentage(num, round_digits=None):
    num = round(num * 100, round_digits)
    return f"{str(num)+'%'}"

# print(get_percentage(0.0123))
# print(get_percentage(0.0123, 0))
# print(get_percentage(0.0123, 1))
# print(get_percentage(0.0123, 10))
# print(get_percentage(0.0296, 1))


