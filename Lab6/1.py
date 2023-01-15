def imie_nazwisko(imie, wiek=20):
    """Funkcja wypisuje imię i wiek"""
    print(f'Imie: {imie}, wiek: {wiek}')

imie_nazwisko('imie1', 25)
imie_nazwisko('imie2')

print(imie_nazwisko.__doc__)