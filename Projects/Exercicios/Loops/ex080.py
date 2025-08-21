valores = []
for contador in range(0,5):
    valor = int(input('Digite um valor: '))
    if contador == 0 or valor > valores[len(valores)-1]:
        valores.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor < valores[posicao]:
                valores.insert(posicao,valor)
                print(f'Valor adicionado na posicao {posicao} na lista')
                break
            posicao += 1
print(f'A lista em ordem crescente:{valores}')