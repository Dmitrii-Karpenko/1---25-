nomer = input('введите номер вашего места')
if int(nomer) <= 36 and int(nomer) % 2 == 0:
    print('Ваше место верхнее, купе')
elif int(nomer) <= 36 and int(nomer) % 2 != 0:
    print('Ваше место нижнее, купе')
else:
    print('Ваше место боковое')