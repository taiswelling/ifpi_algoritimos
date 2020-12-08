peça1 = input('').split(' ')
peça2 = input('').split(' ')

a = int(peça1[0])
b = int(peça1[1])
c = float(peça1[2])

d = int(peça2[0])
e = int(peça2[1])
f = float(peça2[2])

total = (b*c) + (e*f)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
