def impar_par(numeros):
    pares = []
    impar = []
    #Verifica se o numero é impar ou par. Se for par adiciona em uma lista par e se for impar em uma lista impar 
    for valor in numeros:
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impar.append(valor)
    return pares, impar #Retorna as listas dos numeros impares e pares


#programa principal
numeros = []
for contador in range(0,7):
    valor = int(input(f'Digite o {contador+1}o. valor: '))
    numeros.append(valor)
pares, impar = impar_par(numeros) #Como eu quero retornar duas variáveis da funcao.Eu declarei duas variáveis no programa principal tambem.
print(f'Números pares: {pares}')
print(f'Números ímpares: {impar}')