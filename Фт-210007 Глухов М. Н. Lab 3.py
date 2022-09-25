alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
smesh = int(input('Введите положительный шаг для шифровки, \nлибо отрицательный для дешифровки '))
mes = input('Введите сообщение для шифровки ')
itog = ''

for i in mes:
    mesto = alp.find(i)
    new_mesto = mesto + smesh
    if i in alp:
        itog += alp[new_mesto]
    else:
        itog += i
print (itog)