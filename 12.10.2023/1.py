start = input("начальное ")
konec = input("конечное ")
try:
    start = int(start)
    konec = int(konec)
except ValueError:
    exit()
sum = 0
i = start
while i <= konec:
    sum += i
    i += 1
print(sum)