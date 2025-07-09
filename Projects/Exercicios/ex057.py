sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Nao entendi! Informe novamente seu sexo: [M/F]')).strip().upper()[0]
print('Dado gravado com sucesso! Seu sexo é {}'.format(sexo))