'''
Escreva um algoritmo que crie uma tupla com 10 palavras.
Encontre dentro dessa tupla as vogais de cada palavra.
Faça um print na tela com o nome da palavra e suas respectivas
vogais.
'''

palavras = ('Programação', 'Algoritmos', 'Lógica', 'Sistemas','Python', 'Java', 'Alan', 'Turing', 'Ada', 'Lovelace')
print(palavras)

# Função para encontrar as vogais em uma palavra
def encontrar_vogais(palavra):
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    return vogais

# Iteração sobre as palavras na tupla
for palavra in palavras:
    vogais_palavra = encontrar_vogais(palavra)
    print("Palavra:", palavra)
    print("Vogais:", vogais_palavra)
    print()

'''
O algoritmo percorre cada palavra da tupla, chama a função encontrar_vogais() 
para encontrar as vogais em cada palavra e, em seguida, imprime o nome da 
palavra e suas respectivas vogais.
'''

# jeito do professor
for palavra in palavras:
    print('\nPalavra:{} --> vogais:'.format(palavra.upper()), end=' ')
    for letra in palavra:
        if letra.lower()in 'aeiou':
            print(letra.upper(), end=' ')