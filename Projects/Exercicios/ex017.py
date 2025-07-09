from math import sqrt,pow,hypot
CatetoO = float(input('Digite o valor do cateto oposto:'))
CatetoA = float(input('Digite o valor do cateto adjacente:'))
Hipo = sqrt(pow(CatetoO,2) + pow(CatetoA,2))
print('O triangulo tem cateto adjacente de valor {},oposto de valor {} e hipotenusa de valor {:.2f}'.format(CatetoO,CatetoA,Hipo))

co = float(input('Digite o comprimento do CO: '))
ca = float(input('Digite o comprimento de CA: '))
hi = hypot(co,ca)
print('Hipotenusa vale {}'.format(hi))
