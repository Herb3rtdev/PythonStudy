def pesquisa_binaria(lista, numero_escolhido):
    baixo = 0
    alto = len(lista) - 1


#Enquanto baixo for menor igual a alto, o programa estara em loop
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        #Se o chute, que é o numero que está no meio da lista for igual ao numero escolhido, o programa retorna com a posicao do numero 
        if chute == numero_escolhido:
            return meio
        #Se o chute for maior que o numero escolhido, irá diminuir um do alto, consequentimente a lista ficara menor
        if chute > numero_escolhido:
            alto = meio - 1
        #Se o chute for maior que o baixo entao será aumentado o baixo em mais um e os numeros que ficaram para atras serao descartados
        else:
            baixo = meio + 1
    return None
    
    
minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista,3))
print(pesquisa_binaria(minha_lista, 7))