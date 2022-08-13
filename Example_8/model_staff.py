import json
import os
import view
import controller

def AddStaff():
    data = {}
    data['staff'] = []
    with open('Example_8/Staff.json','r', encoding='utf-8') as fh:            
        if os.stat('Example_8/Staff.json').st_size == 0:
            data['staff'].append({
                'ID': '0',
                'FIO': input('Введите ФИО: '),
                'phone': input('Введите телефон: ')
            })
        else:
            data = json.load(fh)
            data['staff'].append({
                'ID': str(int(data['staff'][len(data['staff'])-1]['ID'])+1),
                'FIO': input('Введите ФИО: '),
                'phone': input('Введите телефон: ')
            })
    with open('Example_8/Staff.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: AddStaff()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
    

def DelStaff():
    data = {}
    data['staff'] = []
    with open('Example_8/Staff.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/Staff.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            FIO = input('Введите ФИО сотрудника, которого нужно удалить: ')
            data = json.load(fh)
            count = 0
            for p in data['staff']:
                if p['FIO'] == FIO:
                    data['staff'].pop(data['staff'].index(p))
                else:
                    count += 1
            if count > 0:       
                print('Такого сотрудника не существует')
    with open('Example_8/Staff.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: DelStaff()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
            

def RemoveStaff():
    data = {}
    data['staff'] = []
    with open('Example_8/Staff.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/Staff.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            value=int(input('Что хотите изменить? 1-ФИО, 2-телефон: '))
            if value == 1:
                FIO = input('Введите ФИО сотрудника, которого нужно изменить: ')
                data = json.load(fh)
                count = 0
                for p in data['staff']:
                    if p['FIO'] == FIO:
                        FIO = input('Введите новые ФИО сотрудника: ')
                        data['staff'][data['staff'].index(p)]['FIO'] = FIO
                    else:
                        count += 1
                if count > 0:       
                    print('Такого сотрудника не существует')
            elif value == 2:
                phone = input('Введите телефон сотрудника, которого нужно изменить: ')
                data = json.load(fh)
                count = 0
                for p in data['staff']:
                    if p['phone'] == phone:
                        phone = input('Введите новые телефон сотрудника: ')
                        data['staff'][data['staff'].index(p)]['phone'] = phone
                    else:
                        count += 1
                if count > 0:       
                    print('Такого сотрудника не существует')
    with open('Example_8/Staff.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: RemoveStaff()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()