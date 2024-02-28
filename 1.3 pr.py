year = input('ведите год')
if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print('Год високосный')
else:
    print('Это год не високосный')