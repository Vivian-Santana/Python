'''
aula 6 tema 3
Imagine uma situação na qual você deve realizar o cadastro de uma lista de 
compras em um sistema. Cada produto comprado deverá ser registrado com seu 
nome, quantidade e valor unitário
'''

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:]) # lista item copiada dentro da lista mercado.
    item.clear() # povoa a lista e limpa ela depois para inserir novos dados.
print(mercado)

'''
print('\nOutro jeito')
mercado2 = []
for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = input('Digite a quantidade: ')
    valor = input('Digite o valor: ')
    mercado2.append([nome, qtd, valor])
print(mercado2)
'''

soma = 0
print('Lista de compras: ')
print('-' * 40)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {} '.format(item[0],item[1],item[2],item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 40)
print('Total a ser pago: {}'.format(soma))

'''
saída
[['ovo', 12, 20.0], ['banana', 6, 5.5], ['cafe', 1, 18.0]]
3 listas dentro de uma
cada item com a quantidade e valor dentro do colchete é uma lista.
'''