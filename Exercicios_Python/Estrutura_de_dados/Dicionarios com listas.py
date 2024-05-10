'''
Aula 4 tema 4 -> dicionários dentro de listas
um dicionário, e dentro dele para cada palavra chave uma lista
'''

games = {'nome':['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yeallow'],
         'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'],
         'ano': [1990, 1998, 1999]}
print(games)
# saída
# palavra chave | lista |                                                palavra chave | lista                                      palavra chave | lista
# {'nome': ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yeallow'], 'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'], 'ano': [1990, 1998, 1999]}
print('\npreenchendo a lista através do input')
games2 = {'nome':[], 'videogame':[], 'ano':[]}
for i in range(3):
    nome= input('\nQual o nome do jogo? ')
    videogame = input('Para qual video-game ele foi lançado? ')
    ano = input('Qual o ano de lançamento? ')
    games2['nome'].append(nome)
    games2['videogame'].append(videogame)
    games2['ano'].append(ano)
print('-' * 20)
print(games2)