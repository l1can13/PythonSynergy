class Calculator:
    @staticmethod
    def add(a, b):
        """
           Складывает два значения.

           params:
                  a-первое слагаемое
                  b-второе слагаемое

           return: результат сложения a, b
        """
        return a+b

#Деление, деление по модулю.
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