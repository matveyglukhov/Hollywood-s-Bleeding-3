alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #список букв алфавита
choice = int(input('Введите 1 для шифровки, -1 для дешифровки '))
smesh = int(input('Введите шаг шифровки '))
mes = input('Введите сообщение для шифровки ')
itog = ''

if choice == 1:
    for i in mes:
        mesto = alp.find(i)
        new_mesto = mesto + smesh
        if i in alp:
            itog += alp[new_mesto % 33]
        else:
            itog += i
    print (itog) #строка вывода

if choice == -1:
    for i in mes:
        mesto = alp.find(i)
        new_mesto = mesto - smesh
        if i in alp:
            itog += alp[new_mesto % 33]
        else:
            itog += i
    print (itog)