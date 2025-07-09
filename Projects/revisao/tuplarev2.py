numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    numero = int(input('Digite um numero: '))
    if  0 <= numero <= 20:
        print(f'Voce digitou o numero {numeros[numero]}.')
        break
    else:
        print('Tente novamente.',end='')
print('Programa finalizado.')