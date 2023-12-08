import math
dlina_okruznost=input("asd ")
perimeter_kvadrat=input(" a ")
try:
    dlina_okruznost=float(dlina_okruznost)
    perimeter_kvadrat=float(perimeter_kvadrat)
except ValueError:
    exit()
diametr_okurok=dlina_okruznost/math.pi
storona_kadarat=perimeter_kvadrat/4
if diametr_okurok<=storona_kadarat:
    print("вместиться ")
else:
    print("не ")