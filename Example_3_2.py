#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#Пример:
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: 4
#список: ["123", "234", 123, "567"], ищем: "123", ответ: 2
#список: [], ищем: "123", ответ: такой строки нет

list = ["qwe", "asd", "zxc", "waqwe", "ertqwe"]
word="qwe"
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
word2="йцу"
list3 = ["йцу", "фыв", "ячс", "цук", "кен", "йццу"]
def SearchWordInList(list, word):
    count=0
    for i in list:
        if word in i:
            count+=1
        if count > 1:
            print(f'Список: {list}')
            print(list.index(i))
            break
    if count <= 1:
        print(f'Список: {list}')
        print('Такой строки второй раз не встречается')
            
SearchWordInList(list,word)
SearchWordInList(list2,word2)
SearchWordInList(list3,word2)