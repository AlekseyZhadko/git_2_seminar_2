def view_data(data):
    print(f'Результат = {data}')

def get_value():
    return int(input('Значение = '))

def mode():
    mode_1 = ['Сложение','Деление','Умножение','Вычетание','Возведение в степень N']
    mode_2 = ['Квадратный корень','Возведение в квадрат','Факториал','Синус','Косинус','Тангенс']
    for i, val in enumerate(mode_1, start=1):
        print(f'{i} {"".join(val)}')
    for i, val in enumerate(mode_2, start=6):
        print(f'{i} {"".join(val)}')
    return int(input('Действие? = '))

def mode_2():
    mode_1 = ['Квадратный корень']
    for i, val in enumerate(mode_1, start=1):
        print(f'{i} {"".join(val)}')
    return int(input('Действие? = '))