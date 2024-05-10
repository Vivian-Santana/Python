# exemplo de polinômio intepolador
'''
No Python, podemos utilizar a função “lagrange()” da biblioteca científica
scipy para obtermos um polinômio que interpola um conjunto de pontos.
Utilizaremos a sequência de comandos:
from scipy.interpolate import *
x=[]
y=[]
p=lagrange(x, y)
print(p)
bastando atribuir os valores de x com os respectivos valores de y
relacionados aos dados do problema.

Por exemplo, se quisermos o polinômio que interpola os pontos A(4, 2),
B(7, -1), C(10, 12) e D(11,15), basta considerarmos os valores de x de cada
ponto, ou seja, x=[4, 7, 10, 11]. Precisamos também dos respectivos valores
y=[2, -1, 12, 15]. Utilizando os comandos
'''
'''
from scipy.interpolate import *
x=[4, 7, 10, 11]
y=[2, -1, 12, 15]
p=lagrange(x, y) # função lagrange associada a x e y
print(p)
# o polinômio interpolador é p(x)=-0,1746x³+4,556x²-34,87x+79,78
'''

'''
Exemplo de aplicação em um problema

A concentração média de partículas por
milhão (ppm) de um certo poluente em uma determinada região está se alterando
com o passar do tempo e que os dados obtidos durante 4 anos foram

Ano             1       2       3       4
Concentração    80      95      110     122

podemos obter o polinômio que interpola estes dados. Para isto,
precisamos dos valores 1, 2, 3 e 4 associados a x e os respectivos valores 80,
95, 110 e 122 associados a y.

from scipy.interpolate import *
x=[1, 2, 3, 4]
y=[80, 95, 110, 122]
p=lagrange(x, y)
print(p)

# O polinômio interpolador obtido é p(x)=-0,5x³+3x²+9,5x+68.

from scipy.interpolate import *
x=[0, 3, 5, 7]
y=[2, -4, 1, 6]
p=lagrange(x, y) # função lagrange associada a x e y
print(p)
'''
'''
ATIVIDADE PRÁTICA QUESTÃO 14
Por exemplo, se quisermos o polinômio que interpola os pontos A(0, 6),
B(5, 2) e C(8, 15), basta considerarmos os valores de x de cada
ponto, ou seja, x=[4, 7, 10, 11]. Precisamos também dos respectivos valores
y=[2, -1, 12, 15]. Utilizando os comandos
'''
''''''
from scipy.interpolate import *
x=[0, 5, 8]
y=[6, 2, 15]
p=lagrange(x, y) # função lagrange associada a x e y
print(p)