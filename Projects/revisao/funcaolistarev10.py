def lista():
    #cadastra o peso e o nome das pessoas
    temporaria = []
    principal = []
    while True:
        temporaria.append(str(input('Nome: ')))
        temporaria.append(float(input('Peso KG: ')))
        principal.append(temporaria[:])#coloca uma lista dentro da outra[[nome,peso][nome1,peso1]]
        temporaria.clear()#Apaga a lista anterior 
        resp = str(input('Voce quer continuar? [S/N]'))
        if resp in 'Nn':
            break
    return principal


def maior_menor():
    pessoas = lista()
    print('-=-'*15)
    print(f'A quantidade de pessoas cadastradas foi {len(pessoas)} pessoas')
    maior = pessoas[0][1]
    menor = pessoas[0][1]


    #Verifica o maior e o menor peso 
    for contador in range(0,len(pessoas)):
        if pessoas[contador][1] > maior:
           maior = pessoas[contador][1]
        if pessoas[contador][1] < menor:
            menor = pessoas[contador][1]
    print(f'O maior peso foi de {maior:.2f} KG. Os mais pesados são ',end='')

    #Caso tenha repetiçao de peso, o programa vai imprimir mais de um nome
    
    #Vai verificar que são as pessoas que tem o maior peso
    for valor in pessoas:
        if valor[1] == maior:
            print(valor[0],end=' ')
    print(f'\nO menor peso foi de {menor:.2f} KG. Os mais leves são ',end='')
    
    #Vai verificar que são as pessoas que tem o menor peso
    for valor in pessoas:
        if valor[1] == menor:
            print(valor[0],end=' ')
    
        





#programa principal
maior_menor()
    