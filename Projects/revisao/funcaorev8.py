def contador_vogais(n):
    soma_vogais = 0
    print(f'Na palavra {n} temos: ',end=' ')
    for letras in n:
        if letras in 'AEIOU':
            print(letras,end='...')
            soma_vogais += 1
    return soma_vogais
    

palavra = str(input('Digite uma palavra: ')).upper()
quantidade = contador_vogais(palavra)
print(f'\nUm total de {quantidade} vogais ')



