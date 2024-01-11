import datetime
curent_den_nedeli=1
while True:
    if curent_den_nedeli==1:
        print("понедельник ")
    elif curent_den_nedeli==2:
        print("вторник ")
    elif curent_den_nedeli==3:
        print("среда ")
    elif curent_den_nedeli==4:
        print("четверг ")
    elif curent_den_nedeli==5:
        print("пятница раскумарница ")
    elif curent_den_nedeli==6:
        print("суббота ")
    elif curent_den_nedeli==7:
        print("воскресенье день безделья ")
        curent_den_nedeli=0
    eshe_budesh=input("еще? ")
    if eshe_budesh == "ок":
        curent_den_nedeli+=1
        continue
    else:
        break