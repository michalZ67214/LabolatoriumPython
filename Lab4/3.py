zwierzeta = []

n = int(input('Ile chcesz dodać zwierząt do listy: '))

for i in range(n):
    zwierzeta.append(input('Zwierze nr '+ str(i+1) + ': '))

zwierzeta.sort()

print(zwierzeta[0], zwierzeta[-3:])