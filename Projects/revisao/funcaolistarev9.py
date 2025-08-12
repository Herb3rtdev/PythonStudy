def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    #Vai armazenar as posicoes do maior numero e do menor
    pos_maior = []
    pos_menor = []
    #Verifica qual é o maior e o menor numero
    for pos,v in enumerate(lista):
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    #Verifica qual é a posiçao do maior e menor. Caso apareceça em mais de uma opção, o programa vai mostrar tambem.
    for i in range(len(lista)):
        if lista[i] == maior:
            pos_maior.append(i)
        if lista[i] == menor:
            pos_menor.append(i)
    #Exibe os resultados
    return f'O maior valor digitado foi {maior} e a posiçao foi {pos_maior}\nO menor valor digitado foi {menor} e a sua posicao foi {pos_menor}'     


#Programa principal
numeros = []
for c in range(0,5):
    n = int(input(f'Digite um valor para a posição {c+1}:'))
    numeros.append(n)
print(f'Voce digitou os valores: {numeros}')
print(maior_menor(numeros))