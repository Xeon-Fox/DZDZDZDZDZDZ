#1
p = input("перимтр квадрата: ")
try:
    p=float(p)
except ValueError:
    print("nuh uh")

a = p / 4
s = a * a
print("Площадь квадрта равна", s)