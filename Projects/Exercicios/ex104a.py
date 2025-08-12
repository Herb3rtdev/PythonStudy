def leiaInteiro(mensagem):
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        if ok:
            break
    return valor



n = leiaInteiro('Digite um numero: ')
print(f'Voce digitou o numero inteiro {n}')