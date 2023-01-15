def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b

def dzielenie(a,b):
    if b == 0:
        return None
    else:
        return a/b

a = 1
b = 2

kalkulator = {
    '+': dodawanie,
    '-': odejmowanie,
    '*': mnozenie,
    '/': dzielenie
}

d = '+'
x = 1
y = 2

print(f'{x} {d} {y} = {kalkulator[d](x,y)}')