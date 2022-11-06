import sys

def convert_from_10(l, p):
    final_number = ''
    tmp_number = l
    while tmp_number > 0:
        if p == 16 and tmp_number % p >= 10:
            final_number += hex_[str(tmp_number % p)]
        else:
            final_number += str(tmp_number % p)
        tmp_number //= p

    final_number = final_number[::-1]
    
    print(str(l) + ' w systemie ' + system_of_number[p] + ' wynosi ' + final_number)


system_of_number = {
  2: "binarnym",
  3: "trójkowym",
  4: "czwórkowym",
  5: "piątkowym",
  6: "szóstkowym",
  7: "siódemkowym",
  8: "ósemkowym",
  9: "dziewiątkowym",
  10: "dziesiętnym",
  16: "szesnastkowym"
}

hex_ = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}


try:
    liczba = int(input('Podaj liczbę dziesiętną: '))
except ValueError:
    sys.exit('Nieprawidłowa liczba')

p = int(input('Podaj system pozycyjny (2-10 lub 16): '))


if p in range(2, 11) or p == 16:
    convert_from_10(liczba, p)
else:
    print('Błędny system pozycyjny')