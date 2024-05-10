'''
MEDIANA
1. Durante determindado dia, uma pessoa realizou de hora em hora medições 
da velocidade de dowload de sua internet por meio de um app e obteve os 
seguintes resultados (Mbps): 
67,8; 78,6; 54,4; 98,6; 99,4; 130,8; 142,6; 161,6; 142,5; 158,4
Neste período, qual foi a mediana?
'''
import pandas as pd

x = {'Velocidade':[67.8, 78.6, 54.4, 98.6, 99.4, 130.8, 142.6, 161.6, 142.5, 158.4]}
d= pd.DataFrame(x)
mediana = d['Velocidade'].median()
print(f'1. Mediana: {mediana}')
'''
Média
9. Durante determindado dia, uma pessoa realizou de hora em hora medições 
da velocidade de dowload de sua internet por meio de um app e obteve os 
seguintes resultados (Mbps): 
67,8; 78,6; 54,4; 98,6; 99,4; 130,8; 142,6; 161,6; 142,5; 158,4
Neste período, qual foi a velocidade média de download, em Mbps?
'''
media = d['Velocidade'].mean()
print(f'\n9. Média = {media}')
'''
DESVIO PADRÃO

13. Durante determindado dia, uma pessoa realizou de hora em hora medições 
da velocidade de dowload de sua internet por meio de um app e obteve os 
seguintes resultados (Mbps): 
67,8; 78,6; 54,4; 98,6; 99,4; 130,8; 142,6; 161,6; 142,5; 158,4
 Obtenha o desvio padrão
'''
desvio_padrao = d['Velocidade'].std()
print(f'\n13. Desvio padrão:{desvio_padrao}')

'''
NOTAÇÃO CIENTÍFICA NORMALIZADA

2 Por meio do Python escreva a representação do número 458189
utilizando notação cientifica normalizada com 8 casas decimais.
'''

a = 458189
print('\n2. notação do numero 458189: %.8e'%a)

'''
PROPOSIÇÕES

3. considerando as proposições simples

p: hj é sábado

q: tenho um compromisso

r: Estou disposto

escreva em linguagem corrente a proposição "p+q"
Resp: p+q = Hj é sab. ou tenho um compromisso
'''

'''
4. Dadas as proposições simples p, q q r onde V(p)= F, V(q)=F e V(r)= V. 
os valores lógicos das proposições compostas "~p+r" e "q+~r" são, respectivamente

V e F
por que 
~p+r:
~F+V
V+V
V
-----
q+~r:
F+~V
F+F
F
'''

'''
ARITMÉTICA MODULAR
5. Se um relógio analógico está marcando 10 horas e um evento está agendado 
para começar daqui a 19h, q horas o relógio estará marcando no inicio deste evento?
Resp. 5h
'''
relogio =(10+19)%12
print('\n5. 🕜⏲️⏰⌚', relogio)

'''
NOTAÇÃO CIENTÍFICA NORMALIZADA
6. Escreva a representação do número 0,000345 utilizando a notação cientifica normalizada
com 4 casa decimais.
'''
a1 = 0.000345
print('\n6. notação do numero 0,000345: %.4e'% a1)

'''
Funções
7. Uma função da forma y= ax²+bx+c
fórmula 
Xv = -b/2a
e
Yv = −𝛥/4a onde 𝛥 = 𝑏² - 4ac

considerando a função quadrática y = 10x² - 150X + 300
calcule Xv e Yv
'''
A = 10
B = -150
C =300
xv = -B/(2*A)
delta = B**2-4*A*C
yv = -delta/(4*A)
print('\n7. xv=',xv , ' yv=',yv)

'''
8. Calcule a= 7,0102x10⁵ / b= 2,1233x10³ na notação cientifica normalizada
apresentando o resultado com10 casas decimais.
'''
print()
a2 = 7.0102e+05
b2 = 2.1233e+03
c2 = a2/b2
print('\n8.  7,0102x10⁵ / b= 2,1233x10³ = %.10e'% c2)


# 17. Calcule a= 7,0102X10⁵ - b= 2,1233x10³ obtenha o resultado com 10 casas decimais.

a3= 7.0102e+05
b3= 2.1233e+03
c3 = a3 - b3
print('\n17. 7,0102x10⁵ - b= 2,1233x10³ = %.10e'% c3)

# 18. Calcule  a= 7,0102X10⁵ + b= 2,1233x10³ obtenha o resultado com 10 casas decimais.

a4 = 7.0102e+05
b4 = 2.1233e+03
c4 = a4 + b4
print('\n18. 7,0102x10⁵ + b= 2,1233x10³ = %.10e'% c4)

'''
Dadas as proposições simples p, q q r onde V(p)= F, V(q)=F e V(r)= V. 
os valores lógicos das proposições compostas "~p+r" e "p+q" são, respectivamente
Resp V e V

~p+r:
~F+V
V+V
V
----------
p+q
F+F
F
'''

'''
ERRO RELATIVO
11. Considerando um problema onde o valor exato de uma variável corresponde 
a 0,5672 e o valor aproximado é 0,55. Qual é p erro relativo?
Erro absoluto
𝐸A = |𝑥 − 𝑥̅|.

O erro relativo é dado por
𝐸𝑅 =|𝑥−𝑥̅||𝑥|, 𝑥 ≠ 0.
'''
print('\n11. Erro relativo:', end ='')
print(abs(0.5672-0.55)/abs(0.5672))

'''
ERRO ABSOLUTO
19 Considerando um problema onde o valor exato de uma variável correspondente 
a 0,5672 e o valor aproximado é 0,55. Qual o erro Absoluto?
'''
print('\n19. Erro absoluto:', end ='')
print(abs(0.5672-0.55))

'''
12. Dados os vetores
u = (3,6, -1) e V = (11,14,9) obtenha por meio do python o vetor w = u.v
'''
import numpy as np

u = np.array([[3, 6, -1]])
v = np.array([[11, 14, 9]])
w = np.inner(u,v) # operação conhecido como produto escalar ou produto interno, dá pra usar para calculo de media ponderada.
print('\n12. {}'.format(w))

'''
POLINÔMIO
14. Considerando os pontos A(0,6), B(5,2) e C(8,15), obtenha o respectivo polinômio interpolador dde Lagrange.
'''
from scipy.interpolate import *
x=[0, 5, 8]
y=[6, 2, 15]
p=lagrange(x, y) # função lagrange associada a x e y
print('\n14.',p)

'''
CONVERSÃO DE BASE
15. Converta o decimal 12323 na respectiva forma hexadecimal
'''
print(f'\n15. O hexadecimal correspondete a 12323 é: {hex(12323)[2:]}')

'''
16. Converta o decimal 12323 na respectiva forma binária.
'''
print('\n16 O binário do decimal 12323 é: ', bin(12323)[2:])

'''
20. Considerando um problema onde o valor exato de uma variável correspondente 
a 12456,77 e o valor aproximado é 12450. Qual é  o erro absoluto?
'''
print('\n20. Erro absoluto: ', end ='')
print(abs(12456.77-12450))

#Ou

x1 = 12450
x2 = 12456.77
EA = abs(x2-x1)
print('\n',EA)
