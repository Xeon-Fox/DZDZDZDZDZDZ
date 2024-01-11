while True:
    vvod_inputer_computer=input("pervoi vvedi ")
    second_vvod_computer_inputer=input("second ")
    try:
        vvod_inputer_computer=int(vvod_inputer_computer)
        second_vvod_computer_inputer=int(second_vvod_computer_inputer)
    except ValueError:
        exit()
    znak_che_tam_nado_sdelat=input("ZZZZVV SVO ZNAK VVEDI ")
    match znak_che_tam_nado_sdelat:
        case "+":
            result = vvod_inputer_computer+second_vvod_computer_inputer
            print(result)
        case "-":
            result = vvod_inputer_computer-second_vvod_computer_inputer
            print(result)
        case "*":
            result = vvod_inputer_computer*second_vvod_computer_inputer
            print(result)
        case "/":
            result = vvod_inputer_computer/second_vvod_computer_inputer
            print(result)
        case _:
            print("че")
    eshe_budesh=input("еще будешь ")
    if eshe_budesh == "да":
        continue
    else:
        break