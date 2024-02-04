class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def bark(self):
        return f"{self.name} гавкает"

    def fetch(self, item):
        return f"{self.name} принес {item}."

    def birthday(self):
        self.age += 1
        return f"С днем рождения {self.name} ему {self.age}."

dog1 = Dog("Бобик", "мопс", 5, "черный")
print(dog1.bark())
print(dog1.fetch("мяч"))
print(dog1.birthday())
