class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start_car(self):
        return f"{self.year} {self.make} {self.model} завелась"

    def drive_car(self):
        return f"ты ездиешь на {self.year} {self.make} {self.model}"

    def park_car(self):
        return f"{self.year} {self.make} {self.model} припаркована"

car1 = Car("Subaru", "Impreza", 2004, "Синяя")
print(car1.start_car())
print(car1.drive_car())
print(car1.park_car())