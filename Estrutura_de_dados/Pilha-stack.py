'''
Stacks (listas de python - arrays dinâmicos)

Utilizando uma lista do Python para simular a estrutura de dados da pilha.
Operações básicas de inserção (push) empilha os dados, 
remoção (pop) desempilha e listagem dos elementos. 

Insere o dado no início e remove do início (topo) -> LIFO = Last In First Out
'''

# Funções
def push(pilha, top, tam, dado):
  if len(pilha) == tam: # Verifica se a pilha já está na capacidade máxima (tam)
    print('Pilha cheia! Impossível inserir. ')
  else:
    pilha.insert(top, dado)
    top += 1 # incremento para inserir os dados em cada indice
    return pilha, top

def pop(pilha, top):
  if len(pilha) == 0: # Verifica se a pilha está vazia.
    print('Pilha vazia! Impossível remover. ')
  else:
    del pilha[top]
    top -= 1 # decremento para remover os dados de cada indice
    return pilha, top

# Programa principal
top = 0
pilha = [] # lista que será usada como a estrutura de dados da pilha
tam = 5 # variável que define a capacidade máxima da pilha

while True:
  print ('\nMenu')
  print('1 - Inserir na pilha')
  print('2 - Remover da pilha')
  print('3 - Listar a pilha')
  print('4 - Sair \n')

  op = int(input("Escolha uma opção: ")) # op é uma variável que armazena a opção escolhida pelo usuário
  if op ==1: 
    dado = int(input('Qual número deseja inserir? '))
    push(pilha, top, tam, dado) # chamada da função push para add o dado a pilha.
  elif op == 2: 
    pop(pilha, top) # a função pop é chamada para remover o elemento do topo da pilha
  elif op == 3:
    for item in pilha:
      print(item)
  elif op == 4: 
    print('Encerrando...')
    break
  else: 
    print("Selecione outra opção!\n")