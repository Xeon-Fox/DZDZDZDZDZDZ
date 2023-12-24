try:
    fd = open("output.txt", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

splitedtext_text_for_protocol = text.split('://')
splitedtext_text_for_protocol_final=splitedtext_text_for_protocol[0]
print("протокол: ", splitedtext_text_for_protocol_final)

splitedtext_text_for_adress = splitedtext_text_for_protocol[1].split('/', maxsplit=1)
splitedtext_text_for_adress_final = splitedtext_text_for_adress[0].removeprefix('www.')
print("длмееное имя: ", splitedtext_text_for_adress_final)

splitedtext_text_for_operation=splitedtext_text_for_adress[1].split('?')
splitedtext_text_for_operation_final=splitedtext_text_for_operation[0].removeprefix('?')
print("операция: ", splitedtext_text_for_operation_final)

print("Параметры: ")
splitedtext_text_for_search=splitedtext_text_for_operation[1].split('&')
splitedtext_text_for_search_final=splitedtext_text_for_search[0]
print("    ", splitedtext_text_for_search_final)

print('    ',splitedtext_text_for_search[1])