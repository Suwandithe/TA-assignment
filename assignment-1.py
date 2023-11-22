class House:
    def __init__(self, color, has_garage, address):
        self.color = color
        self.has_garage = has_garage
        self.address = address

    def paint_house(self, new_color):
        self.color = new_color
        return f'The house is now painted { new_color}'

    def add_garage(self):
        if self.has_garage:
            return 'The house already has a garage'
        else:
            self.has_garage = True
            return " A garage has been added to the house"

    def set_address(self, new_address):
        self.address = new_address
        return f"The house address is now {new_address}"

    # testing the method
my_house = House(color = 'blue' , has_garage= False, address= " 123 Main st")

print(my_house.paint_house('yellow'))
print(my_house.add_garage())
print(my_house.add_garage())
print(my_house.set_address('456 west st '))