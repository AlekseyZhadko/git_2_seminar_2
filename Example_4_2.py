# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 3 (необязательное).
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на 
# стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая команда;Забито первой командой;Вторая команда;Забитовторой командой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всего очков

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
def AddElementDict(Name,NumberOfGames,Wins,Draws,Losses,Points):
    data={}
    data["Name"]=Name
    data["NumberOfGames"] = NumberOfGames
    data["Wins"] = Wins
    data["Draws"] = Draws
    data["Losses"] = Losses
    data["Points"] = Points
    res["Games"].append(data)

res= {'Games': []}

def RemoveElementDict(Dict,NumberOfGames,Wins,Draws,Losses,Points):
    Dict["NumberOfGames"] += NumberOfGames
    Dict["Wins"] += Wins
    Dict["Draws"] += Draws
    Dict["Losses"] += Losses
    Dict["Points"] += Points

def Number(count):
    try:
        count=int(count)
        if count <= 0:
            raise Exception
    except Exception:
        count = input('Введите количество игр: ')
        return(Number(count))
    return count

num = input('Введите количество игр: ')
count = Number(num)

print('Введите результаты игры в следующем формате: \nПервая команда;Забито первой командой;Вторая команда;Забитовторой командой')

def FilterList(Str):
    try:
        if int(Str[1])<0 or int(Str[3])<0 or (Str[0].lower().strip()==Str[2].lower().strip()):
            raise Exception 
    except Exception:
        print('Введенные данные на верны')
        print('Введите результаты игры в следующем формате: \nПервая команда;Забито первой командой;Вторая команда;Забитовторой командой')
        Str = input().split(';')
        return(FilterList(Str))
    return Str

for i in range(0,int(count)):
    st = input().split(';')
    stroka = FilterList(st)
    if len(res["Games"]) != 0:
        k1=0
        k2=0
        for i in res["Games"]:
            if (stroka[0]==i["Name"]):
                k1+=1
                if int(stroka[1])>int(stroka[3]): RemoveElementDict(i,1,1,0,0,3)
                elif int(stroka[1])<int(stroka[3]): RemoveElementDict(i,1,0,0,1,0)
                else: RemoveElementDict(i,1,0,1,0,1)  
            if (stroka[2]==i["Name"]):
                k2+=1
                if int(stroka[1])>int(stroka[3]): RemoveElementDict(i,1,0,0,1,0)    
                elif int(stroka[1])<int(stroka[3]): RemoveElementDict(i,1,1,0,0,3)
                else:RemoveElementDict(i,1,0,1,0,1)            
        if k1 == 0: AddElementDict(stroka[0],1,1,0,0,3)
        if k2 == 0: AddElementDict(stroka[2],1,0,0,1,0)
    else:
        if int(stroka[1])>int(stroka[3]): 
            AddElementDict(stroka[2],1,0,0,1,0)
            AddElementDict(stroka[0],1,1,0,0,3)    
        elif int(stroka[1])<int(stroka[3]):
            AddElementDict(stroka[2],1,1,0,0,3)
            AddElementDict(stroka[0],1,0,0,1,0)
        else:     
            AddElementDict(stroka[2],1,0,1,0,1)
            AddElementDict(stroka[0],1,0,1,0,1)  

for i in res["Games"]:
    print(' '.join("{}".format(v) for v in i.values()))

