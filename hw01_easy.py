
__author__ = 'Павлов Александр Олегович'

#задача1

#вариант1
def print_list(spisok) :
	сч = 1
	for el in spisok :
		print(str(сч)+'.',el)
		сч = сч + 1


spisok =  ["яблоко", "банан", "киви", "арбуз"]
print_list(spisok)

#вариант2
def print_list2(spisok) :
	for i in range(len(spisok)) :
		print(str(i+1)+'.',spisok[i])


spisok =  ["яблоко", "банан", "киви", "арбуз"]
print_list2(spisok)


#задача2

def remove_unwanted_elements(target,unwanted) :
	for el in target :
		if unwanted.count(el) > 0 :
			target.remove(el)

target = ['a','b','c','d','b','c','e']
unwanted = ['e','g','b','c','f']


remove_unwanted_elements(target,unwanted)
print(target)


#задача 3

def new_remade_list(origin) :
	res = []
	new_val = 0
	for el in origin :
		if el % 2 == 0 :
			new_val = el / 4
		else :
			new_val = el * 2
		res.append(new_val)
	return res

print(new_remade_list([2,54,17,2,3,13,24]))