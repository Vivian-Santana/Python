'''
Vamos considerar uma indústria que produz teclados para um determinado modelo de notebook. 
Sabendo que o custo unitário de produção corresponde a R$ 28,00 e que mensalmente x unidades 
são produzidas, podemos expressar o custo mensal de produção C em função da quantidade de 
teclados produzidos. Como o custo unitário corresponde a R$ 28,00 e a quantidade mensal 
produzida é x, precisamos multiplicar o custo unitário (28 reais) pela quantidade produzida 
(x unidades). Logo, a função que relaciona o custo mensal com a quantidade de teclados é
C(x)=28x.
'''

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0, 10, 100)
y=28*x
plt.plot(x,y)
plt.show()

# Supondo que a produção em um determinado mês foi de 2344 unidades,
# podemos calcular o respectivo custo fazendo
x=2344
y=28*x
print('Custo mensal:', y)