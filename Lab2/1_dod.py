import sys

# 110 (2) -> 6 (10)
# 0 * 2^0 + 1 * 2^1 + 1 * 2^2 = 0 + 2 + 4 = 6

def convert_to_10(l, p):
    numbers = []
    for i in l:
        numbers.append(int(i))

    if max(numbers) > p-1:
        print('Podana liczba nie jest ' + system_of_number[p])
        sys.exit()

    numbers.reverse()

    number_in_10 = 0

    for i in range(len(numbers)):
        number_in_10 += numbers[i] * pow(p, i)

    print('Podana liczba w systemie dziesiętnym wynosi: ', end='')
    print(number_in_10)


system_of_number = {
  2: "binarna",
  3: "trójkowa",
  4: "czwórkowa",
  5: "piątkowa",
  6: "szóstkowa",
  7: "siódemkowa",
  8: "ósemkowa",
  9: "dziewiątkowa",
}


liczba = input('Podaj liczbę: ')

p = int(input('Podaj system pozycyjny (2-10): '))

if p == 10:
    print('Podana liczba w systemie dziesiętnym wynosi: ', end='')
    print(liczba)
elif p in range(2, 10):
    convert_to_10(liczba, p)
else:
    print('Błędny system pozycyjny')