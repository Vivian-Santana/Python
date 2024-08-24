'''VERSÃO SIMPLIFICADA DO PYTHON removendo e inserindo os dados 
usando pop e append diretamente nos laços if else.
'''
pilha = []
tam = 5

while True: 
  print('\n1 - Inserir na pilha')
  print('2 - Remover da pilha')
  print('3 - Listar a pilha')
  print('4 - Sair')

  op = int(input("Escolha uma opção: ")) 
  if op ==1: 
    dado = int(input('Qual número deseja inserir? '))
    if len(pilha) < tam:
      pilha.append(dado)
    else:
      print('Pilha cheia! Impossível inserir. ')
  elif op == 2: 
    if len(pilha) > 0:
      pilha.pop()
    else:
      print('Pilha vazia! Impossível remover. ')
  elif op == 3:
    # Inverte a pilha para exibir do último inserido ao primeiro e depois reverte de volta para manter a ordem original.
    pilha.reverse()
    for item in pilha:
      print(item)
    pilha.reverse()
  elif op == 4: 
    print('Encerrando...')
    break
  else: 
    print("Selecione outra opção!\n")