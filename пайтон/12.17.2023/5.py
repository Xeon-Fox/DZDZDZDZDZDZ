length = input("длина строки можно пожалуйста узнать от вас😭😭🙏🙏: ")
try:
   length = int(length)
except ValueError:
   print("длина это цифры если чо😤😤 ")
   exit()

c1 = input("символ 1 для строки чтобы чередовалось там: ")
c2 = input("символ 2 для строки чтобы чередовалось там: ")

string = ""
for i in range(length):
    if i % 2 == 0:
      string += c1
    else:
      string += c2 
      
print(string)