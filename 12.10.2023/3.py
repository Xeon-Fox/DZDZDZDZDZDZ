delit_chislo = input("delit chislo kokoe ")
try:
    delit_chislo = int(delit_chislo)
except ValueError:
    exit()
count = 0
while delit_chislo >= 50:
    delit_chislo /= 2
    count += 1
print(delit_chislo, "чесло", count, "делений")