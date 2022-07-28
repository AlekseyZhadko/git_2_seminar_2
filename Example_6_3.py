#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
import json

with open('Example_6_3_Stroka.json', 'r',encoding='utf-8') as fh:
    Stroka = json.load(fh)

def encoding(stroka):
    stroka = [stroka[i] for i in range(len(stroka))]
    count=1
    RLE=''
    for i in range(len(stroka)-1):
        if stroka[i]==stroka[i+1]:
            count+=1
        else:
            RLE+=str(count)+stroka[i]
            count=1
    if stroka[len(stroka)-1] != stroka[len(stroka)-2]:
        RLE+='1'+stroka[len(stroka)-1]
    else:
        RLE+=str(count)+stroka[len(stroka)-1]
    with open('Example_6_3_RLE_encoding.json','w', encoding='utf-8') as fh:
        fh.writelines(json.dumps(RLE,indent=3, ensure_ascii=False))
    return RLE

def decoding(stroka):
    RLE=''
    for i in range(0,len(stroka),2):
        for j in range(0,int(stroka[i])):
            RLE+=stroka[i+1]
    with open('Example_6_3_RLE_decoding.json','w', encoding='utf-8') as fh:
        fh.writelines(json.dumps(RLE,indent=3, ensure_ascii=False))
    return RLE

print(Stroka)
Stroka=encoding(Stroka)
print(Stroka)
Stroka=decoding(Stroka)
print(Stroka)