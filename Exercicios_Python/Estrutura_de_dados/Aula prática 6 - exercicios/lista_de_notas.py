'''
Dada uma lista contendo as notas de alunos em uma disciplina, 
escreva uma expressão para:
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
a) Encontrar quantos alunos tiraram nota 7
b) Alterar a última nota para 4
c) Encontrar a maior nota
d) Ordenar a lista de notas
e) A média das notas
'''

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)
# Encontrar quantos alunos tiraram nota 7
quantidade_nota_7 = notas.count(7)
print('a) Quantidade de alunos com nota 7:' , quantidade_nota_7)

# Alterar a última nota para 4
notas[-1] = 4
print('\nb) Notas atualizadas: ', notas)

print('\nc) Maior nota: ', end='')
maior_nota = max(notas) # crio uma variável e passo o nome da lista dentro do parâmetro de max
print(maior_nota)

print('\nd) Ordenando as notas em ordem crescente: ', end='')
notas.sort()
print(notas)

print('\nd) Ordenando as notas em ordem decrescente: ', end='')
notas.sort(reverse=True) # o argumento passado no parâmetro de sorte reverte a ordenação dos dados.
print(notas)

print('\ne) Média das notas: ', end='')
media = sum(notas) / len(notas) # uso a função sum() para somar tds as notas, depois diviso pelo tamanho len()
print('{:.3}'.format(media))
# ou usar a função round para arredondar a média para duas casas decimais.

media_arredondada = round(media, 2)
print('e) Média das notas arredondada: ', media_arredondada)
