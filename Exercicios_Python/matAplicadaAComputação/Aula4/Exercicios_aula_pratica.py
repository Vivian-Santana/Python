'''
1. Utilize o Python para gerar um conjunto de números inteiros que variam 
de -10 a 20. Em seguida, verifique se o número -1 está neste conjunto.
'''
# Gera um conjunto de números inteiros de -10 a 20
from matplotlib import pyplot as plt
import numpy as np

print('1)')
conjunto_numeros = set(range(-10, 21)) #  a função set() cria um conjunto de números inteiros de -10 a 20.

# Verifica se o número -1 está no conjunto
numero_verificado = -1
if numero_verificado in conjunto_numeros: # o operador in verifica se o número -1 está presente no conjunto.
    print(f"{numero_verificado} está presente no conjunto.")
else:
    print(f"{numero_verificado} não está presente no conjunto.")
#ou
print('-'*35,'ou','-'*35)
C=np.linspace(-10, 20, 31)
print(C)
if -1 in C:
    print('True')
else:
    print('False')
'''
2. Utilize o Python para gerar um conjunto de números inteiros que variam 
de -10 a 20. Em seguida, verifique se o número -11 está neste conjunto.
'''
print('2)')
conj_num = set(range(-10,20))
if -11 in conj_num:
    print('-11 está presente no conjunto.')
else:
    print('-11 não está presente no conjunto.')

'''
3. No conjunto a seguir são apresentados os valores dos salários mínimos de 1995
a 2022 dispostos em ordem cronológica.
S={100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}
Verifique, por meio do Python, se o valor R$ 350,00 está neste conjunto.
'''
print('3)')
S = [100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212]

if 350 in S:
    print('350,00 R$ está presente no conjunto.')
else:
    print('350,00 R$ não está presente no conjunto.')
print()
'''
4. Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012,
323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que
armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário
está ou não neste conjunto para permitir ou proibir a entrada na residência.
print('4)')

senhas = ['452012','323233', '787910', '528917', '683524']

senha = input('🏡Digite a sua senha: ')
if senha in senhas:
    print('Entrada autorizada 🔓')
else:
    print('Entrada não autorizada 🔒')
'''
'''
5. O vetor v contém os preços de venda de algumas mercadorias:
v=(1210, 897, 1230, 1495, 799, 890, 1010)
A loja está com uma promoção onde é dado um desconto de 20% em todas as
mercadorias. Por meio do Python, obtenha o vetor que contém os preços destas
mercadorias com o desconto
'''
v = (1210, 897, 1230, 1495, 799, 890, 1010)

# Calcular o vetor com preços após o desconto de 20%
v_com_desconto = [preco * 0.8 for preco in v]

print("5) Preços com desconto:", v_com_desconto)
# ou 
print('-'*35,'ou','-'*35)
v=np.array([[1210, 897, 1230, 1495, 799, 890, 1010]])
w=0.8*v
print('5){}'.format (w))

# 6. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v.
u = np.array([[3, 4, 8]])
v = np.array([[10, 12, -1]])
z = u+v
print('\n6){}'.format(z))

#7. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v.
a = np.array([[3, 4, 8]])
b = np.array([[10, 12, -1]]) # 8-(-1) = 9
c = a-b
print('\n7) {}'.format(c))
# ou
print('-'*35,'ou','-'*35)
vetor_v = (10, 12, -1)
vetor_u = (3, 4, 8)
# Subtrair vetor v de vetor u elemento a elemento
resultado = [vetor_u[i] - vetor_v[i] for i in range(len(vetor_u))]
print("7) Vetor u - v:", resultado)
print()
'''
 u[i] - v[i] calcula a diferença entre os elementos correspondentes dos vetores u e v. 
 O loop for percorre os índices dos elementos nos vetores (0, 1 e 2) e cria uma nova 
 lista resultado com as diferenças.
'''
# 8. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u.v
d = np.array([[3, 4, 8]])
e = np.array([[10, 12, -1]])
f = np.inner(d,e) # operação conhecido como produto escalar ou produto interno, dá pra usar para calculo de media ponderada.
print('8) {}'.format(f))

'''
9. Considere as matrizes

A   (3   5   9
    4   2  -3
    1   5  -5)
e
B   (12  -6  7
    3   0   2
   -1   10  1)
Utilize o Python para obter a matriz C=A+B.
'''
A = np.array([[3, 5, 9],[4, 2, -3], [1, 5, -5]])
B = np.array([[12, -6, 7],[3, 0, 2], [-1, 10, 1]])
C = A+B
print('\n9) {}'.format(C))

'''
10. Considere as matrizes
A   (3   5   9
    4   2  -3
    1   5  -5)
e
B   (12  -6  7
    3   0   2
   -1   10  1)
Por meio do Python, obtenha a matriz C=A.B.
'''
A1 = np.array([[3, 5, 9],[4, 2, -3], [1, 5, -5]])
B1 = np.array([[12, -6, 7],[3, 0, 2], [-1, 10, 1]])
C1 = np.matmul(A1,B1) # multiplicação das matrizes.
print('\n10) {}'.format(C1))

# 11. Construa o gráfico da função y=x³-2x²+12x-1 no intervalo [-3, 4].
'''
x = np.linspace(-3, 4)
y = x**3 - 2*x**2 + 12*x - 1
plt.plot(x,y)
plt.show()
'''

# 12. Quais são as coordenadas do vértice da função f(x)=-2x2+21x-8?
a1 = -2
b1 = 21
x_vertice = -b1 / (2*a1)
y_vertice = -2 * x_vertice**2 + 21 * x_vertice - 8
print('\n12) x = {}'.format(x_vertice),'\ty = {}'.format(y_vertice))
#ou
'''
print('-'*35,'ou','-'*35)
a=-2
b=21
c=-8
xv=-b/(2*a)
delta=b**2-4*a*c
yv=-delta/(4*a)
print('\n12) x = {}'.format (xv))
print('y = {}'.format (yv))
'''

'''
13. Uma empresa produz carregadores para um determinado modelo de telefone
celular e precisa obter a função que relaciona o lucro mensal com o preço de venda
dos carregadores. Os custos fixos mensais da empresa correspondem a R$
47.500,00. Para um preço de venda de R$ 12,00 por unidade, o lucro mensal
corresponde a R$ 22.000,00. Quando cada carregador é vendido por R$ 20,00, o
lucro mensal é de R$ 20.450,00. Obtenha o polinômio interpolador que relaciona o
lucro y com o preço de venda x.
'''
from scipy.interpolate import *

x=[0, 12, 20] # primeiro valor é 0 pq está associado ao custo fixo mensal sem venda, então venda = 0.
y=[-47500, 22000, 20450]# 47500 custo valor negativo, lucro  22000, 20450 valor positivo.
p=lagrange(x, y)
print('\n13) {}'.format (p))

# 14. Obtenha a soma 7+8 módulo 12.
m = (7+8) % 12
print('\n14) {}'.format(m))

# apol questão 6 multiplicação dos vetores u e v
vetor_u = np.array([[4, 7, 0, -8]])
vetor_v = np.array([[9, 17, -12, 21]])
resultado6 = np.inner(vetor_u, vetor_v)
print('\n6 apol){}'.format(resultado6))
resul_soma= vetor_u+vetor_v
print('soma6: ',resul_soma)


print('\n------------questão 12 ativi----------------')
u1 = np.array([[3, 6, -1]])
v1 = np.array([[11, 14, 9]])
resultado1 = np.inner(u1,v1) # operação conhecido como produto escalar ou produto interno, dá pra usar para calculo de media ponderada.
print('8) {}'.format(resultado1))

