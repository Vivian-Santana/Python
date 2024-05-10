# exemplo 1 matriz

import numpy as np
'''
A= np.array([[3, 2, -1],[5, 0, 20]]) # colchete maior associado ao array, concehtes internos menores associados às linhas da matriz.
print(A)
'''

'''
Uma indústria de cadeiras gamer possui três modelos denominados de A,
B e C, e possui duas fábricas chamadas de F1 e F2. Na fábrica F1, são
produzidas as peças, e na fábrica F2 é feita a montagem das cadeiras.
Os custos de produção e de transporte associados à fábrica F1
correspondem a
Custo de produção das peças (R$) Custo de transporte (R$)
A 400,00                            10,00
B 480,00                            12,00
C 600,00                            15,00
Os custos de montagem e de transporte associados à fábrica F2 são:
Custo de montagem (R$) Custo de transporte (R$)
A 31,00                 11,00
B 37,00                 11,00
C 48,00                 11,00
A partir destas informações, determine os custos totais de produção e de
transporte referentes a cada modelo de cadeira gamer.
Os custos são obtidos a partir da soma das matrizes associadas às
fábricas F1 e F2:
F2:
F1 = (400   10
      480   12
      600   15)
      e
F2 = (31    11
      37    11
      48    11)
'''
# F1=np.array([[400, 10],[480, 12],[600, 15]])
# F2=np.array([[31, 11],[37, 11],[48, 11]])
# CustoTotal=F1+F2
# print(CustoTotal)

'''
Sabendo que houve um aumento de 10% sobre os custos de fabricação
das peças e sobre os respectivos custos de transporte, quais serão os valores
após o aumento?
Como o aumento foi de 10%, podemos dizer que o fator de aumento
corresponde a 1,1, pois 100%+10%=110%=1,1. Para atualizarmos os valores,
basta multiplicarmos os dados de F1 por 1,1. Podemos armazenar esses valores
na própria matriz F1 por meio da expressão “F1=1.1*F1”.
'''
# F1=np.array([[400, 10],[480, 12],[600, 15]])
# F1=1.1*F1
# print(F1)

# MULTIPLICAÇÃO DE MATRIZES
# linha multiplica coluna
'''
Vamos agora aprender a multiplicar matrizes utilizando “np.matmul” da
biblioteca numpy.
Exemplo:
Dadas as matrizes
A = (3  1  3
     6  5  5) 
e 
B = (100  50
     50   100
     50   50)

calcule a multiplicação de A por B.
Chamando de C o resultado da multiplicação de A por B e utilizando os
comandos
'''
A=np.array([[3, 1, 3],[6, 5, 5]])
B=np.array([[100, 50],[50, 100],[50, 50]])
C=np.matmul(A, B)
print(C)
