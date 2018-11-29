# автор - Павлов Александр Олегович

#Задача 1


import os

def create_dirs():
    for i in range(1,10):
        os.mkdir('dir_' + str(i))


def delete_dirs():
    for i in range(1,10):
        os.rmdir('dir_' + str(i))

#create_dirs()
#delete_dirs()
	
			
#Задача 2   

import os
	
print([x for x in os.listdir() if os.path.isdir(x)])


#Задача 3

import os
import shutil


fil = os.path.realpath(__file__)
shutil.copy(fil,'copy_file.py')