#Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
#Порядок элементов менять нельзя.
#Пример:
#[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
#[1, 5, 2, 3, 4, 1, 7] => [1, 5]

def Sequence(list_sequence):
    min_sequence = min(list_sequence)
    for i in list_sequence:
        if min_sequence == i: list_sequence.pop(list_sequence.index(i))
    max_sequence = min(list_sequence)
    for i in list_sequence:
        if max_sequence == i: list_sequence.pop(list_sequence.index(i))
    difference=max_sequence-min_sequence
    max_sequence=Search_Max_Sequence(list_sequence,max_sequence,difference)
    list_res=[]
    list_res.append(min_sequence)
    list_res.append(max_sequence)
    return list_res
         
def Search_Max_Sequence(list_sequence, max_sequence, difference):
    count=0
    for i in list_sequence:
        if max_sequence+difference == i:
            count+=1
            max_sequence+=difference
            return Search_Max_Sequence(list_sequence,max_sequence,difference)
    if count == 0:
        return max_sequence
    
list_1 = [1, 5, 2, 3, 4, 1, 7] 
print(list_1)
print(Sequence(list_1))