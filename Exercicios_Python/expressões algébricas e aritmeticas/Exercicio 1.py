'''
Desenvolva um algoritmo que solicite ao usuário o preço de um produto 
e um percentual de desconto a ser aplicado a ele. Calcule e exiba o Valor 
do desconto e o preço final do produto (exercício da apolstila - aula 2)
'''

preco = float(input('Digite o preço do produto: ')) # convertendo string em float
percentual = float(input('Digite o percentual de desconto (0 - 100) %: '))

desconto = preco * (percentual / 100)
preco_final = preco - desconto

print('O preço do produto: {}.\n Desconto: {}%' .format(preco, percentual))
print('Valor calculado de desconto: {}\n Valor final do produto: {}' .format(desconto, preco_final))
