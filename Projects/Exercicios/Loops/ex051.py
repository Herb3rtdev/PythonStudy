print('PROGRESSÃO ARITMÉTICA')
primeiroT = int(input('Primeiro termo PA:'))
razao = int(input('Qual é a razao da PA:'))
for c in range(0,10):
   ultimoT = primeiroT + (razao * c)
   print(ultimoT, end=(' -> '))
print('Finish')
#guanabara
p1 = int(input('1.o termo:'))
r  = int(input('Razao:'))
decimo = p1 + (9 * r)
for c in range(p1,decimo + r, r):
   print(c, end=(' ->'))
   print('Its over')
