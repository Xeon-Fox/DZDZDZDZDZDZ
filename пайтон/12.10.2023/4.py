number_count = 10
positive = 0
negative = 0
zero = 0
even = 0
odd = 0
number = 0
while number_count > 0:
    number = input("число ")
    try:
      number = int(number)
    except ValueError:
      exit()
    if number > 0:
      positive += 1
    elif number < 0:
      negative += 1
    else:
      zero += 1
    if number % 2 == 0:
      even += 1
    else:
      odd += 1
    number_count -= 1
print("положительных ", positive)
print("отрицательных ", negative)
print("0 ", zero)
print("четных ", even)
print("нечетных ", odd)