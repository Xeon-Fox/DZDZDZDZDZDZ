class Person:
    def __init__(self, name, age, occupation, nationality):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.nationality = nationality

    def introduce_self(self):
        return f"Привет меня зовут {self.name} мне {self.age} лет. Я работаю на {self.occupation}."

    def celebrate_birthday(self):
        self.age += 1
        return f"С днем рождения {self.name} тебе {self.age} лет"

    def change_job(self, new_job):
        self.occupation = new_job
        return f"{self.name} теперь работает как {self.occupation}."

person1 = Person("Алексей", 30, "инженер", "казахстанец")
print(person1.introduce_self())
print(person1.celebrate_birthday())
print(person1.change_job("архитектор"))