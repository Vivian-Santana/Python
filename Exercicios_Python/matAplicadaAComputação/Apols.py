# ******** APOL 1 **********
# escreva o decimal 89 na respectiva forma binária

import numpy as np
import pandas as pd

numero= 89
print(f'1. O binário correspondete a 89 é: {bin(numero)[2:]}')

# 2 Qual é a forma hexadecimal associada ao número decimal 12001?
print(f'\n2. O hexadecimal correspondete a 12001 é: {hex(12001)[2:]}')

# 3 Represente o número 12453301 utilizando a notação científica normalizada
num = 12453301
print('\n3. 12453301 é = %.10e' % num)

# 4. Qual é a forma decimal do número binário 110011?
# Defina o número binário
numero_binario = '110011'

# Use a função int() com base 2 para converter de binário para decimal
numero_decimal = int(numero_binario, 2)

# Imprima o resultado
print(f'\n4. O número binário {numero_binario} em decimal é: {numero_decimal}')

# 5. Qual a representação da forma binária referente ao decimal 57?
print(f'\n5. O binário correspondete a 57 é: {bin(57)[2:]}')

# 6 converta o binário 11111011 para a respectiva forma decimal
num_bin = '11111011'
num_dec = int(num_bin, 2)
print(f'\n6. o binário {num_bin} em decimal é: {num_dec}')

'''
 7 determine o valor lógico das proposições P: Se 3⁴= 12 então 2⁰= 2 e Q: ~(3>2).
V(P)= Se F então F e V(Q)= ~V
Resposta V(P)= V e V(Q)= F
'''
# Dado o hexadecimal 2A2, escreva-o na respectiva forma decimal
# Defina o número hexadecimal
numero_hexadecimal = '2A2'

# 8 Use a função int() com base 16 para converter de hexadecimal para decimal
numero_decimal = int(numero_hexadecimal, 16)

# Imprima o resultado
print(f'\n8. O número hexadecimal {numero_hexadecimal} em decimal é: {numero_decimal}')

'''
 9 Considerando as proposições p, q e r onde V(p)= V, V(q)= F e V(r)= F obtenha o valor lógico das proposições P: p+q e Q: (p.r)'
Resp V(p)= V e V (Q)= V
'''
#10 Calcule a= 8,151521x10⁵ + b= 2,456732x 10³
a= 8.151521e+05
b= 2.456732e+03
c= a+b
print('\n10) 8,151521x10⁵ + b= 2,456732x 10³ = %.8e'%c)
# ******** APOL 1 **********

# ******** APOL 2 **********
print('\n','-'*25,"Apol 2",'-'*25)
'''
1 Um relógio analítico está marcando 10h e um evento está agendado para começar daqui a 17h, 
que horas o relógio estará marcando no início deste evento?
'''
print('\n1. ',(10+17)%12, 'horas')

# 2 Obtenha o polinômio que interpola os pontos A(0,2), B(3,-4),C(5,1) e D(7,6)

from scipy.interpolate import*
x= [0, 3, 5, 7]
y= [2, -4, 1, 6]
p= lagrange(x,y)
print('\n2.',p)

# 3 Obter a mediana das notas de 0 a 10 obtidas de 12 estudantes
# 8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5
n = {'Dados':[8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]}
d = pd.DataFrame(n)
mediana = d['Dados'].median()
print(f'\n3. Mediana das notas:{mediana}')

# 9 calcule o desvio padrão das notas dos alunos
desvio_padrao= d['Dados'].std()
print(f'\n9. Desvio padrão das notas dos alunos: {desvio_padrao}')

# 10 Calcule a média das notas dos alunos

media= d['Dados'].mean()
print(f'\n10. Média: {media}')

'''
4 Um equipamento tem vida útil de 12.000h com desvio padrão de 800h.
Qual é aprobabilidade de que um destes equipamentos, selecionado ao acaso,
tenha vida útil entre 10.000 e 12.000 horas?
'''
import scipy.stats

media1= 12000
desvio_p= 800
x1 = 10000
p = 0.5-scipy.stats.norm(media1,desvio_p).cdf(x1)
print('\n4. ', p)

'''
5 Os componentes dos seguites vetores estão associados aos gastos com energia elétrica(vetor u)
e com água (vetor v) nos seis primeiros semestres do ano.

u = (134.10, 112.87, 146.02, 151.19, 147.08, 136.32)
V = (89.10, 78.50, 94.09, 101.44, 89.99, 90.04)
Obtenha o vetor u+v que contém a soma dos gastos com energia elétrica e com água nestes meses.
'''
u=np.array([[134.10, 112.87, 146.02, 151.19, 147.08, 136.32]])
v =np.array([[89.10, 78.50, 94.09, 101.44, 89.99, 90.04]])
w=u+v
print('\n5.', w)

# 6 Considerando os vetores u=(4, 7, 0, -8) e v=(9, 17, -12, 21) obtenha o vetor u.v

vetor_u = np.array([[4, 7, 0, -8]])
vetor_v = np.array([[9, 17, -12, 21]])
resultado6 = np.inner(vetor_u, vetor_v)
print('\n6. apol)')
print(resultado6)

# 7 Utilizando a cifra de César, qual é a forma criptogradada associada à palavra "FUTEBOL"?
from string import ascii_uppercase

a= list(ascii_uppercase)
m= input('\n7. Digite a mensagem: ')
m= m.upper()
mc= ""
for l in m:
 i=ord(l)-65
 if l in a:
   mc += a[(i+3)%26]
else:
 l
print(f'Mensagem criptografada: {mc}')

# 8 Utilizando a cifra de César qual é a palavra original associada à forma criptografada "FRPSXWDGRU"?
a= list(ascii_uppercase)
mc= input('\n8 Digite a mensagem criptografada: ')
mc= mc.upper()
m= ""
for l in mc:
 i=ord(l)-65
 if l in a:
   m+=a[(i-3)%26] # diferença da codificação p a decodificação
else:
 l
print(f'Mensagem original: {m}')

# ******** APOL 2 **********
