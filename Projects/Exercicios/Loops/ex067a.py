while True:
    n = int(input('Digite um numero para fazer a tabuada:'))
    if n < 0:
        break
    print('--' * 15)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('--' * 15)
print('PROGRAMA TABUADA encerrado!')