palavras = ('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro')
for palavra in palavras:
    print(f'\n Na palavra {palavra} temos ',end='')
    for vogais in palavra:
        if vogais in 'AaEeIiOoUu':
            print(vogais,end=' ')
            
            