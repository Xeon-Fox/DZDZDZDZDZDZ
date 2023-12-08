valuta_nato_america=input("скока ")
try:
    valuta_nato_america=float(valuta_nato_america)
except ValueError:
    exit()
vo_chto=input("во что ")
match vo_chto:
    case "EUR":
        print(valuta_nato_america*0.92)
    case "UAN":
        print(valuta_nato_america*36.48)
    case "AZN":
        print(valuta_nato_america*1.7)
    case _:
        print("нельзя")