inicio = int(input('inicio do jogo: '))
fim = int(input('fim do jogo: '))

duracao = fim- inicio
duracao2 = (24-inicio)+fim

if fim>inicio:
    print(f' O JOGO DUROU {duracao} HORAS')

if inicio > fim:
    print(f' O JOGO DUROU {duracao2} HORAS')

if inicio==0 and fim==0:
    print(f' O JOGO DUROU 24 HORAS')