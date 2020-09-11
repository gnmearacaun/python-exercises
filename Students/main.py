class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + self.birth_year

s_name = input()
s_lname = input()
s_dob = input()
studier = Student(s_name, s_lname, s_dob)
print(studier.id)
