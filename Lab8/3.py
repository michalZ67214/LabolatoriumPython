import sys

def potega(lista1, lista2):
    if len(lista1) != len(lista2):
        print('Listy muszą być tej samej długości')
        sys.exit()

    lista_z_potegami = []
    for i in range(len(lista1)):
        lista_z_potegami.append(lista1[i] ** lista2[i])

    return lista_z_potegami


l1 = [2, 2]
l2 = [2, 3]

print(potega(l1, l2))