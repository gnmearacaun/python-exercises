class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.t_area = float((self.a * self.b) / 2)

    def get_area(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            print(self.t_area)
        else:
            print("Not right")

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
righty = RightTriangle(input_c, input_a, input_b)
righty.get_area()
