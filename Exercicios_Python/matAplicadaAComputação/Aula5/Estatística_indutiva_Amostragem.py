'''
Considerando que será realizado um estudo relacionado a 20.000
pessoas e que apenas uma algumas delas fará parte de forma efetiva, qual é o
tamanho da amostra considerando uma margem de erro de 2%?
'''
N=20000
e=0.02
n=N/(1+N*e**2)
print(f'Tamanho da amostra: {n}')

# Resultado com aredodndamento
from math import ceil # a função ceil faz o arredondamento para p próximo inteiro

N=20000
e=0.02
n=ceil(N/(1+N*e**2))
print(f'Tamanho da amostra com arredondamento: {n}') 