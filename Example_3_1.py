#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
#Пример:
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
word="qwe"
list2 = ["йцу", "фыв", "ячс", "цукйцу", "йцукен", "йцу"]
word2="йцу"
def SearchWordInList(list, word):
    count=0
    for i in list:
        if word in i:
            count+=1
    print(f'Список: {list}')
    print(f'Ответ: {count}')

SearchWordInList(list,word)
SearchWordInList(list2,word2)