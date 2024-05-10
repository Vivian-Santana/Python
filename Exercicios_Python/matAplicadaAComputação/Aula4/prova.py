'''
13. Uma empresa produz carregadores para um determinado modelo de telefone
celular e precisa obter a função que relaciona o lucro mensal com o preço de venda
dos carregadores. Os custos fixos mensais da empresa correspondem a R$
5000,00. Para um preço de venda de R$ 15,00 por unidade, o lucro mensal
corresponde a R$ 30.000,00. Quando cada carregador é vendido por R$ 17,00, o
lucro mensal é de R$ 28.00,00. Obtenha o polinômio interpolador que relaciona o
lucro y com o preço de venda x.
'''
import numpy as np
from scipy.interpolate import *

x=[0, 15, 17] # primeiro valor é 0 pq está associado ao custo fixo mensal sem venda, então venda = 0.
y=[-50000, 30000, 28000]# 47500 custo valor negativo, lucro  22000, 20450 valor positivo.
p=lagrange(x, y)
print('\n13) {}'.format (p))

'''
Considerando que será realizado um estudo relacionado a 20.000
pessoas e que apenas uma algumas delas fará parte de forma efetiva, qual é o
tamanho da amostra considerando uma margem de erro de 2%?
'''
N=150000
e=0.03
n=N/(1+N*e**2)
print(f'Tamanho da amostra: {n}')

# prova 8 obtenha a soma dos vetores u + v
u = np.array([[4, 7, 0, -8]])
v = np.array([[9, 17, -12, 21]])
w = u+v
print('8- prova: ',w)

#14. Considerando os pontos A(0,2), B(3,-4) e C(5,1) D(7,6), obtenha o respectivo polinômio interpolador dde Lagrange.

from scipy.interpolate import *
x=[0, 3, 5, 7]
y=[2, -4, 1, 6]
p=lagrange(x, y) # função lagrange associada a x e y
print('\n10-prova.',p)