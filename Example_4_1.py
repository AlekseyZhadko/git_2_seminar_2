# Вычислить результат деления двух чисел c заданной точностью d
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from tokenize import Double


number_1 = input('Введите число 1: ')
number_2 = input('Введите число 2: ')
d = input("Введите точность деления: ")

def division(number_a, number_b, accuracy):
    try:
        number_a=int(number_a)
        number_b=int(number_b)
        accuracy=float(accuracy)
    except:
        print("Введены не верные значения")
        number_a = input('Введите число 1: ')
        number_b = input('Введите число 2: ')
        accuracy = input("Введите точность деления: ")
        return division(number_a, number_b, accuracy)
    print(round(number_a/number_b, len(str(accuracy)) - str(accuracy).find('.') - 1))

division(number_1, number_2, d)