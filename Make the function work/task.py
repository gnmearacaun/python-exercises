def closest_higher_mod_5(x):
    if x % 5 == 0:
        return print(x)
    return print(x // 5 * 5 + 5)
x = int(input())
closest_higher_mod_5(x)

