a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

perímetro = a+b+c


if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perímetro = {perímetro}')

else:
    area=((a+b)*c)/2
    print(f'Area = {area}')