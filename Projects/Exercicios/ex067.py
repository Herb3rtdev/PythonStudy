
while True:
    contador = 1
    n = int(input('Digite um numero:'))
    if n >= 0:
        while contador <= 10:
            print(f'{n} x {contador} = {n * contador}')
            contador += 1
    else:
        break
print('PROGRAMA FINALIZADO!')





