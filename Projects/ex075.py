quantidade_par = 0
numeros = (int(input('Digite um numero:')),
 int(input('Digite outro numero: ')),
 int(input('Digite mais um numero: ')),
 int(input('Digite o último número: ')))
print(f'Voce digitou os valores {numeros}')
print(f'O numero 9 apareceu {numeros.count(9)}')
if numeros == 3:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
for c in numeros:
    if c % 2 == 0:
        quantidade_par += 1
print(f'A quantidade de valores pares foi {quantidade_par}')
