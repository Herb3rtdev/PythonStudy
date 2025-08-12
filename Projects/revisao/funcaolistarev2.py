def adicionando_valores():
    valores = []
    while True:
        valor = int(input('Digite um valor: '))
        if valor not in valores:
            valores.append(valor)
            print('Valor adicionado com sucesso')
        else:
            print('Valor duplicado! Não pode ser adicionado...')
        resp = str(input('Voce quer continuar? [S/N]'))
        if resp in 'Nn':
            break
    print(sorted(valores))


#Programa principal
adicionando_valores()