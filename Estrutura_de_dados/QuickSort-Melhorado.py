'''
Versão simplificada usando as característica do Python

Esta versão simplificada do algoritmo QuickSort utiliza as características avançadas do Python, 
como a compreensão de listas, para tornar o código mais conciso e legível.
'''
def quickSort(dados):
  # Se a lista dados tiver menos de 2 elementos, ela já está ordenada e é retornada como está.
  if len(dados) < 2:
    return dados
  else:
    pivo = dados[0] # O primeiro elemento da lista é escolhido como o pivô.
    '''
    Usando compreensões de listas, a lista é dividida em duas sublistas: menores e maiores.
    menores contém todos os elementos menores ou iguais ao pivô.
    maiores contém todos os elementos maiores que o pivô.
    '''
    menores = [i for i in dados[1:] if i <= pivo]
    maiores = [i for i in dados[1:] if i >  pivo]

    '''
    Chamada Recursiva e Combinação:
    A função quickSort é chamada recursivamente nas sublistas menores e maiores.
    Os resultados são concatenados com o pivô no meio para formar a lista ordenada.
    '''
    return quickSort(menores) + [pivo] + quickSort(maiores)

#Programa Principal
dados = [50, 25, 92, 16, 76, 30, 43, 54, 19]
dados = quickSort(dados)
print(dados)