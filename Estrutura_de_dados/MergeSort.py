# Merge Sort -> Dividir para conquistar
'''
A função mergeSort divide a lista principal dados em duas sublistas, esquerda e direita. 
Após ordenar recursivamente essas sublistas, ela as mescla de volta na lista original dados.

Divisão Recursiva: O array é continuamente dividido em metades até que cada sub-array tenha 
um único elemento ou nenhum (o que significa que está ordenado por definição).

Mesclagem: Os sub-arrays são então mesclados em ordem crescente, reunindo-os para formar o array ordenado final.
'''

def mergeSort(dados):
  
  # Condição que indica se os dados ainda precisam ser divididos
  if len(dados) > 1: # verifica o tamanho do conjunto de dados (neste caso é 8, e 8 é > q 1).

    # divide recursivamente
    meio = len(dados)//2 # pega o tamanho do conjunto de dados e divide por 2, // pega só a parte inteira da divisão.
    esquerda = dados[:meio] # a variável da esquerda recebe a lista até o meio.
    direita = dados[meio:]  # a vairável da direita pega do meio até o fim.

    '''
    A função mergeSort é chamada recursivamente para esquerda e direita 
    até que cada sublista contenha apenas um elemento 
    (lembrando que uma função recursiva invoca ela mesma).
    
    invocando a função mergeSort pegando só o ramo esquerdo,
    vai pegando os dados da esquerda até ficar com um dado só,
    quando ficar com um dado só a condição recursiva para de ser executada,
    e o mergeSort passa a ser chamado do lado direito.
    '''
    mergeSort(esquerda)
    mergeSort(direita)

    '''
    Após quebrar tds os dados em partes unitárias essa parte do código intercala/mescla 
    os dados. Os dados serão organizados no local certo da lista.
    '''

    '''
    Após a ordenação recursiva, os índices i, j, e k são usados 
    para mesclar esquerda e direita de volta em dados:
        i é o índice para percorrer a sublista esquerda.
        j é o índice para percorrer a sublista direita.
        k é o índice para percorrer e colocar elementos na lista dados.
    Os índices garantem que os elementos sejam comparados e colocados 
    na ordem correta em cada etapa da mesclagem.
    '''
    i = j = k = 0 # inicialização dos índices

    '''
    Mescla os sub-arrays esquerda e direita:
    Este loop compara os elementos de esquerda e direita e coloca o menor elemento em dados[k].
    i é incrementado se o elemento de esquerda é menor.
    j é incrementado se o elemento de direita é menor.
    k é sempre incrementado para mover para a próxima posição em dados.
    '''
    while i<len(esquerda) and j<len(direita):
      if esquerda[i]<direita[j]:
        dados[k]=esquerda[i]
        i=i+1
      else:
        dados[k]=direita[j]
        j=j+1
      k=k+1

    '''
    Essa parte adiciona os elementos restantes, caso algum dado tenha 
    ficado de fora da lista, os loops garantem que quaisquer elementos restantes 
    em esquerda ou direita sejam adicionados a dados.
    Se esquerda ainda tem elementos (i < len(esquerda)), eles são copiados para dados.
    Se direita ainda tem elementos (j < len(direita)), eles são copiados para dados.
    Visualização com um Exemplo:
    '''
    # Adiciona os elementos restantes de esquerda, se houver
    while i<len(esquerda):
      dados[k]=esquerda[i]
      i=i+1
      k=k+1

    # Adiciona os elementos restantes de direita, se houver
    while j<len(direita):
      dados[k]=direita[j]
      j=j+1
      k=k+1

# Programa Principal
# os dados serão organizados em ordem crescente.
dados = [54, 26, 93, 17, 77, 31, 44, 55]
mergeSort(dados)
print(dados)

