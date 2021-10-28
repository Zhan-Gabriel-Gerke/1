print("Камень ножницы бумага ")
from random import *
while type(a) !=int:
    try:
        a=input("Введите камень-1 ножницы-2 бумага-3: ")
    except TypeError:
            print("Viga")
b=randint(1,3)