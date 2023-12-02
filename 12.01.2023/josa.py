#1 vvesti_cheto=input("sadf ")
# match vvesti_cheto:
#     case "0":
#         print(")")
#     case "1":
#         print("!")
#     case "2":
#         print("@")
#     case "3":
#         print("#")
#     case "4":
#         print("%")
#     case "5":
#         print("^")
#     case "6":
#         print("&")
#     case "7":
#         print("*")
#     case "8":
#         print("(")
#     case "9":
#         print("$")
#     case _:
#         print("asd")

# 3 year_good_askdl = input("   asd ")
# try:
#    year_good_askdl = int(year_good_askdl)
# except ValueError:
#    exit()
# if (year_good_askdl % 4 == 0) and (year_good_askdl % 100 != 0) or (year_good_askdl % 400 == 0):
#     print('висо')
# else:
#     print('🏳️‍🌈🏳️‍🌈🏳️‍🌈 ')

#4 slovo = input("ASDasd ")
# proshlaya_bukva = proshlaya_bukva[::-1]
# if proshlaya_bukva == a:
#   print("параллелипипед ")
# else:
#   print("🏁")

#5 valuta_nato_america=input("скока ")
# try:
#     valuta_nato_america=float(valuta_nato_america)
# except ValueError:
#     exit()
# vo_chto=input("во что ")
# match vo_chto:
#     case "EUR":
#         print(valuta_nato_america*0.92)
#     case "UAN":
#         print(valuta_nato_america*36.48)
#     case "AZN":
#         print(valuta_nato_america*1.7)
#     case _:
#         print("нельзя")

#6 cost_democracy_type_anarchy=input("asd ")
# try:
#     cost_democracy_type_anarchy=int(cost_democracy_type_anarchy)
# except ValueError:
#     exit()
# match cost_democracy_type_anarchy:
#     case x if x < 200:
#         print("не жирно ли скидку на это спрашивать?")
#     case x if x < 300:
#         print("3%, жмоб")
#     case x if x < 500:
#         print("5%, рыночек зарешал")
#     case _:
#         print("7%, подавись")

#7 import math
# dlina_okruznost=input("asd ")
# perimeter_kvadrat=input(" a ")
# try:
#     dlina_okruznost=float(dlina_okruznost)
#     perimeter_kvadrat=float(perimeter_kvadrat)
# except ValueError:
#     exit()
# diametr_okurok=dlina_okruznost/math.pi
# storona_kadarat=perimeter_kvadrat/4
# if diametr_okurok<=storona_kadarat:
#     print("вместиться ")
# else:
#     print("не ")

shet=0
firt_quation=input("5-6 или 7-8 ")
if firt_quation == "-1":
    print("красава")
    shet+=2
else:
    print("не")
seco_quation=input("lim где x стремиться к -1 (x^3+3x^2-2)/(x^3+x^2+x+1) ")
if seco_quation == "я в 10 классе че это😭😭":
    print("иче")
elif seco_quation == "-3/2":
    print("красава")
    shet+=2
else:
    print("не")
tird_quation=input("X/x^2-x+2/1-x^2=5/x^2+x ​")
if tird_quation == "5":
    print("красава")
    shet+=2
elif tird_quation == "да ёб твою где цифры":
    print("лан лан чел")
else:
    print("не")
print(shet)