import math


class Calculator:
    @staticmethod
    def add(a, b):
        """
        складывай два числа.

        params:
             a-первое слогаемое
             b-второе слогаемое
        return - результат сложения a, b.
        """

        return a + b

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

        return a / b

    @staticmethod
    def division_by_modulus(a, b):
        """
           Деление двух значений по модулю.

           params:
                  a-первое значение
                  b-второе значение

           return: результат деления по модулю a, b
        """

        return a % b

    @staticmethod
    def tg(a):
        """Вычисляет тангенс a.
        params:
        a - первое.
        tanh - вычисляет тангенс.
        return: результат вычисления.
        """

        return math.tan(a)

    @staticmethod
    def ctg(x):
        return 1 / math.tan(x)

    @staticmethod
    def root_extraction(a, n, ):
        """
        vivod korna n-stepeni
        params:
            a - ch
            n - stepen korna
            returne: n koren iz a
        """

        return a ** (1 / n)

    @staticmethod
    def exponentiation(a, n, ):
        """
        vvod v stepen
        params:
            a - ch
            n - stepen 
            returne: a v stepeni n
        """

        return a ** n

    @staticmethod
    def sub(A, B):
        """
        Вычитается два числа.

        params:
            A-Уменьшаемое.
            B-Вычитаемое.

        return: Результат вычитаемого A,B.
        """

        return A - B

    @staticmethod
    def multiplication(A, B):
        """
        Умножается два числа.

        params:
             A-Множимое.
             B-Множитель.

        return: Результат умножения A,B.
        """

        return A * B

    @staticmethod
    def twotothepower(n):
        """ значеие 2 в степени n
        params:
        n = n-ная степеть
        return: результат 2 в n-ной степени
        """

        return 2 ^ n

    @staticmethod
    def invert(y):
        """инвертирование
        params:
         а - число
        return: инвертировали число в минус n-ной степени
        """

        return 1 / y ** -1

    @staticmethod
    def abs(a):
        """
            Делает модуль из числа.

            parans:
            a-число которое хотим перевести в модуль.

            return:число в модуле.
        """

        return abs(a)

    @staticmethod
    def fact(b):
        """
            Находит факториал числа.

            parans:
            b-число факториал которого хотим найти.

            return:факориал числа.
        """

        return math.factorial(b)
