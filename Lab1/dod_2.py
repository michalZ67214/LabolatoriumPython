a = float(input('Podaj współczynnik a: '))
b = float(input('Podaj współczynnik b: '))

if a == 0:
    if b == 0:
        print('Równanie tożsamościowe')
        exit()
    else:
        print('Równanie sprzeczne')
        exit()

print(f'x= {(-b)/a}')