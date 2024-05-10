'''
Aula 4 tema 4 -> listas dentro de dicionários
Uma lista contendo, em cada índice, um dicionário.
'''

print('Lista de dicionários')
games = [] # lista games rece dicionários
# dicionários (tem os nomes de dados mas os valores neles são diferentes.)
game1 = {'nome': 'Super Mario',
         'videogame': 'Super Nintendo',
         'ano':1990}
game2 = {'nome': 'Zelda Ocaria of time',
         'videogame': 'Nintendo 64',
         'ano':1998}
game3 = {'nome': 'Pokemon Yellow',
         'videogame': 'Game Boy',
         'ano':1999}
games = [game1, game2, game3]
print(games)

# preenchendo o dicionário através do input
game = {}
games =[]
for i in range(3):
    game['nome']= input('\nQual o nome do jogo? ')
    game['videogame'] = input('Para qual video-game ele foi lançado? ')
    game['ano'] = input('Qual o ano de lançamento? ')
    games.append(game.copy())
print('-' * 20)
for e in games: # 1 for anda na lista
    for i, j in e.items(): # 2 for anda nos dicionários armazenando  chave em i e dados em j
        print('\nO campo {} tem o valor {}:'.format(i,j))
