# автор - Павлов Александр Олегович


#Задача 1

def list_transform(lst):
    res = [x ** 2 for x in lst]
    return res


print(list_transform([1, 2, 4, 0]))

		
#Задача 2 
	
def get_common_fruits(fr1,fr2):
    res = [x  for x in fr1 if x in fr2]
    return res

fr1 = ['яблоки','груши','помидоры','виноград','сливы']
fr2 = ['ананасы','сливы','картофель','яблоки','помидоры']


print(get_common_fruits(fr1,fr2))


#Задача 3

def list_filter(lst):
    return [x for x in lst if x > 0 and (x % 3 == 0) and not(x % 4 == 0)]


lst = [17,9,-4,16,18,12]

print(list_filter(lst))


