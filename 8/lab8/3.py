class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name != '':
            self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age


person1 = Person('Sofi', 22)
person1.set_age(19)
print(person1.get_name(), person1.get_age())
