cost = input("Введите стоимость покупки в натовской валюте: ")
discount = input("Введите размер скидки в %: ")

try:
    cost = int(cost)
    discount = int(discount)
except ValueError:
    print("нормально введи четы")
    exit()

discount_amount = cost * discount / 100
final_cost = cost - discount_amount

template= "К оплате: %s натовских долларов"
print(template % final_cost)