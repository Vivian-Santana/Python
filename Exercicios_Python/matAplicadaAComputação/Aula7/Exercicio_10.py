'''
10. Uma forma de saber o tamanho da amostra por meio do tamanho da população
“N” e a margem de erro “e” aceitável é a fórmula de Slovin
𝑛 = 𝑁 / 1+𝑁𝑒²
É uma fórmula bastante simples e utilizada quando não há informações
relacionadas ao desvio padrão ou a um nível de confiança associado ao estudo. Por
meio da fórmula de Slovin e do Python, obtenha o tamanho da amostra
considerando uma margem de erro de 2% para uma população de 150000 dados.
'''
from math import ceil

N=150000
e=0.02
n=ceil(N/(1+N*e**2))
print(f'\n10) Tamanho da amostra: {n}')
