import math

class Calculator:
    @staticmethod
    def add(a,b):
        """
        складывай два числа.

        params:
             a-первое слогаемое
             b-второе слогаемое
        return - результат сложения a, b.
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

    @staticmethod
    def division(a, b):
        """
           Деление двух значений.

           params:
                  a-первое значение
                  b-второе значение

           return: результат деления a, b
        """
        return a/b

    @staticmethod
    def division_by_modulus(a, b):
        """
           Деление двух значений по модулю.

           params:
                  a-первое значение
                  b-второе значение

           return: результат деления по модулю a, b
        """
        return a%b