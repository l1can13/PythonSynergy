from calculator import Calculator
operaition=''
a=None

operaition = ['+','-','/','*','%','off']
while operaition !='off':
    operaition = input("ввидите операцию:+,-,/,*,%")
    a=input('Введите первый оператор')
    в=input('Введите второй оператор')
    if operaition not in operaitions:
        print('вы ввели неверную операцию')
        continue
    if operaition =='+':
        print('результат',operaition,'равен',Calculator.add(a,b))
    if operaition =='*':
        print('результат',operaition,'равен',Calculator.multiplication(A,B))
    



