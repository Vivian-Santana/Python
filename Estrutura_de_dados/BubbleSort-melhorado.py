def bubbleSort(dados):
  tam = len(dados)
  for v in range(0, tam, 1):
    #flag começa em 0
    troca = 0
    for i in range(0, tam-1, 1):
      if dados[i] > dados[i+1]:
        aux = dados[i]
        dados[i] = dados[i+1]
        dados[i+1] = aux
        #se houve uma troca, mantém a flag em 1
        troca = 1
    if troca == 0:
      return