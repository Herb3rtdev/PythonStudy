print('Os numeros pares são:')
for c in range(0,51):
    if c % 2 == 0:
        print(c, end='-')

#guanabara dá menos trabalho para a maquina dessa forma
print('')
for d in range(0,51,2):
    print(d, end=' ')