'''
Com o objetivo de criar um sistema novo de emplacamento de veículos, deputados em do Distrito Federal – DF, 
decidiram que o último número da placa dos veículos, irá representar o estado de registro dele. Para isso, 
sua equipe de desenvolvedores foi encarregada de desenvolver uma Tabela Hash com endereçamento em cadeia 
de 10 posições (cada posição do vetor deve ser uma lista encadeada), representando os números de 0 a 9 que 
irão representar os 26 estados e o Distrito Federal (total 27). 

A função hash deve seguir as seguintes regras: 
A entrada da função hash deve ser uma string com 2 letras, representando a sigla do estado e/ou distrito federal. 
Caso a sigla seja DF (Distrito Federal), por questões de superstição, os deputados solicitaram que o retorno da 
função seja 7 sempre. 
Caso contrário, a função deve retornar a posição com base no valor ASCII das duas letras e seguindo a seguinte regra: 

posição=(CHAR1ASCII+ CHAR2ASCII)MOD 10
'''
# Nó da lista encadeada. Cada nó contém a sigla de um estado e um ponteiro para o próximo nó na lista.
class Nodo:
    def __init__(self, sigla):
        self.sigla = sigla
        self.proximo = None

# Define uma lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None
    # Insere um novo nó no início da lista.
    def inserir_no_inicio(self, sigla):
        novo_nodo = Nodo(sigla)
        novo_nodo.proximo = self.head
        self.head = novo_nodo
    # Imprime todos os nós da lista encadeada, começando da head até o final.
    def imprimir_lista(self):
        atual = self.head
        while atual:
            print(f"[{atual.sigla}]", end=" -> ")
            atual = atual.proximo
        print("None")

# Define a tabela hash com encadeamento
class TabelaHash:
    # Inicializa a tabela hash com 10 posições, cada uma contendo uma lista encadeada.
    def __init__(self):
        self.tabela = [ListaEncadeada() for _ in range(10)]

    '''
    Função de hash que determina a posição na tabela para uma sigla. 
    A sigla "DF" retorna a posição 7, todas as outras são calculadas 
    pela soma dos valores ASCII dos caracteres da sigla, MOD 10
    '''
    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10 # a função ord do python recebe um caracter e retorna um inteiro.

    #  Insere uma sigla na posição correta da tabela, utilizando a função de hash para determinar a posição.
    def inserir(self, sigla):
        posicao = self.funcao_hash(sigla)
        self.tabela[posicao].inserir_no_inicio(sigla)

    # Imprime todas as listas encadeadas em cada posição da tabela hash
    def imprimir_tabela(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            self.tabela[i].imprimir_lista()

# Função principal do programa com inputs das siglas dos estados
def main():
    estados = [
        ("AC"), ("AL"), ("AP"), ("AM"), 
        ("BA"), ("CE"), ("DF"), ("ES"),
        ("GO"), ("MA"), ("MT"), ("MS"),
        ("MG"), ("PA"), ("PB"), ("PR"),
        ("PE"), ("PI"), ("RJ"), ("RN"),
        ("RS"), ("RO"), ("RR"), ("SC"),
        ("SP"), ("SE"), ("TO"), ("VS")
    ]

    # Cria uma instância da Tabela Hash
    tabela_hash = TabelaHash()

    # Insere cada sigla dos estados na Tabela Hash
    for sigla in estados:
        tabela_hash.inserir(sigla)

    tabela_hash.imprimir_tabela()

# Chama a função main
if __name__ == "__main__":
    main()
