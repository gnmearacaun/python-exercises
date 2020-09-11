class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.h_feet = self.height / 0.3048

    # create convert_height here
    def convert_height(self):
        return self.h_feet
