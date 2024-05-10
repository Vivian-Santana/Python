# Respresentação de números usando a notação científica normalizada - aula 3
a = 3242
print('%.10e' % a)

numero = 12453301
print('%.10e' % numero)

'''
a saída será 3.2420000000e+03 o e+03 indica que o num foi multiplicado por 10³
A função % é usada para formatação de string e permite que inserir valores formatados em uma string. 
Nesse caso %.10e indica que a formatação do número usando a notação científica será com 10 casas decimais após o ponto (10 casas na mantissa).
'''
print()

# 0,23241 = 2,3241 * 10⁻¹
b = 0.23241
print('%.4e' % b) # saída com 4 casas decimais.

print()

# 0,0000054 = 5,4 * 10⁻⁶
print('%.4e' % 0.0000054)

print()

# 543230.0 corresponde a 5,4323 * 10⁵ q é igual a 5,4323 * 100000
print(5.4323e+05) # saída 543230.0

print('\nARITMÉTICA DE PONTO FLUTUANTE')

print('\nSoma')
c = 2.3421e+02 # 2.3421 * 10²
d = 3.5154e+02 # 3.5154 * 10²
e = c+d
print('%.10e' % e)

print('\nQuestão 8')
r= 8.151521e+03
s= 2.456732e+03
t= r+s
print('%.10e'% t)

print('\nQuestão 2')
u= 8.151521e+03
v= 2.456732e+03
x= u*v
print('%.10e'% x)

'''
A notação "e+02" (ou "E+02") é uma forma de representar números em notação científica. 
Ela indica que o número que a precede deve ser multiplicado por 10 elevado à potência 
indicada após o "e+" (ou "E+"). Nesse caso específico, "e+02" significa multiplicar 
o número por 10 elevado à potência de 2.
'''
print('\nSoma com expoentes diferentes')

f = 2.3421e+02 # 10²
g = 3.5154e+04 # 10⁴
h = f+g
print('%.10e' % h)

print('\nSoma com expoentes diferentes')
letra_A = 8.151521e+05 #  * 10⁵
letra_B = 2.456732e+03 #  * 10³
resposta = letra_A+letra_B
print('%.10e' % resposta)

print('\n-------ATIV PRAT Q 18--------')
var_a = 7.0102e+05
var_b = 2.1233e+03
resp = var_a + var_b
print('%.10e'% resp)

print('\nSubtração')

i = 2.3421e+02 # 10²
j = 3.5154e+02 # 10²
k = i-j
print('%.10e' % k)

print('\n-------ATIV PRAT Q 17--------')
a2= 7.0102e+05
b2= 2.1233e+03
resul = a2 - b2
print('%.10e'% resul)

print('\nMultiplicação')

l = 2.34221e+02 # 10²
m = 3.5154e+02  # 10²
n = l*m
print('%.10e'% n)

print('\nDivisão')

o = 2.34221e+02 # 10²
p = 3.5154e+02  # 10²
q = o/p
print('%.10e'% q)

# ativ q 8
print()
a1 = 7.0102e+05
b1 = 2.1233e+03
resultado = a1/b1
print('%.10e'% resultado)