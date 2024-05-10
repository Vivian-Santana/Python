'''
se a função quadrática que relaciona o lucro mensal de um
determinado estacionamento com o preço cobrado por hora é
L(x)=-340x2+5700x-9500
onde x é o preço cobrado por hora e L é o lucro mensal, podemos fazer o
gráfico da função. Podemos também saber qual é o preço que maximiza o lucro
e o saber qual é o respectivo lucro máximo.
Para o gráfico da função, basta fazermos
'''
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0, 16, 100)
y=-340*x**2+5700*x-9500
plt.plot(x,y)
plt.show()

# Como o preço que maximiza o lucro corresponde ao valor de Xⅴ, temos:
a=-340
b=5700
xv=-b/(2*a)
print("Preço (valor de x):" f'{xv:.2f}')

'''
Logo, o preço ótimo é R$ 8,38.
O lucro máximo pode ser obtido por meio da substituição de xv na função
L(x)=-340x2+5700x-9500 ou por meio da fórmula 𝑦𝑣 = −𝛥/4𝑎 onde 𝛥 = 𝑏² − 4𝑎𝑐.
Utilizando a fórmula, temos:
'''
a=-340
b=5700
c=-9500
delta=b**2-4*a*c
yv=-delta/(4*a)
print('Lucro máximo:' f'{yv:.11f}') #o lucro máximo corresponde a R$ 14.389,71.

