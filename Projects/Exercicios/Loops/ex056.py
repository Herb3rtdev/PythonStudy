soma_idade = 0
idademaisvelho = 0
nomemaisvelho = ''
maisnovo = ''
idademaisnovo = 0
totmulher = 0
for c in range(1, 5):
    print('----{}.o PESSOA----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
        idademaisnovo = idade
        maisnovo = nome
    if sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
        idademaisnovo = idade
        maisnovo = nome
    elif sexo in 'Mm' and idade < idademaisnovo:
        idademaisnovo = idade
        maisnovo = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma_idade / 4
print('A media do grupo é {}'.format(media))
print('O homem mais velho do grupo é {} e tem {} anos. '.format(nomemaisvelho,idademaisvelho))
print('O homem mais novo do grupo é {} e tem {} anos.'.format(maisnovo,idademaisnovo))
print('A quantidade de mulheres abaixo dos 20 anos é {}'.format(totmulher))
