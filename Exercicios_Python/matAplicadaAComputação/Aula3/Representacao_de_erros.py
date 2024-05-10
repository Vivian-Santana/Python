# Aula 3 números reais e erros
from math import factorial, pi

x_graus= float(input('Digite o valor do ângulo, em graus: '))
termos= int(input('Digite o número de termos do somatório: ')) # se digitar um num mt grande aqui terá um erro de overflow (num mt grande ou alé da capacidade de processamento do sistema)
x_radianos= pi*x_graus/180
seno= 0
for n in range(termos):
    seno= seno+(-1)**n*x_radianos**(2*n+1)/factorial(2*n+1)
print(seno)

print()

'''
erro absoluto
O erro absoluto é o módulo da diferença entre o valor exato e o valor
aproximado: 𝐸𝐴 = |𝑥 − 𝑥̅|

em que x é o valor exato e 𝑥̅ é o valor aproximado.
Exemplo:
Considere um problema em que o valor exato de uma variável
corresponde a 123450,10 e o valor aproximado é 123400. 
Qual é o erro absoluto?

O erro absoluto é dado por

𝐸A = |𝑥 − 𝑥̅|.

Como x=123450,10 e 𝑥̅=123400, temos:

𝐸𝐴 = |𝑥 − 𝑥̅|
𝐸𝐴 = |123450,10 − 123400|
𝐸𝐴 = |50,10|
𝐸𝐴 = 50,10
'''

# Em Python, o módulo é calculado pela função abs(). Assim, temos
print('Erro absoluto:')
print(abs(123450.10-123400))
'''
É possível perceber que há um erro de arredondamento no resultado
apresentado, pois em vez de 50,10, é apresentado o valor 50,10000000000582.
O erro relativo é a divisão do módulo da diferença entre o valor exato e o valor
aproximado pelo módulo do valor exato:
𝐸𝑅 =|𝑥−𝑥̅||𝑥|, 𝑥 ≠ 0.
Podemos escrever o erro relativo na forma de porcentagem. Basta
multiplicarmos esse erro por 100%:
𝐸𝑅 =|𝑥−𝑥̅||𝑥|. 100%, 𝑥 ≠ 0
'''
print()
'''
Considere um problema onde o valor exato de uma variável corresponde
a 123450,10 e o valor aproximado é 123400. Qual é o erro relativo?
O erro relativo é dado por
𝐸𝑅 =|𝑥−𝑥̅||𝑥|, 𝑥 ≠ 0.
Como x=123450,10 e 𝑥̅=123400, temos:

𝐸𝑅 =|𝑥 − 𝑥̅||𝑥|𝐸𝑅 =|123450,10 − 123400||123450,10|
𝐸𝑅 =|50,10||123450,10|𝐸𝑅 = 50,10123450,10
𝐸𝑅 = 0,00040583199...

Na forma de porcentagem, temos
𝐸𝑅 = 0,00040583199 𝑥 100%
𝐸𝑅 = 0,040583199%
Por meio do Python, temos o cálculo do erro absoluto:
'''
print('Erro relativo:')
print(abs(123450.10-123400)/abs(123450.10))

print()

# tratamento de erros
x = 10
y = 0
try:
    x/y
except ZeroDivisionError:
    print('Infelizmente ocorreu um erro. Não é possível realizar uma divisão por zero.')