import math
n1 = int(input('Digite o 1.o numero:'))
n2 = int(input('Digite o 2.o numero:'))
n3 = int(input('Digite o 3.o numero:'))
l= [n1,n2,n3]
numero = min(l)
num = max(l)
print(numero)
print(num)

#guanabara resolucao
n1 = int(input('Digite o 1.o numero:'))
n2 = int(input('Digite o 2.o numero:'))
n3 = int(input('Digite o 3.o numero:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(menor)
print (maior)