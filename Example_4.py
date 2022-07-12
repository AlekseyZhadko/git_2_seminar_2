# Напишите программу, которая по заданному номеру, четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y)

print('Диапазон координат X и Y, в указанной четверти')
number = input('Введите номер четверти: ')

def Coordinate(quarter):
    try:
        quarter = int(quarter)
    except:
        print('Error: требуется номер четверти')
        quarter =  input('Введите номер четверти: ')
        return Coordinate(quarter)
    if  quarter == 1:
        print(f'Диапазон координат x(0;+∞); y(0;+∞)')
    elif quarter == 2:
        print(f'Диапазон координат x(-∞;0); y(0;+∞)')
    elif quarter == 3:
        print(f'Диапазон координат x(-∞;0); y(-∞;0)')
    elif quarter == 4:
        print(f'Диапазон координат x(0;+∞); y(-∞;0)')
    else:
        print('Такой четверти не существует')

Coordinate(number)