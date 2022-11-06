def a(x):
    if x > 0:
        return 'a) ' + str(2*x)
    elif x == 0:
        return 'a) 0'
    else:
        return 'a) ' + str(x*-3)

def b(x):
    if x >= 1:
        return 'b) ' + str(pow(x, 2))
    elif x < 1:
        return 'b) ' + str(x)

def c(x):
    if x > 2:
        return 'c) ' + str(2 + x)
    elif x == 2:
        return 'c) 8'
    else:
        return 'c) ' + str(x - 4)


x = float(input('Podaj wartość rzeczywistą: '))
print(a(x))
print(b(x))
print(c(x))