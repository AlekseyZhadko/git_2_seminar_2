#Создайте программу для игры в "Крестики-нолики"

import os 
import random
os.system('CLS') 

pole=[['_','_','_'],['_','_','_'],['_','_','_']]
def print_pole(pole):
    print('№ 1 2 3')
    for i, val in enumerate(pole, start=1):
        print(f'{i} {" ".join(val)}')

def NotElement(element):
    try:
        if element!='X' and element!='O':
            raise Exception
    except Exception:
        print('Введенные данные не верны')
        element=input('Выберите за что будете играть: 1 - O или 2 - X = ')
        return NotElement(element)
    return element

def number_user(number): asd
    try:
        if (int(number)<1 or int(number)>3):
            raise Exception 
    except Exception:
        print('Введенные данные не верны')
        number = int(input('Введите значение снова: '))
        return number_user(number)
    return number

element_user=input('Выберите за что будете играть: 1 - O или 2 - X = ')
element_user=NotElement(element_user)

if element_user=='O':
    element_bot='X'
else:
    element_bot='O'

def win(pole,element):
    if pole[0][0]==element and pole[0][1]==element and pole[0][2]==element: return True
    if pole[1][0]==element and pole[1][1]==element and pole[1][2]==element: return True
    if pole[2][0]==element and pole[2][1]==element and pole[2][2]==element: return True
    if pole[0][0]==element and pole[1][0]==element and pole[2][0]==element: return True
    if pole[0][1]==element and pole[1][1]==element and pole[2][1]==element: return True
    if pole[0][2]==element and pole[1][2]==element and pole[2][2]==element: return True
    if pole[0][0]==element and pole[1][1]==element and pole[2][2]==element: return True
    if pole[0][2]==element and pole[0][1]==element and pole[2][0]==element: return True
    return False

def pole_no_duplication(pole,element,x,y):
    if pole[x-1][y-1]=='_':
        pole[x-1][y-1]=element
        return pole
    else:
        x=random.randint(1,3)
        y=random.randint(1,3)
        return pole_no_duplication(pole,element,x,y)

def filter_pole_user(pole,element,x,y):  
    if pole[x-1][y-1]=='_':
        pole[x-1][y-1]=element
        return pole
    else:
        print('Данная ячейка занята!')
        x=(input('Введите номер строки:  '))
        x=int(number_user(x))
        y=(input('Введите номер столбца: '))
        y=int(number_user(y))
        return filter_pole_user(pole,element,x,y)

def game(pole,element_user,element_bot,step):
    count=0
    if any("_" in i for i in pole) == True:
        if step==1:
            print('Ваш ход:')
            x=(input('Введите номер строки:  '))
            x=int(number_user(x))
            y=(input('Введите номер столбца: '))
            y=int(number_user(y))
            filter_pole_user(pole,element_user,x,y)
            print_pole(pole)
            step=0
            if win(pole,element_user) == False: return game(pole,element_user,element_bot,step)
            else: count=1
        else:
            print('Ход компьютера:')
            x=random.randint(1,3)
            y=random.randint(1,3)
            pole_no_duplication(pole,element_bot,x,y)
            print_pole(pole)
            step=1
            if win(pole,element_bot) == False: return game(pole,element_user,element_bot,step)
            else: count=1
        if count==1:
            if step==0: return print('Победил игрок')
            else: return print('Победил компьютер')
    else:
        return print('Ничья')


print_pole(pole)
game(pole,element_user,element_bot,1)



    