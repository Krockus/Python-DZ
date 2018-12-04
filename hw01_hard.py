# автор - Павлов Александр Олегович

#Задача 1


import random

class matritsa:
    body = []
    x = 0
    y = 0
    def __init__(self,xz = 0, yz = 0):
        self.x = xz
        self.y = yz
        self.body = [[random.randint(1,100) for yt in range(yz)] for xt in range(xz)]

    def raspechatat(self):
        print(self.body)

     # транспонирование матрицы
    def transponirovat(self):
        t_matr = matritsa(self.y,self.x)
        for i in range(self.y):
            for j in range(self.x):
                t_matr.body[i][j] = self.body[j][i]

        return t_matr

    # домножение элементов на число
    def umnogenie(self,mnoj):
        u_matr = matritsa(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                u_matr.body[i][j] = self.body[i][j] * mnoj

        return u_matr

mtr = matritsa(3,4)
mtr.raspechatat()

t_mtr = mtr.transponirovat()
t_mtr.raspechatat()

u_mtr = mtr.umnogenie(2)
u_mtr.raspechatat()

