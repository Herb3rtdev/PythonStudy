from time import sleep


def maior(*list):
    print('-='*15)
    vmaior = 0
    #O for foi usado para tanto declarar os valores da tupla quanto para saber a posicao para assim declarar o maior
    for valor in range(0,len(list)):
        print(list[valor],end=' ')
        if valor == 0:
            vmaior = list[0]
        else:
            if list[valor] > vmaior:
                vmaior = list[valor]
    sleep(0.5)
    print(f'Foram informados {len(list)} valores ao todo.')
    print(f'O maior valor informado foi {vmaior}')
    

#Programa Principal 
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()