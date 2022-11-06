print('Jaką operację chcesz wykonać?\n1)dodawanie\n2)odejmowanie\n3)mnożenie\n4)dzielenie\n5)potęgowanie')

op = int(input('Wpisz numer operacji: '))

if op == 1:
    a = float(input('Podaj argument 1: '))
    b = float(input('Podaj argument 2: '))
    print('Wynik: ', a+b)
elif op == 2:
    a = float(input('Podaj argument 1: '))
    b = float(input('Podaj argument 2: '))
    print('Wynik: ', a - b)
elif op == 3:
    a = float(input('Podaj argument 1: '))
    b = float(input('Podaj argument 2: '))
    print('Wynik: ', a * b)
elif op == 4:
    a = float(input('Podaj argument 1: '))
    b = float(input('Podaj argument 2: '))
    if b == 0:
        print('Nie można dzielić przez 0')
        exit()
    print('Wynik: ', a / b)
elif op == 5:
    a = int(input('Podaj argument 1: '))
    b = int(input('Podaj argument 2: '))
    print(f'Wynik {a}^{b} : ', pow(a, b))
else:
    print('Nieprawidłowa operacja')