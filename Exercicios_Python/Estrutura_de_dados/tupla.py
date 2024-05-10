'''
aula 6 tema 1
A tupla é uma estrutura de dados estática, imutável.
Representada em python por parenteses()
'''

#tupla é o equivalente a vetor em java
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)
# maneiras de acessar os dados na tupla
print(mochila[0]) # print do elemeto 1 - índice 0
print(mochila[2]) # print do elemento 3 - indice 2
print(mochila[0:2]) # print dos elementos 0 eté 2 (mas o 2 não sai) - Índice 0 e 1
print(mochila[2:]) # print dos elementos a parti do índice 2
print(mochila[-1]) # print do ultimo

print('------------------------------------')
# mochila[2] = 'ovos'  essa atribuição dá erro pq tuplas são imutáveis

# varredura dos itens na tupla
for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

print('------------------------------------')
# varredura com o range
tam =len(mochila)
for i in range (0, tam, 1):
    print('Na minha mochiça tem: {}'.format(mochila[i]))

print('------------------------------------\n'+
      'upgrade da mochila')
# upgrade na tupla (união de duas tuplas)
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

print('------------------------------------\n'+
      'mochila invertida')
mochila_grande_invertida = upgrade + mochila # a ordem dos fatores altera a saída
print(mochila_grande)
print(mochila_grande_invertida)

print('------------------------------------')
# desmpacotamento de funções: passar diversos parâmetros numa função
def soma(* num): # * signfica desmpacotamento: pega tds os dados que vieram como parametro armazena na variável num,
    soma = 0
    print('Tupla: {}'.format(num)) # a variável num será uma tupla que será manipulada e somada dentro da função. 
    for i in num: 
        soma += i
    return soma
# programa principal (chamada da função soma)
print('Resultado: {}\n'.format(soma(1,2))) # 1 e 2 entram na variável num e se tornar uma tupla, faz a soma e vai retonar o resultado final
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))
