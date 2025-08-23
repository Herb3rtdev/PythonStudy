def ficha(nome='',gols=''):
    """
    :param nome: Vai passar para a função um nome, caso não passe um nome o padrão vai ser <desconhecido>
    :param gols: Vai passar para a função o número de gols, caso não passe nenhum valor o padrão vai ser 0
    :return: Vai retornar a frase com o nome e o número de gols. 
    """
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gols(s) campeonato.'


#Programa principal
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
print(ficha(nome,gols))