def medidor_de_letras(palavras):
    print(f'Esse nome tem um total de {len(palavras)} letras ')
    print('-'*len(palavras))
    print(palavras)
    print('-'*len(palavras))



palavra = str(input('Digite uma palavra:'))
medidor_de_letras(palavra)