import sys	

def f_Add() :
	print('Добавляем...')
	# Вставить сюда рабочий код
	print('Добавили')

def f_Delete() :
	print('Удаляем...')
	# Вставить сюда рабочий код
	print('Удалили')

def f_Print() :
	print('Печатаем...')
	# Вставить сюда рабочий код
	print('Напечатали')
	
def f_Count() :
	print('Считаем...')
	# Вставить сюда рабочий код
	print('Посчитали')

def f_Exit() :
	sys.exit()

func_names = {'Добавляем': f_Add, 'Удаляем': f_Delete, 'Печатаем': f_Print, 'Считаем': f_Count, 'Выход': f_Exit}
menu_counts = {1: 'Добавляем',     2: 'Удаляем',         3: 'Печатаем',        4: 'Считаем',      5: 'Выход'}

for k in sorted(menu_counts.keys()) :
	print(k,':', menu_counts[k])

while True :

	cmd_id = input('Введите команду')
	try :
		id_num = int(cmd_id)
		cmd_id = menu_counts[id_num]

	except :
		pass

	func_names[cmd_id]()