l1 = float(input('Qual o tamanho do 1.o lado M:'))
l2 = float(input('Qual o tamanho do 2.o lado M:'))
l3 = float(input('Qual o tamanho do 3.o lado M :'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
       print('Existe um triangulo')
else:
    print('Nao dá para formar um triangulo')
