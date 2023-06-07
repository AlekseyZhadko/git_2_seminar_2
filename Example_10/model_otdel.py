import json
import os
import view
import controller

def AddOtdel():
    data = {}
    data['otdel'] = []
    with open('Example_8/otdel.json','r', encoding='utf-8') as fh:            
        if os.stat('Example_8/otdel.json').st_size == 0:
            data['otdel'].append({
                'ID': '0',
                'name': input('Введите название отдела: ')
            })
        else:
            data = json.load(fh)
            data['otdel'].append({
                'ID': str(int(data['otdel'][len(data['otdel'])-1]['ID'])+1),
                'name': input('Введите название отдела: ')
            })
    with open('Example_8/otdel.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: AddOtdel()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()

def DelOtdel():
    data = {}
    data['otdel'] = []
    with open('Example_8/otdel.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/otdel.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            name = input('Введите название отдела, который нужно удалить: ')
            data = json.load(fh)
            count = 0
            for p in data['otdel']:
                if p['name'] == name:
                    data['otdel'].pop(data['otdel'].index(p))
                else:
                    count += 1
            if count > 0:       
                print('Такого отдела не существует')
    with open('Example_8/otdel.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: DelOtdel()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
            

def RemoveOtdel():
    data = {}
    data['otdel'] = []
    with open('Example_8/otdel.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/otdel.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            name = input('Введите название отдела, который нужно изменить: ')
            data = json.load(fh)
            count = 0
            for p in data['otdel']:
                if p['name'] == name:
                    name = input('Введите новое название отдела: ')
                    data['otdel'][data['otdel'].index(p)]['name'] = name
                else:
                    count += 1
            if count > 0:       
                print('Такого отдела не существует')
    with open('Example_8/otdel.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: RemoveOtdel()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()