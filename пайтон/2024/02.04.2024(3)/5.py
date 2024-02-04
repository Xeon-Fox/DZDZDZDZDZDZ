class House:
    def __init__(self, address, rooms, floors, color):
        self.address = address
        self.rooms = rooms
        self.floors = floors
        self.color = color

    def describe_house(self):
        return f"Дом находится по адресу {self.address} у него {self.rooms} комнат и {self.floors} этажей, цвет дома - {self.color}."

    def paint_house(self, new_color):
        self.color = new_color
        return f"Дом теперь окрашен в {self.color}."

    def add_room(self):
        self.rooms += 1
        return f"Теперь в доме {self.rooms} комнаты."

house1 = House("Алжир", 3, 2, "белый")
print(house1.describe_house())
print(house1.paint_house("синий"))
print(house1.add_room())
