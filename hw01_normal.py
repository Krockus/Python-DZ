# ����� - ������ ��������� ��������

import os
import sys


def f_GoToFolder():
    strok = input('������� ��� ����� ���� ����� �������������')
    try:
        os.chdir(strok)
        print('������� �������������')
    except:
        print('���������� �������������', strok)



def f_FolderWatch():
    try:
        print(os.listdir())
        print('������� �')
    except:
        print('���������� ����������� ���������� �����')


def f_DeleteFolder():
    strok = input('������� ��� ��������� �����')
    try:
        os.rmdir(strok)
        print('������� �������')
    except:
        print('���������� �������', strok)

def f_CreateFolder():
    strok = input('������� ��� �����')
    try:
        os.mkdir(strok)
        print('������� �������')
    except:
        print('���������� �������',strok)


def f_Exit():
    sys.exit()


func_names = {'������� � �����': f_GoToFolder, '���������� � �����': f_FolderWatch, '������� �����': f_DeleteFolder, '������� �����': f_CreateFolder, '�����': f_Exit}
menu_counts = {1: '������� � �����', 2: '���������� � �����', 3: '������� �����', 4: '������� �����', 5: '�����'}

for k in sorted(menu_counts.keys()):
    print(k, ':', menu_counts[k])

while True:

    cmd_id = input('������� �������')
    try:
        id_num = int(cmd_id)
        cmd_id = menu_counts[id_num]

    except:
        pass

    func_names[cmd_id]()
