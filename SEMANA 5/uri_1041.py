x = float(input('eixo x: '))
y = float(input('eixo y: '))

if x==0 and y==0:
    print('origem')

if x>0 and y>0:
    print('Q1')

if x<0 and y>0:
    print('Q2')

if x<0 and y<0:
    print('Q3')

if x>0 and y<0:
    print('Q4')