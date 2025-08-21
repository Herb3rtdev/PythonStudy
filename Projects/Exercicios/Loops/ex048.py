s = 0
f = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        f += 1
print('A soma dos {} numeros ímpares multiplos de 3 é {}'.format(f,s))
