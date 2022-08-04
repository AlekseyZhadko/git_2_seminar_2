import log 

def staples(stroka):
    count=0
    stroka_res=''
    for i in stroka:
        if '(' == i:
            count=1
            start=stroka.index(i)
        if ')' == i:
            finish=stroka.index(i)
    if count==1:
        res = stroka[start+1:finish]
        res= calc(res)
        stroka_res=stroka[:start]+str(res)+stroka[finish+1:]
        print(stroka_res)
        return staples(stroka_res)
    else: 
        return calc(stroka)


def calc(stroka):
    count=0
    operation=['*','/','+','-']
    for i in operation:
        if i in stroka:
            count+=1
            if i=='*':
                number=int(stroka[stroka.index(i)-1])*int(stroka[stroka.index(i)+1])
                stroka_res=stroka[:stroka.index(i)-1]+str(number)+stroka[stroka.index(i)+2:]
                return calc(stroka_res)
            if i=='+':
                number=int(stroka[stroka.index(i)-1])+int(stroka[stroka.index(i)+1])
                stroka_res=stroka[:stroka.index(i)-1]+str(number)+stroka[stroka.index(i)+2:]
                return calc(stroka_res)
            if i=='-':
                number=int(stroka[stroka.index(i)-1])-int(stroka[stroka.index(i)+1])
                stroka_res=stroka[:stroka.index(i)-1]+str(number)+stroka[stroka.index(i)+2:]
                return calc(stroka_res)
            if i=='/':
                number=int(stroka[stroka.index(i)-1])/int(stroka[stroka.index(i)+1])
                stroka_res=stroka[:stroka.index(i)-1]+str(number)+stroka[stroka.index(i)+2:]
                return calc(stroka_res)
    if count==0:
        return stroka

def expression():
    stroka = input('Введите выражение: ')
    log.calc_log('Выражение: ',stroka)
    return staples(stroka)


