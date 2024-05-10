'''
Aula 4 tema 4
Dicionário é uma estrutura dinâmica
podemos alterar dados e tamanho
Indexados por chaves (palavras-chave)
Representados em python por chaves {}
'''

print('\nCriando um jogo com duas chaves e dois dados:')
game = {'nome': 'Super Mario', # chave (indexação) antes dos dois pontos :, dado está depois dos dois pontos.
        'desenvolvedora': 'Nintendo',
        'ano': 1990}
print(game)

print('\nChamando um dado através de uma chave:')
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

'''
métodos para manipular dados do dicionário:
values: obtém só os dados
keys: obtém só as chaves
items: obtém o par chave:dado
'''

print('\nprintando os valores')
print(game.values())

print('\nprinta tds os valores de forma mais bonita:')
for i in game.values():
    print(i)

print('\nprintando as chaves')
print(game.keys())

print('\nprinta tds as chaves de forma mais bonita:')
for i in game.keys():
    print(i)

print('\nprinta items (chaves e dados)')
print(game.items)

print('\nprinta tds os items de forma mais bonita:')
for i, j in game.items(): # variável i pega as chaves, variável j pega os dados
    print('{} = {}'.format(i,j))