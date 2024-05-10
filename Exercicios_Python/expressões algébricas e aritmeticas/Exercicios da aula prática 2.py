'''
Exercicios da aula prática 2
Escreva as seguintes expressões algébricas em linguagem Python:
A) O somatório dos 5 primeiros números inteiros;
B) A média entre 23, 19 e 31
C) O número de vezes que 73 cabe em 403
D) A sobra quando 403 é dividido por 73
E) 2 elevado à 10ª potência
F) O valor Absoluto da diferença entre 54 e 57
G) O menor valor entre 34, 29 e 31
'''

print('a) ', 1 + 2 + 3 + 4 + 5, '\n')

print('b) ',(23 + 19 + 31) / 3, '\n')

print('c) ',403 // 73 , '\n') # resultado só da parte inteira

print('d) ',403 % 73, '\n')

print('e) ',2 ** 10, '\n')

print('f) ',abs(54-57), '\n') # saída valor absoluto (ignora o sinal- q seria -3)

print('g) ',min(34, 29, 31), '\n')

'''
Atribuição
H) atribuir o valor inteiro 3 à variável a
I) atribuir o valor 4 à variável b
J) atribuir à variável c o valor da expressão a*a + b*b
'''

# h
a = 3

# i
b = 4

# j
c = a*a + b*b

'''
Execute as seguintes atribuições:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
'''
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

'''
Utilizando operadores + e *, crie as saídas a seguir:
k) 'ant bat cod'
L) 'ant ant ant ant ant ant ant ant ant ant '
M) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
N) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
'''

print('k) ', s1 + ' ' + s2 + ' ' + s3, '\n')

print('l) ', 10 * (s1 + ' '), '\n')

print('m) ', 7 * (s1 + ' ' + s2 + ' '), '\n')

print('n) ', 5 * ((s2 * 2) + s3 + ' '), '\n')