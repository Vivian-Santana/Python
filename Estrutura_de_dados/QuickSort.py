'''
Quick Sort -> ordenação rápida, tbm dividir para conquistar:

Usa um pivô para organizar os dados a partir dele, o usando como ponto de partida para divisão dos dados.
geralmente usa o primeiro dado como pivô, compara o pivô com tds os dados a esquerda e com 
tds os dados da direita, se o dado for menor que o pivô vai pra a esquerda, se for maior vai pra a direita.
A diferença do Quick sort para o merge sort é que Primeiro ele organiza os dados depois faz a recursão.
'''

#Versão clássica
def quickSort(dados,inicio,fim):
  if inicio < fim:
    posicao_de_particionamento = partition(dados,inicio,fim) # a posição onde o pivô parou
    quickSort(dados,inicio,posicao_de_particionamento - 1) # até o pivô
    quickSort(dados,posicao_de_particionamento + 1,fim) # após o pivô

def partition(dados,inicio,fim):
  '''
  Os índices esquerda e direita são usados para percorrer a lista 
  e posicionar os elementos corretamente em relação ao pivô.
  '''
  pivo = dados[inicio] # Escolhe o pivô como o primeiro elemento
  esquerda = inicio + 1
  direita = fim
  flag = False # Flag para controlar o loop

  '''
  A lista é reorganizada de modo que todos os elementos menores ou iguais ao pivô fiquem à esquerda 
  e os maiores ou iguais fiquem à direita.
  Isso é feito usando dois loops while que movem esquerda e direita até encontrar elementos fora de lugar, 
  que são então trocados.
  '''
  while not flag:
    # Move o índice esquerda para a direita enquanto os elementos forem menores ou iguais ao pivô
    while esquerda <= direita and dados[esquerda] <= pivo:
      esquerda += 1
    # Move o índice direita para a esquerda enquanto os elementos forem maiores ou iguais ao pivô
    while direita >= esquerda and dados[direita] >= pivo:
      direita -=1
    # Se os índices se cruzarem, a partição está completa
    if direita < esquerda:
      flag = True
    else:
      # Troca os elementos fora de lugar usando a variável temporária temp
      temp = dados[esquerda]
      dados[esquerda] = dados[direita]
      dados[direita] = temp
 # Coloca o pivô em sua posição correta usando a variável temp
  temp = dados[inicio]
  dados[inicio] = dados[direita]
  dados[direita] = temp
  return direita

'''
A expressão esquerda += 1 é (forma abreviada de escrever esquerda = esquerda + 1). 
Isso significa que o valor de esquerda é aumentado em 1. É usado para mover o índice
esquerda para a direita, percorrendo a sublista em busca de um 
elemento maior que o pivô.
Já o contrário direita -= 1 é (forma abreviada de escrever direita = direita - 1). 
Isso significa que o valor de direita é diminuído em 1. É usado para mover o índice
direita para a esquerda, percorrendo a sublista em busca de um elemento menor que o pivô.

A variável temp é utilizada como uma variável temporária para ajudar na troca de elementos 
entre duas posições em uma lista. Uma técnica comum em algoritmos de ordenação, onde é 
necessário trocar elementos de lugar para organizar os dados.
'''

#Programa Principal
dados = [50,25,92,16,76,30,43,54,19]
quickSort(dados,0,len(dados)-1)
print(dados)