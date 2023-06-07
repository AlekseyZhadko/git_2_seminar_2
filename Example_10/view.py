def mode():
    mode = ['Добавить данные','Удалить данные','Изменить данные','Импорт БД','Экспорт БД','Выход']
    for i, val in enumerate(mode, start=1):
        print(f'{i} {"".join(val)}')

    return int(input('Действие? = '))

def mode_table():
    mode = ['Сотрудники','Отделы','Должности','Кем работает']
    for i, val in enumerate(mode, start=1):
        print(f'{i} {"".join(val)}')

    return int(input('Выберите таблицу = '))

def step():
    step = ['Продолжить','В меню','Выйти']
    for i, val in enumerate(step, start=1):
        print(f'{i} {"".join(val)}')

    return int(input('Действие? = '))

