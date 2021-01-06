valores= input('').split(' ')


a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maiorab= (a + b + abs (a-b))/2

maior = (c + maiorab + abs (c-maiorab))/2

print('{:.0f} eh o maior'.format(maior))
