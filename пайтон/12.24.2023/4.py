try:
    fd = open("tt.txt", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

usd = 458.74

for line in text.splitlines():
    line = line.strip()
    if line:
        if line.endswith(" $"):
            try:
                amount = float(line[:-2])
            except ValueError:
                print("деньги неправильно")
                continue 

            tenge = amount * usd
            line = line[:-2] + "$ =" + " ₸" + str(tenge)

        elif line.endswith(" USD"):
            try:
                amount = float(line[:-4])
            except ValueError:
                print("деньги неправильно")
                continue

            tenge = amount * usd
            line = line[:-4] + "$ =" + " ₸" + str(tenge)
        print(line)
        with open("f.txt", "a", encoding='utf8') as write:
            write.write(line + "\n")
#насчет "В качестве аргументов программа должна принимать имена входного и выходного файлов:" непонял немножечко