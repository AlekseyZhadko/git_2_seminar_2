import json
import os
import view
import controller

def AddMaster():
    data = {}
    data['master'] = []
    with open('Example_8/master.json','r', encoding='utf-8') as fh:            
        if os.stat('Example_8/master.json').st_size == 0:
            with open('Example_8/Staff.json','r', encoding='utf-8') as fh: 
                print('Выберите сотрудника:')
                data_value = {}
                data_value['staff'] = []
                data_value = json.load(fh)
                for p in data_value['staff']:
                    print(str(data_value['staff'][data_value['staff'].index(p)]['ID'])\
                        +' '+str(data_value['staff'][data_value['staff'].index(p)]['FIO']))
                ID_man = input('Введите ID: ')
            with open('Example_8/otdel.json','r', encoding='utf-8') as fh: 
                print('Выберите отдел:')
                data_value = {}
                data_value['otdel'] = []
                data_value = json.load(fh)
                for p in data_value['otdel']:
                    print(str(data_value['otdel'][data_value['otdel'].index(p)]['ID'])\
                        +' '+str(data_value['otdel'][data_value['otdel'].index(p)]['name']))
                ID_otdel = input('Введите ID: ')
            with open('Example_8/post.json','r', encoding='utf-8') as fh: 
                print('Выберите должность:')
                data_value = {}
                data_value['post'] = []
                data_value = json.load(fh)
                for p in data_value['post']:
                    print(str(data_value['post'][data_value['post'].index(p)]['ID'])\
                        +' '+str(data_value['post'][data_value['post'].index(p)]['name']))
                ID_post = input('Введите ID: ')
            data['master'].append({
                'ID_man': ID_man,
                'ID_otdel': ID_otdel,
                'ID_post': ID_post
            })
        else:
            data = json.load(fh)
            with open('Example_8/Staff.json','r', encoding='utf-8') as fh: 
                print('Выберите сотрудника:')
                data_value = {}
                data_value['staff'] = []
                data_value = json.load(fh)
                for p in data_value['staff']:
                    print(str(data_value['staff'][data_value['staff'].index(p)]['ID'])\
                        +' '+str(data_value['staff'][data_value['staff'].index(p)]['FIO']))
                ID_man = input('Введите ID: ')
            with open('Example_8/otdel.json','r', encoding='utf-8') as fh: 
                print('Выберите отдел:')
                data_value = {}
                data_value['otdel'] = []
                data_value = json.load(fh)
                for p in data_value['otdel']:
                    print(str(data_value['otdel'][data_value['otdel'].index(p)]['ID'])\
                        +' '+str(data_value['otdel'][data_value['otdel'].index(p)]['name']))
                ID_otdel = input('Введите ID: ')
            with open('Example_8/post.json','r', encoding='utf-8') as fh: 
                print('Выберите должность:')
                data_value = {}
                data_value['post'] = []
                data_value = json.load(fh)
                for p in data_value['post']:
                    print(str(data_value['post'][data_value['post'].index(p)]['ID'])\
                        +' '+str(data_value['post'][data_value['post'].index(p)]['name']))
                ID_post = input('Введите ID: ')
            data['master'].append({
                'ID_man': ID_man,
                'ID_otdel': ID_otdel,
                'ID_post': ID_post
            })
    with open('Example_8/master.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))
    step = view.step()
    if step == 1: AddMaster()
    elif step == 2: controller.mode_selection()
    elif step == 3: exit()
