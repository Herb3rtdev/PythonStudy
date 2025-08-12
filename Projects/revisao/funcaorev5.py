def colocacao_times():
    times = ('Sao Paulo', 'Palmeiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético','Botafogo','Atletico-pr','Bahia','Fluminense','sport','Vitoria','Curitiba','Avai')
    print(f'Os 5 primeiros times são {times[0:5]}')
    print('-=-'*14)
    print(f'Os 4 últimos são {times[-5:-1]}')
    print('-=-'*14)
    times_ordem = sorted(times)
    print(f'Times em ordem alfabética: {times_ordem}')
    print('-=-'*14)
    print(f'O Chapecoense está na {times.index('Chapecoense')+1}.o posição')


colocacao_times()