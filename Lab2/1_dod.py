import sys

def convert_to_10(l, p):
    numbers = []
    for i in l:
        numbers.append(int(i))

    if max(numbers) > p-1:
        sys.exit('Podana liczba nie jest ' + system_of_number[p])

    numbers.reverse()

    number_in_10 = 0

    for i in range(len(numbers)):
        number_in_10 += numbers[i] * pow(p, i)

    print('Podana liczba w systemie dziesiętnym wynosi: ', end='')
    print(int(number_in_10))


system_of_number = {
  2: "binarna",
  3: "trójkowa",
  4: "czwórkowa",
  5: "piątkowa",
  6: "szóstkowa",
  7: "siódemkowa",
  8: "ósemkowa",
  9: "dziewiątkowa"
}


liczba = input('Podaj liczbę: ')
if not liczba.isnumeric():
    sys.exit('Nieprawidłowa liczba')

p = int(input('Podaj system pozycyjny (2-10): '))

if p in range(2, 11):
    convert_to_10(liczba, p)
else:
    print('Błędny system pozycyjny')