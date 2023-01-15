def sum_of_values(slownik):
    lista_wartosci = list(slownik.values())
    suma = 0
    for i in lista_wartosci:
        suma += i
    return suma

dict1 = {'data1':10, 'data2':-4, 'data3':2}

print(f'Suma wartości słownika: {sum_of_values(dict1)}')