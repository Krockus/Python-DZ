import sys	

def f_Add() :
	print('���������...')
	# �������� ���� ������� ���
	print('��������')

def f_Delete() :
	print('�������...')
	# �������� ���� ������� ���
	print('�������')

def f_Print() :
	print('��������...')
	# �������� ���� ������� ���
	print('����������')
	
def f_Count() :
	print('�������...')
	# �������� ���� ������� ���
	print('���������')

def f_Exit() :
	sys.exit()

func_names = {'���������': f_Add, '�������': f_Delete, '��������': f_Print, '�������': f_Count, '�����': f_Exit}
menu_counts = {1: '���������',     2: '�������',         3: '��������',        4: '�������',      5: '�����'}

for k in sorted(menu_counts.keys()) :
	print(k,':', menu_counts[k])

while True :

	cmd_id = input('������� �������')
	try :
		id_num = int(cmd_id)
		cmd_id = menu_counts[id_num]

	except :
		pass

	func_names[cmd_id]()