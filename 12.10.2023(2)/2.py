N_chislo_krutoe=input("asd ")
try:
    N_chislo_krutoe=int(N_chislo_krutoe)
except ValueError:
    exit()
current_Chislo_kotoroe_shas=1
before_that_thing=1
poslednee_kotoroe_nam_nada=0
for i in range(N_chislo_krutoe):
    poslednee_kotoroe_nam_nada=before_that_thing
    before_that_thing=current_Chislo_kotoroe_shas
    current_Chislo_kotoroe_shas=before_that_thing+poslednee_kotoroe_nam_nada
    print(current_Chislo_kotoroe_shas)