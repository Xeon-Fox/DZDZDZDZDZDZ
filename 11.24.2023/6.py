number_mumber_humber_dumber = input("Введите трехзначное число: ")
try:
    number_mumber_humber_dumber=int(number_mumber_humber_dumber)
except ValueError:
    exit()
number_mumber_humber_dumber = number_mumber_humber_dumber // 10 % 10
second_digit_cifra_number = number_mumber_humber_dumber
print("Вторая цифра числа:", second_digit_cifra_number)