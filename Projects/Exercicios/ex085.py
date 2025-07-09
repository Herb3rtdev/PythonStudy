numeros = []
pares = []
impares = []
for numero in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
numeros.append((sorted(pares[:])))
numeros.append((sorted(impares[:])))
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')



