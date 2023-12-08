year_good_askdl = input("   asd ")
try:
   year_good_askdl = int(year_good_askdl)
except ValueError:
   exit()
if (year_good_askdl % 4 == 0) and (year_good_askdl % 100 != 0) or (year_good_askdl % 400 == 0):
    print('висо')
else:
    print('🏳️‍🌈🏳️‍🌈🏳️‍🌈 ')