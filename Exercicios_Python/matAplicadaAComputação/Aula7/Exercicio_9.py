'''
9. Durante um determinado dia, uma pessoa realizou de hora em hora medições da
velocidade de download de sua internet por meio de um aplicativo e obteve os seguintes
resultados em megabits por segundo (Mbps):
104,5; 128,9; 201,6; 233,3; 199,2; 236,4; 202,6; 261,1; 240,6; 212,7
Neste período, qual foi a velocidade média de download, em Mbps?

import pandas as pd
x={'Velocidade':[104.5, 128.9, 201.6, 233.3,
199.2, 236.4, 202.6, 261.1, 240.6, 212.7]}
d=pd.DataFrame(x)
media=d['Velocidade'].mean()
print(f'9) Média: {media:.1f}')
'''
# atividade pratica questão 1
import pandas as pd

x={'Velocidade':[67.8, 78.6, 54.4, 98.6,
99.4, 130.8, 142.6, 161.6, 142.5, 158.4]}
v=pd.DataFrame(x)
mediana= v['Velocidade'].median()
print(f'Mediana: {mediana}') # formatar a saída com menos numeros

# calcule a velocidade média questão 9
media= v['Velocidade'].mean()
print(f'\nMédia: {media}')

# calcule a moda
moda= v['Velocidade'].mode()
print(f'\nModa: {moda}')

# calculo do desvio padrão
desvio_padrao= v['Velocidade'].std()
print(f'\nDesvio padrão:  {desvio_padrao}')
