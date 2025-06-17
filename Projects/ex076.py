lista_produtos = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.5,'Canetas',22.3,'Livro',34.9)
print('--'*15)
print(f'{"LISTA DE PREÇO E PRODUTOS":^30}')
print('--'*15)
for posicao in range(0, len(lista_produtos)):
    if posicao % 2 == 0:
        print(f'{lista_produtos[posicao]:.<20}',end='')
    else:
        print(f'R${lista_produtos[posicao]:<15.2f}')  
print('--'*15)
