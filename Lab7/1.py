import numpy as np

lista = []

for i in range(7, -1, -1):
    lista.append(2 ** i)

print(lista)


wagi = np.array(lista)
print(f"Wagi: {wagi}")

liczba_bin = np.random.randint(low=0, high=2, size=(8,))
print(liczba_bin)

iloczyn = wagi * liczba_bin
print(f'mnożenie: {iloczyn}')

d = iloczyn.sum()

print(f'liczba dziesiętna: {d}')