l1 = float(input('Digite o valor do 1.o lado:'))
l2 = float(input('Digite o valor do 2.o lado:'))
l3 = float(input('Digite o valor do 3.o lado:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Existe a possibilidade de formar um triangulo.')
    if l1 == l2 == l3:
        print('Esse triangulo é equilátero')
    elif l1 != l2 != l3 != l1:
        print('Esse triangulo é escaleno')
    else:
        print('Esse triangulo será isóceles')
else:
    print('Não tem como formar um triangulo.')





