salario = float(input('SALARIO ATUAL:'))

if salario >0 and salario <=400:
    reajuste = salario*0.15
    novo = salario + reajuste
    percentual = "15%"
    

if salario >400 and salario <=800:
    reajuste = salario*0.12
    novo = salario + reajuste
    percentual = "12%"

if salario >800 and salario <=1200:
    reajuste = salario*0.1
    novo = salario + reajuste
    percentual ="10%"

if salario >1200 and salario <=2000:
    reajuste = salario*0.07
    novo = salario + reajuste
    percentual = "7%"

if salario >2000 :
    reajuste = salario*0.04
    novo = salario + reajuste
    percentual = "4%"

print(f' Novo salário: {novo}\nReajuste = {reajuste}\nEm percentual = {percentual}')