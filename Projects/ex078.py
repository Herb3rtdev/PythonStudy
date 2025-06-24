maior = menor = 0
valores = []
for contador in range(0,5):
    valores.append(int(input(f'Digite um valor na posicao {contador}: ')))
    if contador == 0:
        maior = menor = valores[contador]
    else:
        if  valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print('-=-'*15)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} e a suas respectivas posicoes sao:',end='')
for posicao,v in enumerate(valores):
    if v == maior:
        print(f'{posicao}',end=' ')
print(f'\nO menor valor digitado foi {menor} e a sua respectivas posicoes sao: ',end='')
for posicao,v in enumerate(valores):
    if v == menor:
        print(f'{posicao}',end=' ')       
          
