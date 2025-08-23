def maior(*numeros):
    maior_numero = numeros[0]
    for contador in numeros:
        print(contador,end=' ')
        if maior_numero < contador:
            maior_numero = contador
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}')
    print('-=' * 18)


print('-=' * 18)    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
