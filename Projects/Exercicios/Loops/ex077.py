palavras = ('aprender','programar','python','linguagens','futuro','familia','casamento','casa','cuidado','serviço')
for pos in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[pos].upper()} temos ',end='')               
    for letra in palavras[pos]: 
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
    