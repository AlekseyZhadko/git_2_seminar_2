#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial


number = input('Введите число: ')

def Numbers(n):
    try:
        n=int(n)
    except:
        n = input('Введите число: ')
        return(Numbers(n))
    for i in range(1,n+1):
        print(factorial(i))


Numbers(number)