'''
8. Um polinômio é uma expressão da forma
p(x)=anxⁿ+an-₁xⁿ⁻¹+...+a₂x²+a₁x+a₀
onde an, an-₁, …, a₂, a₁, a₀ são os coeficientes do polinômio com an diferente de zero.
A partir de um conjunto de pontos dados, podemos obter um polinômio interpolador
que passa por estes pontos. A interpolação polinomial, no Python, pode ser feita por
meio da função “lagrange()” da biblioteca científica scipy. Considerando os pontos
A(2, 2), B(6, 1) e C(9, 10), obtenha o respectivo polinômio interpolador de Lagrange.
'''

from scipy.interpolate import*

x = [2, 5, 9]
y = [2, 1, 10]
p = lagrange(x,y)
print('8) ', (p))