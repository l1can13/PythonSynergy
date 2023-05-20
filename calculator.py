from math import tanh,ctg
class Calculator:
    @staticmethod
    def add(a,b):
        """Складывает два значения.
        params:
            a - первое.
            b - второое.
        return: результат ложения a,b.
        """
        return a+b

    def tg(a):
        """Вычисляет тангенс a.
        params:
        a - первое.
        tanh - вычисляет тангенс.
        return: результат вычисления.
        """
        return tanh(a)
    def ctg(a):
        """Вычисляет котангенс a.
        params :
        a - первое.
        ctg - вычесляет котангенс.
        return: результат вычисления 
        """
        return ctg(a)
