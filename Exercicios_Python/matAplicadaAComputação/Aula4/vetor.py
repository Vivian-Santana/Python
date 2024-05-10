import numpy as np
# 1 exemplo de vetor
# v = np.array([[2,4,5,9]])
# print(v)

'''
Considere o vetor v que armazena os preços de venda, em dólares, de
algumas mercadorias anunciadas em um comércio eletrônico:
v=(22, 12, 54, 89, 11).
Supondo que cada dólar corresponde a R$ 5, obtenha um vetor u que
contém os preços destas mercadorias, mas em reais.
Precisamos escrever o vetor cambio com os respectivos preços em dólar e, em
seguida, precisamos multiplicar este vetor por 5 para que tenhamos um vetor
contendo os preços equivalentes em reais
'''

# cambio =np.array([[22, 12, 54, 89, 11]])
# conversao=5*cambio
# print(conversao)

'''
Considere o vetor v que armazena os preços de venda, em dólares, de
algumas mercadorias anunciadas em um comércio eletrônico:
v=(22, 12, 54, 89, 11)
e o vetor u que armazena os respectivos preços de custo, também em
dólares
u=(18, 4, 39, 61, 8)
Sabendo que a margem de contribuição corresponde ao preço de venda
menos o preço de custo, obtenha o vetor m que contém as respectivas margens
de contribuição, em dólares, destas mercadorias.
Para resolvermos este problema, basta fazermos a subtração v-u para
obtermos o vetor m.
'''
# v=np.array([[22, 12, 54, 89, 11]])
# u=np.array([[18, 4, 39, 61, 8]])
# m=v-u
# print(m)
'''
Obtenha um vetor contendo o valor de cada mercadoria mais o respectivo
frete. Neste caso, precisamos fazer a soma v+t para obtermos o vetor w, que
contém o valor de cada mercadoria mais o respectivo frete.
'''
# v=np.array([[22, 12, 54, 89, 11]])
# t=np.array([[3, 2, 1, 4, 1]])
# w=v+t
# print(w)

'''
Em uma instituição de ensino, os alunos matriculados em uma
determinada disciplina realizaram 4 atividades avaliativas. As notas obtidas por
um dos estudantes estão armazenadas no vetor “notas” e o vetor “pesos”
armazena as porcentagens referentes a cada avaliação, já na forma decimal. Os
vetores são:
notas=(90, 85, 70, 100)
e
pesos=(0,2; 0,2; 0,3; 0,3)
A média do estudante corresponde à soma das multiplicações de cada
nota pelos respectivos pesos. Como esta média pode ser obtida pelo produto
escalar (a média ponderada corresponde ao produto escalar: multiplicação de 
vetores onde vamos multiplicar componentes, somar os resultados e como resposta
 temos o numero.) dos vetores “notas” e “pesos”, determine a média obtida pelo estudante
'''

notas=np.array([[90, 85, 70, 100]])
pesos=np.array([[0.2, 0.2, 0.3, 0.3]])
media=np.inner(notas, pesos) # multiplicação de nota e peso. inner: produto escalar ou produto interno. 
print(media)                 # A função np.inner faz as operações com cada número dos vetores.

# outro jeito
'''
# Vetores de notas e pesos
notas = (90, 85, 70, 100)
pesos = (0.2, 0.2, 0.3, 0.3)

# Cálculo da média usando produto escalar
media = sum(nota * peso for nota, peso in zip(notas, pesos))

print("Média obtida pelo estudante:", media)
'''
'''
# apol questão 5
u=np.array([[134.10, 112.87, 146.02, 151.19, 147.08, 136.32]])
v =np.array([[89.10, 78.50, 94.09, 101.44, 89.99, 90.04]])
resultado=u+v
print(resultado)
'''