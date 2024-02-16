class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, age):
        self.animals.append(Animal(name, age))

    def remove_animal(self):
        self.animals.pop()


zoo = Zoo()
zoo.add_animal('lion', 2)
zoo.add_animal('monkey', 5)
zoo.add_animal('tiger', 3)
zoo.remove_animal()
print(zoo.animals)
