wiek = int(input('Wprowadź wiek klienta: '))

if wiek < 4:
    print('Bilet bezpłatny')
elif wiek >= 4 and wiek <=18:
    print('Cena biletu: 10zł')
else:
    print('Cena biletu: 20zł')