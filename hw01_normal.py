
# автор - Павлов Александр Олегович

#Задача 1

import random

def create_random_file(nam):
    strok = ''
    for i in range(2500) :
        ch = str(random.randint(0,9))
        strok += ch
    f = open(nam, 'w')
    f.write(strok)
    f.close()

def longest_sequence_in_file(nam):
    f = open(nam,'r')
    strok = f.read()
    f.close()
    curr_length = 1;
    curr_symb = strok[0];
    max_length = 1;
    max_symb = strok[0];
    for i in range(len(strok) - 1):
        if strok[i + 1] == curr_symb:
            curr_length += 1
            if curr_length > max_length :
                max_length = curr_length
                max_symb = curr_symb
        else:
            curr_length = 1
            curr_symb = strok[i + 1]

    res = ''
    for j in range(max_length) :
        res += max_symb
    return res


create_random_file('D:\\work\\AI\\random.txt')
print(longest_sequence_in_file('D:\\work\\AI\\random.txt'))


#Задача2

import random

def create_matrix(size):
    x = random.randint(0,size-1)
    y = random.randint(0,size-1)
    matr = [[random.randint(1,9) for j in range(size) ] for i in range(size)]
    matr[x][y] = 0
    return matr


print(create_matrix(5))


