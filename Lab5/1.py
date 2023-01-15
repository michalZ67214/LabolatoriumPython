values = [10, 20, 30]
keys = ['dziesięc', 'dwadziescia', 'trzydziesci']



slownik1 = {}

# slownik1 = dict(zip(keys, values))

for i in range(len(keys)):
    slownik1[keys[i]] = values[i]

slownik1 = {keys[i]:values[i]  for i in range(len(keys))}

print('Słownik 1:', slownik1)


slownik2 = dict(trzydziesci=30, czterdziesci=40, piecdziesiat=50)

print('Słownik 2:', slownik2)


slownik3 = slownik1.copy()

slownik3.update(slownik2)

print(slownik3)