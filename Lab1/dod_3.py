import math
a = float(input('Podaj współczynnik a: '))
b = float(input('Podaj współczynnik b: '))
c = float(input('Podaj współczynnik c: '))

d = (pow(b, 2)) - (4 * a * c)

if d > 0:
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)
    print(f'x1= {x1}')
    print(f'x2= {x2}')
elif d == 0:
    x0 = (-b) / (2*a)
    print(f'x0= {x0}')
else:
    print('brak pierwiastów')