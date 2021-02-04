codigo = int (input('Digite o código: '))
quantidade = int(input("Digite a quantidade: "))


if codigo == 1:
    valor = 4*quantidade
    
if codigo == 2:
    valor = 4.5*quantidade

if codigo == 3:
    valor = 5*quantidade

if codigo == 4:
    valor = 2*quantidade

if codigo == 5:
    valor = 1.5*quantidade

print(f' Total: R$ {valor}')