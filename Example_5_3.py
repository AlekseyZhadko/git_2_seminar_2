#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
#чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
import random

candys = 2021

def FilterGamemod(Gamemod):
    try:
        if (int(Gamemod)<1 or int(Gamemod)>2):
            raise Exception 
    except Exception:
        print('Введенные данные не верны')
        Gamemod=input('Выберите режим игры: 1 - Игрок против Игрока, 2 - Игрок против Компьютера: ')
        return FilterGamemod(Gamemod)
    return int(Gamemod)


Game_mod=input('Выберите режим игры: 1 - Игрок против Игрока, 2 - Игрок против Компьютера: ')
Game_mod=FilterGamemod(Game_mod)
lot = random.randint(1,2)
if Game_mod==1:
    if lot == 1: user_1 = 1
    else: user_1 = 0
elif Game_mod==2:
    if lot ==1:
        Game_mod=3
        user_1=1
    else:
        user_1=0


def Filter(candy,user_1):
    try:
        if (int(candy)<1 or int(candy)>28):
            raise Exception 
    except Exception:
        print('Введенные данные не верны')
        if user_1 == 1:
            candy = int(input('Ходит: Игрок 1, Введите число конфет от 1 до 28: '))
            return(Filter(candy,user_1))
        else:
            candy = int(input('Ходит: Игрок 2, Введите число конфет от 1 до 28: '))
            return(Filter(candy,user_1))
    return int(candy)


print(Game_mod)
def Game(candys,user_1,gamemod):
    candy = 0
    user_1_candy=0
    while candys > 0:
        if user_1==1:
            candy  = input('Ходит: Игрок 1, Введите число конфет от 1 до 28: ')
            candy = Filter(candy,user_1)
            candys-=candy
            user_1_candy=candy
            user_1=0
            if candys < 0:
                candys=0
            print(f'Осталось конфет: {candys}')
        else:
            if gamemod==1:
                candy  = input('Ходит: Игрок 2, Введите число конфет от 1 до 28: ')
                candy = Filter(candy,user_1)
                candys-=candy
                user_1=1
                if candys < 0:
                    candys=0
                print(f'Осталось конфет: {candys}')
            elif gamemod==2:
                if candys==2021:
                    candy=2021-(2021/29*29)
                else:
                    candy=29-user_1_candy
                print(f'Компьютер взял {candy} конфет')
                candys-=candy
                user_1=1
                print(f'Осталось конфет: {candys}')
            else:
                candy=29-(2021-(2021//29*29))
                print(f'Компьютер взял {candy} конфет')
                candys-=candy
                user_1=1
                print(f'Осталось конфет: {candys}')
    if user_1==0:
        print('Победил игрок 1')
    else:
        if gamemod == 1:
            print('Победил игрок 2')
        else:
            print('Победа компьютера')

Game(candys,user_1,Game_mod)