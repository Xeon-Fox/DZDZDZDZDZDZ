class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    def __str__(self):
        return f"{self.__amount} {self.__currency}"

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __truediv__(self, number):
        return [Money(self.amount // number, self.currency) for _ in range(number)]
    
class Account:
    def __init__(self):
        self.__balance = {}

    def __str__(self):
        return ', '.join(f"{amount} {currency}" for currency, amount in self.__balance.items())

    def __iadd__(self, money):#iadd это типо чтобы новый объект не создавался как я понял
        if money.currency in self.__balance:
            self.__balance[money.currency] += money.amount
        else:
            self.__balance[money.currency] = money.amount
        return self

acc = Account()
money1 = Money(100, "USD")
money2 = Money(200, "USD")
money3 = Money(300, "EUR")

print(money1)
print(money2) 
print(money3)

print("///")

acc += money1
acc += money2
acc += money3

print(acc)

print("///")
money4 = money1 + money2
print(money4)

print("///")
money_list = money4 / 3
for money in money_list:
    print(money)
