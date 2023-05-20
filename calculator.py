from math import factorial
class Calculator:
    @staticmethod
    def add(a,b):
        """
            Складывает 2 значения.

            parans:
            a-1-ое слогаемое.
            b-2-ое слогаемое.

            return:результат сложения a и b.
       """
        return a+b

    def abs(a):
        """
            Делает модуль из числа.

            parans:
            a-число которое хотим перевести в модуль.

            return:число в модуле.
        """
        return abs(a)

    def factorial(b):
        """
            Находит факториал числа.

            parans:
            b-число факториал которого хотим найти.

            return:факориал числа.
        """
        return factorial(b)
       
       
