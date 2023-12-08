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