__author__ = '������ ��������� ��������'


#������1

def finding_sqrts(list) :
	res = []
	for el in list :
		if el > 0 :
			new_val = el**0.5
			if (new_val % 1 == 0) :
				res.append(new_val)
	return res

print(finding_sqrts([37,-4,5,-3,64,5,9,7,4]))


#������2

# ������ �� ���������� ��� � �������?
# � ����������� ������ �������� � ������������ ����� ���
# � ����� 2.pdf � ���������� ����� ��� ���
# �������� ��� ������ � ����� ������� � ������ ��� �����������
# ��������� ��� ��������� ���� � ����� �� �������
# ��� � � ������� ������� ������ ����������
# ����� ������� ��� ����������� �������� ��� � �������?
# ����������� ������������� ����� ������� �������� � ���� ������� ���������
# � ��� ��� � ����� ��� ���� ������ � ������� ����� � ���� �������� �� ����

import datetime

def print_date_as_str(str_dat) :
	date = datetime.datetime.strptime(str_dat,'%d.%M.%Y')
	res = datetime.date.strftime(date,"%d-%m-%Y")
	print(res)

print_date_as_str('02.11.2013')


#������3

import random

def create_random_list(n) :
	res = []
	random.seed()
	for i in range(n) :
		el = random.randint(-100,100)
		res.append(el)
	return res

print(create_random_list(10))


#������ 4

def get_two_lists(origin) :
	res1 = []
	res2 = []

	for num in range(len(origin)) :
		
		el = origin[num]
		first_occur = el in origin[:num]
		if not first_occur :
			res1.append(el)
			second_occur = el in origin[num+1:]
			if not second_occur :
				res2.append(el)
	res = [res1,res2]
	return res



list = [1, 2, 4, 5, 6, 2, 5, 2]
res = get_two_lists(list)
print(res[0],'------',res[1])