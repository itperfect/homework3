#
# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента - список списков, копирует его (то есть при
# изменении списков, значения в экземпляре класса не должны меняться). Элементы списков гарантированно числа, и не пустые.
#
# 2. Метод size без аргументов, который возвращает кортеж вида (число строк, число столбцов).
#
# 3. Метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)
#
# 4. На основе пункта 3 сделать метод класса create_transposed, который будет принимать на вход список списков, как и
# в пункте 1, но при этом создавать сразу транспонированную матрицу.

import sys
from pprint import pprint


class MyLists:

    @staticmethod
    def get_rectangle_list(n=0, p=0, z=0):
        '''
        Заполняет прямоугольную матрицу заданного размера
        :param n: Количество столбцов
        :param p:
        :param z:
        :return:
        '''



    @staticmethod
    def get_random_list(n=0, p=0, z=0):
        '''

        генерирует произвольное(<=n) кол-во списков произвольной(<=p) длинны с произвольными(<=z) значениями элементов.

        :param n: max count of inner lists
        :param p: max length of list
        :param z: max element value
        :return: list of lists
        '''

        if n==0 or p==0 or z==0:
            return False

        import random

        result = []

        curr_n = random.randint(1, n + 1)
        for x in range(0, curr_n):
            inner_list = []
            curr_p = random.randint(1, p + 1)
            for y in range(0, curr_p):
                curr_z = random.randint(0, z + 1)
                inner_list.append(curr_z)

            result.append(inner_list)

        return result


class Matrix:

    def __init__(self, initial = None):
        self.value = initial

    def size(self):
        strings_cnt = len(self.value)

        a = list()

        for s in range(0, strings_cnt):
            a.append(len(self.value[s]))

        return strings_cnt, tuple(a)

    def transpose():
        pass

    @classmethod
    def create_transposed():
        pass

    def __setattr__(self, key, new_value):
        if key == 'value':
            if key not in self.__dict__ or self.__dict__[key] == None:
                self.__dict__[key] = new_value
            else:
                pass
        else:
            self.__dict__[key] = new_value


if __name__ == "__main__":
    auto_list = MyLists.get_random_list(2, 5, sys.maxsize//1000000000)

    obj = Matrix(auto_list)
    pprint(obj.value)

    print(obj.size())


    print(len(obj.size()))