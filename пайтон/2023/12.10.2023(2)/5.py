num = input(" число: ")
try:
    num=int(num)
except ValueError:
    exit()
num=str(num) 
largest_digit = 0
smallest_digit = 9
for i in num:
    i=int(i) #русская смекалочка
    if i > largest_digit:
        largest_digit = i
    if i < smallest_digit:
        smallest_digit = i
print(largest_digit, " ", smallest_digit)