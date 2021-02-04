inicio = int(input('A que horas iniciou o jogo?\n'))
minutoi =int(input('E quantos minutos?\n'))
fim =int(input('A que horas finalizou o jogo?\n'))
minutof = int(input('E quantos minutos?\n'))

duracao = fim- inicio
minuto1= minutof-minutoi
duracao2 = (24-inicio)+fim
minuto2 =(60-minutoi)+minutof

if fim>inicio:
    if minutof>minutoi:
        print(f' O JOGO DUROU {duracao} HORAS E {minuto1} MINUTOS')
    if minutoi>minutof:
        print(f' O JOGO DUROU {duracao} HORAS E {minuto2} MINUTOS')

if inicio > fim:
    if minutof>minutoi:
        print(f' O JOGO DUROU {duracao2} HORAS E {minuto1} MINUTOS')
    if minutoi>minutof:
        print(f' O JOGO DUROU {duracao2} HORAS E {minuto2} MINUTOS')
    

if inicio==fim:
    if minutof == minutoi:
        print(f' O JOGO DUROU 24 HORAS e 0 MINUTOS')