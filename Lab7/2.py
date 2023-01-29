import numpy as np

macierz = np.random.randint(0, 51, (5, 5))

print(macierz)

min_ = macierz.min()
max_ = macierz.max()

print()
print(f'wartość minimalna: {min_}')
print(f'wartość maksymalna: {max_}')

max_in_column = np.max(macierz, 0)
max_in_row = np.max(macierz, 1)

print()
print(f'Wartości maksymalne dla kolumn: {max_in_column}')
print(f'Wartości maksymalne dla wierszy: {max_in_row}')

print()
print(f'Sumy dla poszczególnych wierszy: {macierz.sum(1)}')