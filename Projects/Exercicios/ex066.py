
soma = 0
quantidade = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    soma += n
    quantidade += 1
print(f'A soma dos numeros é {soma} e a quantidade de numeros somados é {quantidade}')
