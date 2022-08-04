from datetime import datetime as dt

def calc_log(step,data=''):
    time = dt.now().strftime('%H:%M')
    with open('Example_7/log.txt','a', encoding='utf-8') as file:
        file.writelines(f'{time} {step} {data} \n')