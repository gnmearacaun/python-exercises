class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        # finish the method
        super().__init__(side1=side, side2=side, side3=side)
# obtuse = Triangle(12, 13, 14)
# et = EquilateralTriangle(12)
# print(obtuse.get_perimeter(), et.get_perimeter())
