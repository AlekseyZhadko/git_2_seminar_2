#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

number = input('Введите число: ')

def Summ(n):
    sum = 0
    try:
        float(n)
    except:
        n = input('Введите число: ')
        return(Summ(n))
    for element in n:
        if element != ".":
            sum += int(element)
    print(sum)

Summ(number)