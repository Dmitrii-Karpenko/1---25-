nomer = input('введите номер вашего места')
if int(nomer) <= 36 and int(nomer) % 2 == 0:
    print('Ваше место верхнее, купе')
elif int(nomer) <= 36 and int(nomer) % 2 != 0:
    print('Ваше место нижнее, купе')
elif int(nomer) > 36 and int(nomer) % 2 != 0:
    print('Ваше место боковое, верхнее')
else:
    print('Ваше место боковое, нижнее')