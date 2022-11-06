import random

zestaw_1 = []
zestaw_2 = []

n = int(input("Podaj liczbę elementów listy pierwszej: "))

for i in range(n):
    zestaw_1.append(random.randint(0, 10))

print(zestaw_1)


n = int(input("Podaj liczbę elementów listy pierwszej: "))

for i in range(n):
    zestaw_2.append(random.randint(5, 15))

print(zestaw_2)


x = int(input('Podaj liczbę do szukania: '))

if x in zestaw_1 and x in zestaw_2:
    print('Liczba z zestawu 1 i 2')
elif x in zestaw_1:
    print('Liczba z zestawu 1')
elif x in zestaw_2:
    print('Liczba z zestawu 2')
else:
    print('Nie ma takiej liczby w obu zestawach')


zestaw_1_2 = zestaw_1 + zestaw_2

zestaw_1_2.sort()

print(zestaw_1_2)