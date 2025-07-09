print('SEQUENCIA DE FIBONACCI')
n = int(input('Termos:'))
contador = 2
c1 = 1
c = 0
print(c,end=' -> ')
print(c1,end=' -> ')
while contador < n :
    c2 = c + c1
    c = c1
    c1 = c2
    contador += 1
    print(c2,end=' -> ')
print('FIM')


