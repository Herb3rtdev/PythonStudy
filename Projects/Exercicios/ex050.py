s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}.o numero: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos números pares é {} e a quantidade de numeros pares é {}'.format(s, cont))