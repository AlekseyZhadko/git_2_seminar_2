# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import json

with open('Example_5_1_polynomial_1.json', 'r',encoding='utf-8') as fh:
    polynomial_1 = json.load(fh)
print('Первый многочлен:')
print(polynomial_1)

with open('Example_5_1_polynomial_2.json', 'r',encoding='utf-8') as fh:
    polynomial_2 = json.load(fh)
print('Второй многочлен:')
print(polynomial_2)

def polynomial_znak(poly_1):
    count = 0
    for i in poly_1:
        if '-' in i:
            count+=1
            polyif = i.split('-')
            if len(polyif)>=2 and polyif[0] !='':
                for j in range(1,len(polyif)):
                    polyif[j]='-'+polyif[j]
                    poly_1.append(polyif[j])
                if polyif[0] !='':
                    poly_1.append(polyif[0])
                poly_1.pop(poly_1.index(i))
                return polynomial_znak(poly_1)
    if count == 0:
        return poly_1

def polynomial(poly_1,poly_2,poly_res):
    count = 0
    for i in poly_1:
        if '*' in i:
            param_1=i.split('*')
        else:
            param_1=i
        for j in poly_2:
            if '*' in j:
                param_2=j.split('*')
            else:
                param_2=j
            if type(param_1)==str and type(param_2)==str:
                if param_1.isdigit()==True and param_2.isdigit()==True:
                    if poly_res != '':
                        if (int(param_1)+int(param_2))>0:
                            poly_res=poly_res+'+'
                        elif (int(param_1)+int(param_2))<=0:
                            poly_res=poly_res+''
                    if (int(param_1)+int(param_2))!=0:
                        poly_res=poly_res+str(int(param_1)+int(param_2))
                        poly_2.pop(poly_2.index(j))
                        poly_1.pop(poly_1.index(i))
                        count+=1
                        return polynomial(poly_1,poly_2,poly_res) 
                if param_1 == param_2:
                    poly_res=poly_res+'+'
                    poly_res=poly_res+'2'+param_1
                    poly_2.pop(poly_2.index(j))
                    poly_1.pop(poly_1.index(i))
                    count+=1
                    return polynomial(poly_1,poly_2,poly_res)  
            elif type(param_1)==list and type(param_2)==list:
                if param_1[1] == param_2[1]:
                    if poly_res != '':
                        if (int(param_1[0])+int(param_2[0]))>0:
                            poly_res=poly_res+'+'
                        elif (int(param_1[0])+int(param_2[0]))<=0:
                            poly_res=poly_res+''
                    if (int(param_1[0])+int(param_2[0]))!=0:
                        poly_res=poly_res+str(int(param_1[0])+int(param_2[0]))+param_1[1]
                        poly_2.pop(poly_2.index(j))
                        poly_1.pop(poly_1.index(i))
                        count+=1
                        return polynomial(poly_1,poly_2,poly_res) 
    if count == 0:
        return poly_res

polynomial_1 = polynomial_1.split('+')
polynomial_znak(polynomial_1)
print('Первый многочлен, разбитый на элементы:')
print(polynomial_1)
polynomial_2 = polynomial_2.split('+')
polynomial_znak(polynomial_2)
print('Второй многочлен, разбитый на элементы:')
print(polynomial_2)
polynomial_res = ''
polynomial_res=polynomial(polynomial_1,polynomial_2,polynomial_res)

if len(polynomial_1) != 0:
    for i in polynomial_1:
        if polynomial_res != '':
            if '-' in i:
                polynomial_res=polynomial_res+''
            else:
                polynomial_res=polynomial_res+'+'
        polynomial_res=polynomial_res+i

if len(polynomial_2) != 0:
    for i in polynomial_2:
        if polynomial_res != '':
            if '-' in i:
                polynomial_res=polynomial_res+''
            else:
                polynomial_res=polynomial_res+'+'
        polynomial_res=polynomial_res+i   

print('Результат сложения многочленов:')
print(polynomial_res)
with open('Example_5_1_polynomial_res.json','w', encoding='utf-8') as fh:
        fh.writelines(json.dumps(polynomial_res,indent=3, ensure_ascii=False))