nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

media = ((nota1*2) + (nota2*3) + (nota3*4) + nota4)/10

if media>=7:
    print(f' MÉDIA:{media:.1f}')
    print(f' ALUNO APROVADO:')

if media<5:
    print(f' MÉDIA: {media:1f}')
    print(f' ALUNO REPROVADO')

if media >=5 and media<7:
    print(f' MÉDIA:{media:.1f}')
    print(f' ALUNO EM EXAME:')
    recuperacao = float(input("nota do exame: "))
    mediaf = (media+recuperacao)/2
    print(f' NOTA DO EXAME:{recuperacao:.1f}')
    if mediaf>=5:
        print('ALUNO APROVADO')
        print(f'MÉDIA FINAL: {mediaf:1f}')
    if mediaf<5:
        print('ALUNO REPROVADO')
        print(f'MÉDIA FINAL: {mediaf:.1f}')