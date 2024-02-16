class Animal(object):
    def make_sound(self):
        print("I am an animal")


class Dog(Animal):
    def make_sound(self):
        print("I am a dog")


class Cat(Animal):
    def make_sound(self):
        print("I am a cat")


class Cow(Animal):
    def make_sound(self):
        print("I am a cow")

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()
cow = Cow()
cow.make_sound()