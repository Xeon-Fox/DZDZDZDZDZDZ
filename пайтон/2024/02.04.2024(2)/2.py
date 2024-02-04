import random

N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))

matrix = [[random.randint(-20, 20) for i in range(M)] for i in range(N)]

for row in matrix:
    print(row)