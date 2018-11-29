# автор - Павлов Александр Олегович

import os
import sys


def f_GoToFolder():
    strok = input('Введите имя папки куда нужно переместиться')
    try:
        os.chdir(strok)
        print('Успешно переместились')
    except:
        print('Невозможно переместиться', strok)



def f_FolderWatch():
    try:
        print(os.listdir())
        print('Успешно п')
    except:
        print('Невозможно просмотреть содержимое папки')


def f_DeleteFolder():
    strok = input('Введите имя удаляемой папки')
    try:
        os.rmdir(strok)
        print('Успешно удалено')
    except:
        print('Невозможно удалить', strok)

def f_CreateFolder():
    strok = input('Введите имя папки')
    try:
        os.mkdir(strok)
        print('Успешно создано')
    except:
        print('Невозможно создать',strok)


def f_Exit():
    sys.exit()


func_names = {'Перейти в папку': f_GoToFolder, 'Посмотреть в папке': f_FolderWatch, 'Удалить папку': f_DeleteFolder, 'Создать папку': f_CreateFolder, 'Выход': f_Exit}
menu_counts = {1: 'Перейти в папку', 2: 'Посмотреть в папке', 3: 'Удалить папку', 4: 'Создать папку', 5: 'Выход'}

for k in sorted(menu_counts.keys()):
    print(k, ':', menu_counts[k])

while True:

    cmd_id = input('Введите команду')
    try:
        id_num = int(cmd_id)
        cmd_id = menu_counts[id_num]

    except:
        pass

    func_names[cmd_id]()
