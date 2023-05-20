class Calculator:
    @ staticmethod
    def add(a,b):
        """складывает два значения
        params:
         а - первое слагаемое.
         b - второе слагаемое.
        return: результат сложение a,b.
        """
        return a+b
    @ staticmethod
    def twotothepower(n):
        """ значеие 2 в степени n
        params:
        n = n-ная степеть
        return: результат 2 в n-ной степени
        """
        return 2^n
    @ staticmethod
    def invert(у):
        """инвертирование
        params:
         а - число 
        return: инвертировали число в минус n-ной степени
        """
        return 1/у^-1