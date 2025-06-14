n = s = q = 0
n = int(input('Digite um numero [999 para parar]:'))
while not n == 999:
    s += n
    q += 1
    n = int(input('Digite um numero [999 para parar]:'))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(q,s))
print('FIM')