chislo_zachemto_isportit_kotoroe=input("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.: ")
try:
    chislo_zachemto_isportit_kotoroe=int(chislo_zachemto_isportit_kotoroe)
except ValueError:
    exit()
binarchisloperemenaoguzok=bin(chislo_zachemto_isportit_kotoroe)
vosemchislodropdesateptvoiu=oct(chislo_zachemto_isportit_kotoroe)
desat=hex(chislo_zachemto_isportit_kotoroe)
print('1 ', binarchisloperemenaoguzok, '2 ', vosemchislodropdesateptvoiu, '3 ', desat)