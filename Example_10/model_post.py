import json
import os
import view
import controller

def AddPost():
    data = {}
    data['post'] = []
    with open('Example_8/post.json','r', encoding='utf-8') as fh:            
        if os.stat('Example_8/post.json').st_size == 0:
            data['post'].append({
                'ID': '0',
                'name': input('Введите название должности: ')
            })
        else:
            data = json.load(fh)
            data['post'].append({
                'ID': str(int(data['post'][len(data['post'])-1]['ID'])+1),
                'name': input('Введите название должности: ')
            })
    with open('Example_8/post.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: AddPost()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()

def DelPost():
    data = {}
    data['post'] = []
    with open('Example_8/post.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/post.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            name = input('Введите название должности, которую нужно удалить: ')
            data = json.load(fh)
            count = 0
            for p in data['post']:
                if p['name'] == name:
                    data['post'].pop(data['post'].index(p))
                else:
                    count += 1
            if count > 0:       
                print('Такой должности не существует')
    with open('Example_8/post.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: DelPost()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
            

def RemovePost():
    data = {}
    data['post'] = []
    with open('Example_8/post.json','r', encoding='utf-8') as fh: 
        if os.stat("Example_8/post.json").st_size == 0:
            print('Файл пустой или не существует.')
        else:
            name = input('Введите название должности, которую нужно изменить: ')
            data = json.load(fh)
            count = 0
            for p in data['post']:
                if p['name'] == name:
                    name = input('Введите новую должность: ')
                    data['post'][data['post'].index(p)]['name'] = name
                else:
                    count += 1
            if count > 0:       
                print('Такой должности не существует')
    with open('Example_8/post.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: RemovePost()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
