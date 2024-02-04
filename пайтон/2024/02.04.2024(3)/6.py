class Phone:
    def __init__(self, brand, model, os, color):
        self.brand = brand
        self.model = model
        self.os = os
        self.color = color

    def make_call(self, number):
        return f"Вызов номера {number}"

    def send_message(self, number, message):
        return f"Отправка сообщения \"{message}\" на номер {number}"

    def info(self):
        return f"Телефон {self.brand} {self.model} ОС: {self.os} Цвет: {self.color}"

phone1 = Phone("Google", "Pixel 8", "Andriod", "Hazel")
print(phone1.info())
print(phone1.make_call("+77472828688"))
print(phone1.send_message("+77472828688", "Whatsupp!"))
