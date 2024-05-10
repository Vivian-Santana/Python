'''
7. Uma função da forma
y=ax²+bx+c
onde “a”, “b” e “c” são constantes e “a” é diferente de zero é conhecida como função
quadrática e o respectivo gráfico é uma parábola. As coordenadas do vértice desta
parábola são dadas por
𝑥𝑣 = −𝑏 / 2𝑎    e   𝑦𝑣 = −Δ / 4𝑎 onde Δ = 𝑏²− 4𝑎𝑐

Considerando a função quadrática
y=-4x²+1200x-100
calcule por meio do Python Xv e Yv

a = -4
b = 1200
c = -100
xv = -b / (2*a)
delta = b **2-4 * a * c
yv = -delta / (4*a)
print('7) xv ',(xv), end= '')
print('\tyv ', (yv))
'''
'''
ativ q 7
Considerando a função quadrática
y=10x² -150x +300
calcule por meio do Python Xv e Yv

a = 10
b = -150
c = 300
xv = -b / (2*a)
delta = b **2-4 * a * c
yv = -delta / (4*a)
print('7) xv ',(xv), end= '')
print('\tyv ', (yv))
'''
# ou
a = 10
b = -150
c = 300

Xv = -b / (2 * a)
Yv = a * (Xv ** 2) + b * Xv + c

print("Xv =", Xv)
print("Yv =", Yv)