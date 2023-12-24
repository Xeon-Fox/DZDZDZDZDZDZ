pervoe = input("первое число: ")
second = input("второе число ")
try:
    pervoe = int(pervoe)
    second = int(second)
except ValueError:
    exit()
while second != 0:
    pervoe, second = second, pervoe % second
print(pervoe)