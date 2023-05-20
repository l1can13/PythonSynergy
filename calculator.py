import math

class Calculator:
    @staticmethod
    def add(a,b):
        """
        складывай два числа.

        params:
             a-первое слогаемое
             b-второе слогаемое
        1`return - результат сложения a;b.
        """
        return a+b

    @staticmethod
    def grad_to_rad(grad):
        return grad / 360 * math.pi * 2

    @staticmethod
    def cos(a):
        """
        находит косинус заданного угла

        params:
            a-угол
            return- значение косинуса
        """
        return math.cos(Calculator.grad_to_rad(a))
    @staticmethod
    def sin(a):
        """
        находит синус заданного угла

        params:
            a-угол
            return- значение синуса
        """
        return math.sin(Calculator.grad_to_rad(a))

        