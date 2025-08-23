def notas(*numeros,situação=False):
    """
notas(*números,situação=False)
    -> Função para analisar notas e situações de vários alunos.
    :param número: uma ou mais notas dos alunos(aceita várias, por conta do desempacotamento)
    :param situação: valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: diciónario com várias informações sobre a situação da turma.
    """
    print('---'*30)
    notas_alunos = {}
    soma_notas = 0
    maior = numeros[0]
    menor = numeros[0]
    for contador in range(1,len(numeros)):
        if numeros[contador] > maior:
            maior = numeros[contador]
        if numeros[contador] < menor:
            menor = numeros[contador]
    for numero in numeros:
        soma_notas += numero
    media = soma_notas / len(numeros)
    notas_alunos['Quantidade de notas '] = len(numeros)
    notas_alunos['Maior nota'] = maior
    notas_alunos['Menor nota'] = menor
    notas_alunos['Média'] = media
    if situação:
        if media >= 7:
            notas_alunos['Situação'] = 'BOA'
        elif 7 > media > 5.5:
            notas_alunos['Situação'] = 'MEDIA'
        else:
            notas_alunos['Situação'] = 'RUIM'
    return notas_alunos


resposta = notas(3.5,2, 6.5,2,7,4,situação=True)
print(resposta)