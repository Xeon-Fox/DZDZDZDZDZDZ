number = input("Введите число: ")
try:
    number=int(number)
except ValueError:
    exit()
number=str(number)
skoka_sdvinut = input("Введите количество позиций для сдвига: ")
try:
    skoka_sdvinut=int(skoka_sdvinut)
except ValueError:
    exit()
number_length = len(number)
if skoka_sdvinut > number_length:
    skoka_sdvinut = skoka_sdvinut % number_length
#дальше не придумал русская смекалочка подвела

#VN: а дальше можно циклом начать перебирать цифры number от позиции skoka_sdvinut и из них формировать новое число