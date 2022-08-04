import log
import model_rational
import model_complex
import model_calculating_the_expression
import view
import os 

def mode_selection():
    os.system('CLS') 
    mode_selection = ['Режим - Вычисление выражения','Режим - Калькулятор','Режим - Калькулятор для комплексных чисел']
    for i, val in enumerate(mode_selection, start=1):
        print(f'{i} {"".join(val)}')
    mode = int(input('Выберите режим: '))
    if mode == 1:
        log.calc_log('Выбран режим - Вычисление выражения ')
        button_click_expression()
    elif mode == 2:
        log.calc_log('Выбран режим - Калькулятор ')
        button_click_rational()
    elif mode == 3:
        log.calc_log('Выбран режим - Калькулятор для комплексных чисел ')
        button_click_complex()

def button_click_expression():
    result = model_calculating_the_expression.expression()
    log.calc_log('Результат = ',result)
    view.view_data(result)
    
def button_click_complex():
    mode = view.mode_2()
    if mode == 1:
        value_a = view.get_value()
        log.calc_log('Значение 1 = ',str(value_a))
        model_complex.init(value_a)
        result = model_complex.complex_sqrt()
        log.calc_log('Квадратный корень')
    log.calc_log('Результат = ',result)
    view.view_data(result)

def button_click_rational():
    mode = view.mode()
    if mode>=1 and mode<=5:
        value_a = view.get_value()
        log.calc_log('Значение 1 = ',str(value_a))
        value_b = view.get_value()
        log.calc_log('Значение 2 = ',str(value_b))
        model_rational.init(value_a,value_b)
    elif mode>=6 and mode<=11:
        value_a = view.get_value()
        log.calc_log('Значение 1',str(value_a))
        model_rational.init(value_a)
    if mode == 1: 
        result = model_rational.rational_sum()
        log.calc_log('Сложение')
    elif mode == 2: 
        result = model_rational.rational_div()
        log.calc_log('Деление')
    elif mode == 3: 
        result = model_rational.rational_mult()
        log.calc_log('Умножение')
    elif mode == 4: 
        result = model_rational.rational_sub()
        log.calc_log('Вычетание')
    elif mode == 5: 
        result = model_rational.rational_pow_n()
        log.calc_log('Возведение в степень N')
    elif mode == 6: 
        result = model_rational.rational_sqrt()
        log.calc_log('Квадратный корень')
    elif mode == 7: 
        result = model_rational.rational_pow_2()
        log.calc_log('Возведение в квадрат')
    elif mode == 8: 
        result = model_rational.rational_fact()
        log.calc_log('Факториал')
    elif mode == 9: 
        result = model_rational.rational_sin()
        log.calc_log('Синус')
    elif mode == 10: 
        result = model_rational.rational_cos()
        log.calc_log('Косинус')
    elif mode == 11: 
        result = model_rational.rational_tan()
        log.calc_log('Тангенс')
    log.calc_log('Результат = ',str(result))
    view.view_data(result)