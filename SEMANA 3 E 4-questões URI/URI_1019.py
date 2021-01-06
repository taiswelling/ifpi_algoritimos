N = int(input(''))

hora= N//3600
resto = N%3600

minutos = resto//60
resto2 = resto%60

print('{}:{}:{}'. format(hora,minutos, resto2))
