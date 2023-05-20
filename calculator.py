class Calculator:
    """def add(a, b):
        slozhenie.

        params: 
            a - pervoe ch.
            b - vtoroe ch.
        return: result slozhenia a, b.
        
       return a+b
       """
    @ staticmethod
    def root_extraction(a, n,):
        """
        vivod korna n-stepeni
        params:
            a - ch
            n - stepen korna
            returne: n koren iz a
        """
        return a**(1/n)

    @ staticmethod
    def exponentiation(a, n,):
        """
        vvod v stepen
        params:
            a - ch
            n - stepen 
            returne: a v stepeni n
        """
        return a**n
