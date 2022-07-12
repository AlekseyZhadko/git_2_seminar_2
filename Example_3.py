#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
print('В какой четверти или на какой оси находятся координаты X и Y')
x = input('Введите координату X: ')
y = input('Введите координату Y: ')

def CoordinatePlane(x,y):
    try:
        x = float(x)
        y = float(y)
    except:
        print('Error: требуется ввести числа')
        x = input('Введите координату X: ')
        y = input('Введите координату Y: ')
        return CoordinatePlane(x,y)
    if x > 0 and y > 0:
        print(f'x={x}; y={y} -> 1')
    elif x < 0 and y > 0:
        print(f'x={x}; y={y} -> 2')
    elif x < 0 and y < 0:
        print(f'x={x}; y={y} -> 3')
    elif x > 0 and y < 0:
        print(f'x={x}; y={y} -> 4')
    elif x == 0 and y != 0:
        print(f'x={x}; y={y} -> Ось X')
    elif y == 0 and x != 0:
        print(f'x={x}; y={y} -> Ось Y')
    else:
        print(f'x={x}; y={y} -> Начало координат')

CoordinatePlane(x,y)