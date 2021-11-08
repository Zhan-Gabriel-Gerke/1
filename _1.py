print("Камень ножницы бумага ")
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
        from keyboard import *
        v1=['Камень','Ножницы','Бумага'] 
        v2=['Камень','Ножницы','Бумага'] 
        while True: 
            print('Играем? esc= выходим, enter= играем') 
            if read_key()=='esc': 
                break 
            elif read_key()=='enter': 
                p1=choice(v1) 
                print('Первый Бот: ',p1) 
                p2=choice(v2) 
                print('Второй Бот: ',p2) 
                if p1==p2: 
                    print('Ничья') 
                elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]: 
                    print('Выйграл 1') 
                else: 
                    xˇxprint("Выйграл 2")
