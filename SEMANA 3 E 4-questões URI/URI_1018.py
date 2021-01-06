valor=int(input(''))

valor1 = valor//100
resto1 = valor%100

valor2 = resto1//50
resto2 = resto1%50

valor3 = resto2//20
resto3 = resto2%20

valor4 = resto3//10
resto4 = resto3%10

valor5 = resto4//5
resto5 = resto4%5

valor6 = resto5//2
resto6 = resto5%2

valor7 = resto6//1
resto7 = resto6%1


print(valor)
print('{} nota(s) de R$ 100,00'.format(valor1))
print('{} nota(s) de R$ 50,00'.format(valor2))
print('{} nota(s) de R$ 20,00'.format(valor3))
print('{} nota(s) de R$ 10,00'.format(valor4))
print('{} nota(s) de R$ 5,00'.format(valor5))
print('{} nota(s) de R$ 2,00'.format(valor6))
print('{} nota(s) de R$ 1,00'.format(valor7))
