class Place:
    def __init__(self, area, adress):
        self.area = area
        self.adress = adress

    def to_sell(self):
        print(f'Area is {self.area}, Adress is {self.adress}', end=" ")


class Apartament(Place):
    def __init__(self, area, adress, rooms):
        super().__init__(area, adress)
        self.rooms = rooms

    def to_sell(self):
        super().to_sell()
        print(f'Count of rooms is {self.rooms}')


class House(Place):
    def __init__(self, area, adress, floors):
        super().__init__(area, adress)
        self.floors = floors

    def to_sell(self):
        super().to_sell()
        print(f'Count of floors is {self.floors}')

apartment = Apartament(50, 'Minsk', 2)
apartment.to_sell()
house = House(125, 'Mohilev', 3)
house.to_sell()
