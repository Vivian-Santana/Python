'''
Lista encadeada simples, cada elemento só conhece o próximo elemento e o fim dela é nulo.
A lista sempre inicia no head e cada nó tem um ponteiro que aponta para o próximo elemento.
'''
# Cria cada elemento da lista corresponde a essa classe
class ElementoDaListaSimples:

# construtor de inicialização da classe
    def __init__(self, dado):
        self.dado = dado # instanciando dado
        self.proximo = None # ponteiro do prox dado vazio

#__repr__ é um método especial do Python
#use-o para criar a maneira como objeto 
#é mostrado fora da função print
    def __repr__(self):
        return self.dado

# Cria a lista encadeada simples
class ListaEncadeadaSimples:
  def __init__(self, nodos=None):
    self.head = None # inicilização da lista

    # limpa a lista se tiver informações desnecessárias
    if nodos is not None:
        nodo = ElementoDaListaSimples(dado=nodos.pop(0))
        self.head = nodo
        for elem in nodos:
            nodo.proximo = ElementoDaListaSimples(dado=elem)
            nodo = nodo.proximo
  
  # print da lista
  def __repr__(self):
      nodo = self.head
      nodos = []
      while nodo is not None:
          nodos.append(nodo.dado)
          nodo = nodo.proximo
      nodos.append("None")
      return " -> ".join(nodos)

# Varre a lista (iterador da lista)
  def __iter__(self):
    nodo = self.head
    while nodo is not None:
        yield nodo
        nodo = nodo.proximo

  def inserirNoInicio(self, nodo):
    nodo.proximo = self.head
    self.head = nodo

  def inserirNoFinal(self, nodo):
    if self.head is None:
        self.head = nodo
        return

    nodo_atual = self.head
    while nodo_atual.proximo != None:
        nodo_atual = nodo_atual.proximo

    nodo_atual.proximo = nodo
    return

  def deletar(self, dado):
    if self.head is None:
        raise Exception("A lista está vazia!")

    if self.head.dado == dado:
        self.head = self.head.proximo
        return

    nodo_anterior = self.head
    for nodo in self:
        if nodo.dado == dado:
            nodo_anterior.proximo = nodo.proximo
            return
        nodo_anterior = nodo

    raise Exception("Nó com o dado '%s' não foi econtrado." % dado)

Teste = ListaEncadeadaSimples() # recebe a classe da lista encadeada

# inserção de dados
Teste.inserirNoInicio(ElementoDaListaSimples('40'))
Teste.inserirNoInicio(ElementoDaListaSimples('4'))
Teste.inserirNoInicio(ElementoDaListaSimples('15'))
Teste.inserirNoInicio(ElementoDaListaSimples('7'))

Teste.inserirNoFinal(ElementoDaListaSimples('12'))
Teste.inserirNoFinal(ElementoDaListaSimples('24'))

# varredura na classe, printando os nós e impressão amigável dos outputs
for nodo in Teste:
  print(nodo, end=' -> ')
print('None')

Teste.deletar('4')

for nodo in Teste:
  print(nodo, end=' -> ')
print('None')