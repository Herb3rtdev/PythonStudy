def leiaInt(número):
    if número.isnumeric:
        return número


número = input(leiaInt('Digite um número: '))
print(f'Voce acabou de digitar o número {número}')