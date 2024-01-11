cost_democracy_type_anarchy=input("asd ")
try:
    cost_democracy_type_anarchy=int(cost_democracy_type_anarchy)
except ValueError:
    exit()
match cost_democracy_type_anarchy:
    case x if x < 200:
        print("не жирно ли скидку на это спрашивать?")
    case x if x < 300:
        print("3%, жмоб")
    case x if x < 500:
        print("5%, рыночек зарешал")
    case _:
        print("7%, подавись")
