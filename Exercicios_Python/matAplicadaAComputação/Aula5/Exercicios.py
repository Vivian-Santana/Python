'''
4. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Por meio do Python, obtenha a média, a moda e a mediana dos dados
'''

import pandas as pd
print('4)')
duracao= {'Minutos':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}

p= pd.DataFrame(duracao)
media= p['Minutos'].mean()
moda= p['Minutos'].mode()
mediana= p['Minutos'].median()
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')

'''
6. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Obtenha o desvio padrão por meio do Python.
'''
print('\n6)')
x= {'Minutos':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}
m= pd.DataFrame(x)
desvio_padrao= m['Minutos'].std()
print(f'Desvio padrão:{desvio_padrao}')

'''
10. Utilizando a fórmula de Slovin e o Python, qual é o tamanho da amostra
referente a uma população de 200.000 dados considerando uma margem de erro de
4%?

A fórmula de Slovin é usada para calcular o tamanho da amostra necessário para 
obter uma estimativa confiável da população, levando em consideração uma margem 
de erro desejada. A fórmula é dada por: n = N/(1+N*e² ) onde:
n é o tamanho da amostra
N é o tamanho da população
e é a margem de erro (em forma decimal)
Dado que a população 
N é 200.000 
e a margem de erro e é 0,04 (4% em forma decimal)
, essa fórmula é usada para calcular o tamanho da amostra necessário.
'''
from numpy import ceil

print('\n10)')
N = 200000  # Tamanho da população
e = 0.04  # Margem de erro
n = ceil (N / (1 + N * e ** 2)) # ceil faz o arredondamento para o próximo num. inteiro
print(f"Tamanho da amostra necessário: {n:.0f}")