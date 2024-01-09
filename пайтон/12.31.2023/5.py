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

if is_perfect(2):
   print("совершенное")
else:
   print("не")