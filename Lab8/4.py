def znaki(string_):
    slownik = {}
    for i in string_:
        if i not in slownik.keys():
            slownik[i] = string_.count(i)

    return slownik


string1 = 'aaabbc'

print(znaki(string1))
