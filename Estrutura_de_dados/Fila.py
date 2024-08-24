'''
Fila -> QUEUES sem usar recursos do python. 
Insere o dado no final, remov e do início -> FIFO = First In First Out 
Implementando uma fila com as operações básicas de inserção (queue), remoção (dequeue) 
e listagem dos elementos. Utilizando uma lista do Python para simular a estrutura de dados da fila
'''
'''
A função queue - enfileirar
Verifica se chegou no fim da fila e se tem posição 
(vaga) para inserir no início.

Se a fila não está cheia, o elemento dado é inserido na posição fim.
O valor de fim é incrementado.
Se fim alcança tam, ele é resetado para 0 (circular).
'''
def queue(fila, fim, tam, dado):
  if len(fila) == tam:
    print('Fila cheia! Impossível inserir.\n')
  else:
    if fim < tam:
      fila.insert(fim, dado)
      fim += 1
    else:
      fim = 0
      fila.insert(fim, dado)
  return fila, fim

'''
A função dequeue - desenfileirar
O elemento na posição inicio é removido, substituindo-o por None.
O valor de inicio é incrementado.
'''
def dequeue(fila, inicio):
  if len(fila) == 0:
    print('Fila vazia! Impossível remover.\n')
  else:
    fila[inicio] = None
    inicio += 1
  return fila, inicio

# Programa principal
inicio = 0 # Índice de remoção (dequeue) da fila
fim = 0 # Índice de inserção (enqueue) na fila
fila = [] # Lista que será usada como a estrutura de dados da fila
tam = 5 # Capacidade máxima da fila

# menu
while True:
  print('\n1 - Inserir na fila')
  print('2 - Remover da fila')
  print('3 - Listar a fila')
  print('4 - Sair')

  op = int(input("Escolha uma opção: ")) # op é uma variável que armazena a opção escolhida pelo usuário
  if op ==1:
    dado = int(input('Qual número deseja inserir? '))
    fila, fim = queue(fila, fim, tam, dado) # o dado (num) digitado é passado para a função queue, que o adiciona à fila
  elif op == 2:
    fila, inicio = dequeue(fila, inicio) # a função dequeue é chamada para remover o elemento do início da fila
  elif op == 3:
    for item in fila:
      print(item, end=" ") # os elementos da fila são listados em uma linha, separados por espaço
    print()
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")
    