#3
firstnumberepicbattlecalculator=input("еен ")
secondnumberepicbattlecalculator=input("леен2 ")
try:
    firstnumberepicbattlecalculator=float(firstnumberepicbattlecalculator)
    secondnumberepicbattlecalculator=float(secondnumberepicbattlecalculator)
except ValueError:
    print("нет")
    exit()
pluspppp=firstnumberepicbattlecalculator+secondnumberepicbattlecalculator
minsuyas=firstnumberepicbattlecalculator-secondnumberepicbattlecalculator
umnozit=firstnumberepicbattlecalculator*secondnumberepicbattlecalculator
delit=firstnumberepicbattlecalculator/secondnumberepicbattlecalculator
print(pluspppp," ",minsuyas," ",umnozit," ", delit)

#2
kilometersVvednniChelovekom=input("не позволите ли вы вписать километы ")
try:
    kilometersVvednniChelovekom=float(kilometersVvednniChelovekom)
except ValueError:
    print("неа")
    exit()
natoAmericanMileIhateamerica=float
natoAmericanMileIhateamerica=0.62
kmmileburgeramericailoveamerica=kilometersVvednniChelovekom*natoAmericanMileIhateamerica
print(kmmileburgeramericailoveamerica)

#1
p = input("перимтр квадрата: ")
try:
    p=float(p)
except ValueError:
    print("nuh uh")

a = p / 4
s = a * a
print("Площадь квадрта равна", s)