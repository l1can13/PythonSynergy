import math
a = int(input("Введите первую сторону:  "))
b = int(input("Введите вторую сторону:  "))
c = int(input("Введите третью сторону:  "))
def triangle(a,b,c):
    p = 0
    S = 0
    p = (a+b+c)/2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return(S)
res = triangle()