def is_perfect(n):
    sum = 1
    k = 2
    while k * k <= n:
        if n % k == 0:
            sum += k
            m = n // k
            if m != k:
                sum += m
        k += 1
    return sum == n

start=input("начало диапозона: ")
end=input("конец диапозона: ")
try:
    start = int(start)
    end = int(end)
except ValueError:
    print("диапозон неправмильно ввел")
    exit()
for i in range(start, end):
    if is_perfect(i):
        print(i, "совершенное")
    else:
        print(i, "не совершенное")

#VN: по условию задачи, код с 21 по 25 строки должен быть оформлен в виде отдельной функции