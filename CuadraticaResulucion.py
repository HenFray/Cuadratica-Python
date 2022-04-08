from math import sqrt

a = int(input('valor de a:'))
b = int(input('valor de b:'))
c = int(input('valor de c:'))

x1 = 0
x2 = 0

if (b**2)-(4*a*c)<0 :
    print('ERROR: la raiz cuadrada da negativo y es imposible de resolver :c')
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))
    x1 = x1/(2*a)
    print(x1)
    x2 = (-b - sqrt((b**2)-(4*a*c)))
    x2 = x2/(2*a)
    print(x2)

exit = input('hecho por Mauro Franetovich')