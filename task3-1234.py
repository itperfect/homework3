# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента - список списков, копирует его (то есть при
# изменении списков, значения в экземпляре класса не должны меняться). Элементы списков гарантированно числа,
# и не пустые.
#
# 2. Метод size без аргументов, который возвращает кортеж вида (число строк, число столбцов).
#
# 3. Метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр
# класса Matrix)
#
# 4. На основе пункта 3 сделать метод класса create_transposed, который будет принимать на вход список списков, как и
# в пункте 1, но при этом создавать сразу транспонированную матрицу.

import numpy as np


def get_rectangle(rows=0, cols=0, max_value=0):
    if (rows == 0 or cols == 0 or max_value == 0):
        return False

    from random import randint

    result = [[randint(0, max_value) for _ in range(rows)] for _ in range(cols)]

    return result


class Matrix:
    def __init__(self, initial=[]):
        self.__value = initial

    @property
    def value(self):
        return self.__value

    def size(self):
        rows = len(self.value)
        cols = len(self.value[0])

        return rows, cols

    def transpose(self):
        rows, cols = self.size()
        self.t_value = [[self.value[x][y] for x in range(rows)] for y in range(cols)]
        return self.t_value

    @classmethod
    def create_transposed(self, initial = []):

        rows = len(initial)
        cols = len(initial[0])

        t_value = [[initial[x][y] for x in range(rows)] for y in range(cols)]

        return t_value

if __name__ == "__main__":
    my_list = get_rectangle(4, 3, 3)

#task 1
    my_matrix = Matrix(my_list)
    a = np.array(my_matrix.value)
    print(a)
    print("\n")

#task 2
    print(my_matrix.size())
    print("\n")

#task 3
    b = np.array(my_matrix.transpose())
    print(b)
    print("\n")

#task 4
    c = np.array(Matrix.create_transposed(my_list))
    print(c)

