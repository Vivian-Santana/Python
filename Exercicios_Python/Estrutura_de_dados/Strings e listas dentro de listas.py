'''
aula 6 tema 3
Dupla indexação
o primeiro índice é referente a cada item da lista
o segundo índice é referente a cada caractere da string
Assim, podemos acessar não só cada dado dentro da lista, 
mas também cada carctere das strings de um índice da lista.
'''

print('Retorna o item passado como parâmetro:')
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

print('\nRetorna o índice 0 e dentro dele o caractere na posição 0:')
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0])
print(mochila[2][1]) # retorna a letra A

print('\nVarredura da lista caracter por carcter:')
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila: # 1° laço anda na lista
    for letra in item: # 2° laço anda nos caracteres
        print(letra, end='') # imprime tds os caracteres (end='' - para não pular as linhas do print).
        print()

print('\nmaneiras alternativas de medir as listas')
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1): # tam. da lista
    for j in range(0,len(mochila[i]),1): # tam da string
        print(mochila[i][j],end='')
        print()
