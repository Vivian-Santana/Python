'''
Uma indústria alimentícia produz cookies americanos. No processo de
fabricação, cada porção de massa é pesada antes de ser assada para que os
cookies sejam produzidos dentro do mesmo padrão. Espera-se que cada porção
tenha 50 gramas, mas por diversos fatores há uma variação no peso das
porções. A seguir, temos uma amostra contendo os pesos, em gramas, de 20
porções de massa:
49,7, 50,9, 48,9, 49,8, 50,1, 50,2, 50,8, 49,2, 50,1, 50,0,
50,4, 48,8, 49,3, 49,5, 49,1, 50,6, 49,0, 49,7, 49,7, 50,2
Com base nesses dados, obtenha o desvio padrão por meio do Python
'''
import pandas as pd

x= {'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]}
p= pd.DataFrame(x) # *
desvio_padrao= p['Pesos'].std() # o método std calcula o desvio padrão
print(f'Desvio padrão: {desvio_padrao}')

'''
* "DataFrame" é uma classe da biblioteca pandas em Python que é usada para criar e manipular 
estruturas de dados tabulares chamadas DataFrames. DataFrames são semelhantes a tabelas em 
bancos de dados ou planilhas, onde os dados são organizados em linhas e colunas.
 o código cria um DataFrame p contendo uma coluna chamada "Pesos" com os valores fornecidos e, 
 em seguida, calcula o desvio padrão dessa coluna usando o método .std() e gera a saída do desvio padrão.
'''

# QUESTÃO 9 APOL 2
n= {'Notas': [8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]}
p= pd.DataFrame(n)
desvio_padrao_2= p['Notas'].std()
print(f'Desvio padrão das notas dos alunos: {desvio_padrao_2}')

# questão 10 apol 2
media= p['Notas'].mean()
print(f'Média: {media}')