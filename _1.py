print("Камень ножницы бумага ")
from keyboard import *
from module1 import *
from random import *
if 1==int(input("Хотите ли вы поиграть 0 or 1")):
    g=int(input("Вы хотите поиграть с роботом или с другом  или чтобы робот с роботом 1 or 2 or 3"))
    if g==1:
        win=0
        lose=0
        m=0
        while True:
            a=int(input("Выберите 1-камень 2-ножницы 3-бумага"))
            b=randint(1,3)
            if a==b:
                print("ничья")
            if a==1 and b==2:
                print("Ты победил")
                win+=1
            if a==2 and b==3:
                print("Ты победил")
                win+=1
            if a==3 and b==1:
                print("Ты победил")
                win+=1
            if a==b:
                    print("ничья")
            if b==1 and a==2:
                print("Вы проиграли")
                lose+=1
            if b==2 and a==1:
                print("Вы проиграли")
                lose+=1
            if b==3 and a==1:
                print("Вы проиграли")
                lose+=1
        if win==3:
            print("Ты победил")
        if lose==3:
            print("Ты проиграл")
        print(win)
        print(lose)
    elif g==2:
        win=0
        lose=0
        print("вы выбрали поиграть с другом")
        while True:
            a=int(input("Выберите 1-камень 2-ножницы 3-бумага"))
            b=int(input("Выберите 1-камень 2-ножницы 3-бумага"))
            if a==b:
                print("ничья")
            if a==1 and b==2:
                print("победил игрок номер 1")
                win+=1
            if a==2 and b==3:
                print("победил игром номер 1")
                win+=1
            if a==3 and b==1:
                print("победил игрок номер 1")
                win+=1
            if b==1 and a==2:
                print("победил игрок номер 2")
                lose+=1
            if b==2 and a==1:
                print("победил игрок номер 2")
                lose+=1
            if b==3 and a==1:
                print("победил игрок номер 2")
                lose+=1
    elif g==3:
        v1=['Камень','Ножницы','Бумага'] 
        v2=['Камень','Ножницы','Бумага'] 
        
        m=start()
        if m==1:
            bot_vs_bot(v1,v2)
        elif m==2:
            while 1:
                pass
