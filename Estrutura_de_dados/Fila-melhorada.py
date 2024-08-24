#Fila usando com métodos do Python


fila = []
tam = 5

while True: 
  print('1 - Inserir na fila')
  print('2 - Remover da fila')
  print('3 - Listar a fila')
  print('4 - Sair')

# op é uma variável que armazena a opção escolhida pelo usuário
  op = int(input("Escolha uma opção:")) 
  if op == 1: 
    dado = int(input('Qual número deseja inserir?'))
    if len(fila) < 5:
      fila.append(dado) # append é um método embutido em listas Python que adiciona um novo elemento ao final da fila
    else:
      print('Fila cheia! Impossível inserir. ')
  elif op == 2: 
    if len(fila) > 0:
      fila.pop(0) # o método pop passando 0 como parâmetro remove e retorna o primeiro elemento da fila.
    else:
      print('Fila vazia! Impossível remover. ')
  elif op == 3:
    for item in fila:
      print(item, end=' ')
    print('\n')
  elif op == 4: 
    print('Encerrando...')
    break
  else: 
    print("Selecione outra opção!\n")