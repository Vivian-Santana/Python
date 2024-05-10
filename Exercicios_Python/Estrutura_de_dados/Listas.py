'''
aula 6 tema 2
a lista é uma estrutura de dados dinâmica (podemos alterar o tamanho de acordo com a necessidade).
indexadas por valores numéricos inteiros
representada em python por colchetes []
'''

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

# alterando dados da lista
mochila[2] = 'Laranja'
print('Lista: ', mochila)

print('-------------------------------------------------\n'+
      'Manipulando listas')
# variável + função = método
mochila.append('Ovos') # append = sign apêndice (função = método)
print('Lista: ', mochila) # adiciona ovos ao fim da lista

print('---------------------------------------------------------------')
mochila.insert(1,'Canivete') # função insere o dado que eu quero na posição passada como parâmetro.
print('Lista: ', mochila)# adiciona canivete no indice 1 da lista e desloca os outros dados para a direita.

print('---------------------------------------------------------------\n'+
      'removendo dados da lista')
del mochila[1] # del = deletar remove pelo índice (deletou o canivete)
print('Lista: ', mochila)
mochila.remove('Ovos') # remove pelo nome do dado (valor explicito)
print('Lista: ', mochila)

print('---------------------------------------------------------------')
print('lista y e x')
# particularidade da linguagem python
x = [5,7,9,11]
y = x # referência na memória de uma variável a outra (por isso qualquer mudança q eu fizer em x tbm será feita em y)
print(x) # lista x
print(y) # lista y

print('\nalterando a lista y')
y[0] = 2
print(x)
print(y)
print()
# cópia (como fazer duas listas iguais, uma recebendo a outra, alterando uma sem alterar a outra)
print('lista a e b')
a = [1,5,10,21]
b = a [:] # cria duas cópias na memória, assim da pra alterar uma sem alterar a outra.
print(a)
print(b)

print('\nalterando o valor de b')
b[0] = 2
print(a)
print(b)
