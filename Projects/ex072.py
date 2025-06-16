
numero = ('zero','um','dois','tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis', 'dezessete', 'dezoito','dezenove','vinte')
while True:
    while True:
        escolha = int(input('Digite um numero entre 0 e 20:')) 
        if 0 <= escolha <= 20:
            break
        print('Não entendi.', end='')
    print(numero[escolha])
    resp = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print('Programa finalizado!')
