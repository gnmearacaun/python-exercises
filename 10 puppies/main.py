class Puppy:
    n_puppies = 0  # number of created puppies

    def __new__(cls):
        if cls.n_puppies <= 9:
            cls.n_puppies += 1
            object.__new__(cls)  # create new object of the class
