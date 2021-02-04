a = int(input('Valor de A: '))
b = int(input('Valor de B:'))

lista = [a,b]
ordem = sorted(lista)

if ordem[1] % ordem[0]==0:
    print('são multiplos')
else:
    print('não são multiplos')