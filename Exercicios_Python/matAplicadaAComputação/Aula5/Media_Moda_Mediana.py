'''
Uma indústria alimentícia produz cookies americanos. No processo de
fabricação, cada porção de massa é pesada antes de ser assada para que os
cookies sejam produzidos dentro do mesmo padrão. Espera-se que cada porção
tenha 50 gramas, mas por diversos fatores há uma variação no peso das
porções. A seguir, temos uma amostra contendo os pesos, em gramas, de 20
porções de massa:
49,7, 50,9, 48,9, 49,8, 50,1, 50,2, 50,8, 49,2, 50,1, 50,0,
50,4, 48,8, 49,3, 49,5, 49,1, 50,6, 49,0, 49,7, 49,7, 50,2
Com base nesses dados, por meio do Python, obtenha a média, a moda
e a mediana
'''
from importlib.resources import files
import pandas as pd

x = {'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]} # pesos = coluna associada aos pesos

p= pd.DataFrame(x)
media= p['Pesos'].mean()
moda= p['Pesos'].mode()
mediana= p['Pesos'].median()
print(f'Média: {media}')
print(f'Moda: {moda}') # a moda tem a possibilidade de repetição de dados então na saída ela aparece com dois números, se não houver repetição, aparece apenas zero antes do único numero repetido.
print(f'Mediana: {mediana}') 

# Para resolvermos o mesmo problema, mas agora importando os dados de uma planilha
print('\nLendo os dados diretamente de uma tabela local:')
import io

caminho_arquivo = "C:\Planilhas\Planinha_aula5.xlsx"
dados = pd.read_excel(caminho_arquivo)
print(dados)
print()

media= p['Pesos'].mean()
moda= p['Pesos'].mode()
mediana= p['Pesos'].median()
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')