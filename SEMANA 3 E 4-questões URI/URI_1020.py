idade = int(input(''))

ano = idade//356
resto1 = idade%365

mes = resto1//30
resto2 = resto1%30



print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(ano,mes,resto2))
