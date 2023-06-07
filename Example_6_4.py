# Игра морской бой

import os 
import random
os.system('CLS') 

pole_user1=[['_' for i in range(0, 10)] for j in range(0, 10)]
pole_user2=[['_' for i in range(0, 10)] for j in range(0, 10)]

def print_pole(pole_user1,pole_user2):
    print('№ А Б В Г Д Е Ж З И К     № А Б В Г Д Е Ж З И К')
    for i in range(1,11):
        print(f'{i} {" ".join(pole_user1[i-1])}     {i} {" ".join(pole_user2[i-1])}')

print_pole(pole_user1,pole_user2)