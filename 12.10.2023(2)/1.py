n = input("введит chislo ")
try:
    n = int(n)
except ValueError:
    exit()
for i in range(1, n + 1):
    if n % i == 0:
        print(i, "делитель")