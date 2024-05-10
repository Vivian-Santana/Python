'''
Considere um projetor multimídia cuja lâmpada tem vida útil de 5000
horas com desvio padrão de 300 horas. Supondo que os dados estão de acordo
com uma distribuição normal, determine por meio do Python a probabilidade de
que um projetor, selecionado ao acaso, tenha lâmpada com vida útil entre 5000
e 5500 horas. 
'''
import scipy.stats
'''
media=5000
desvio_padrao=300
X=5500
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(f'A Probabilidade é de: {p}') 
'''
'''
Saída corresponde a 45,22%. A diferença entre o valor obtido por meio do Python
e o valor obtido por meio da tabela (45,25%) é que, no uso da tabela, foi feito um
arredondamento no valor de z.
'''
# apol questão 4
media=12000
desvio_padrao=800
X=10000
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(f'A Probabilidade é de: {p}') 
