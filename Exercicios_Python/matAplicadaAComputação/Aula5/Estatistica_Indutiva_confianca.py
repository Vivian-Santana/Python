'''
Em uma indústria de produtos alimentícios, o peso médio associado a
pacotes de macarrão é de 504 gramas com desvio padrão de 10 gramas. Qual
é o intervalo de confiança para um nível de confiança igual a 90% considerando
uma amostra de 200 pacotes?
Como estamos considerando um nível de confiança igual a 90%, o
primeiro passo é dividirmos 90% por 2, o que resulta em 45% = 0,45. Essa
divisão é feita porque na tabela de distribuição normal temos os valores
associados à metade da curva de Gauss. Por meio da tabela, sabemos que 0,45
corresponde a z = 1,65.
'''
import math

# Dados do problema
peso_medio = 504  # Peso médio em gramas
desvio_padrao = 10  # Desvio padrão em gramas
nivel_confianca = 0.90  # Nível de confiança

# Tamanho da amostra
tamanho_amostra = 200

# Cálculo do valor de z baseado no nível de confiança
z = 1.65  # Valor correspondente a 0.45 na distribuição normal

# Cálculo do erro padrão da média
erro_padrao_media = desvio_padrao / math.sqrt(tamanho_amostra)

# Cálculo do intervalo de confiança
intervalo_inferior = peso_medio - z * erro_padrao_media
intervalo_superior = peso_medio + z * erro_padrao_media

# Exibindo o resultado
print(f"Intervalo de Confiança (90%): [{intervalo_inferior:.2f}, {intervalo_superior:.2f}] gramas")
