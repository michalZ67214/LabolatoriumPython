def find(lista, wartosc):
    new_list = []
    for i in range(len(lista)):
        if lista[i] == wartosc:
            new_list.append(i)

    return new_list


l1 = [1, 2, 1, 1, 3, 5]

wartosc_szukana = 1


lista_indeksow = find(l1, wartosc_szukana)

print(lista_indeksow)