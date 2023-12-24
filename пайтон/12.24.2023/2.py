try:
    fd = open("txtforTIDR.txt", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

emails = text.split("\n")
for email in emails:
    start_and_end_of_emails=email.split("@")

    start_email=start_and_end_of_emails[0]
    if start_email == "":
        print(email, " некорректный адрес")
        continue

    for i in start_email:
        if i in ['-', '&', '=', '_', ',', '<', '>', '+', "'"]:
            print(email, " некорректный адрес")
            continue
    
    end_email=start_and_end_of_emails[1]
    if end_email == "":
        print(email, " некорректный адрес")
        continue

    for i in end_email:
        if i in ['-', '&', '=', '_', ',', '<', '>', '+', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(email, " некорректный адрес")
            continue
    
    find_dot=end_email.split(".")
    try:
        after_dot=find_dot[1]
    except IndexError:
        print(email, " некорректный адрес")
        continue
    
    print(email, "нормас")

    


    
    