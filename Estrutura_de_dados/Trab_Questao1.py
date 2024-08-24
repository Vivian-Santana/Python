'''
Com a finalidade de melhorar o atendimento e priorizar os casos mais urgentes, a direção de um hospital 
criou um sistema de triagem em que um profissional da saúde classifica a ordem de atendimento com base numa avaliação 
prévia do paciente, entregando-lhe um cartão numerado verde (V) ou amarelo (A), que define o menor ou maior grau de 
urgência da ocorrência, respectivamente. Para informatizar esse processo, a direção do hospital contratou você para 
desenvolver uma fila de chamada seguindo as seguintes regras:

•	Pacientes com cartão numerado amarelo (A) são chamados antes dos pacientes com cartão numerado verde (V)
•	Entre os pacientes com cartão numerado amarelo (A), os que tem numeração menor são atendidos antes.
•	Entre os pacientes com cartão numerado verde (V), os que tem numeração menor são atendidos antes.
•	As numerações dos cartões amarelos (A) iniciam em 201.
•	As numerações dos cartões verdes (V) inicial em 1.
'''

# Cria cada cartão de atendimento (instancia cada elemento da lista)
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Inicialização da classe listaEncadeada
class ListaEncadeada:
    def __init__(self):
        self.head = None

# Funções para verificar a prioridade de atendimento

    def inserirSemPrioridade(self, nodo):
        # Se a lista estiver vazia, o nodo se torna a cabeça da lista
        if self.head is None:
            self.head = nodo
        else:
            # se não estiver, percorre até o final da lista para inserir o nodo
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo
            print("Paciente adicionado com sucesso!")

    def inserirComPrioridade(self, nodo):
        # Se a lista estiver vazia ou o primeiro nodo for verde, insere no início
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            # se não, insere o nodo após todos os nodos amarelos
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo
            print("Paciente adicionado com sucesso!")

    # Função para inserção de pacientes
    def inserir(self):
        # Solicita ao usuário a cor e o número do cartão
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        nodo = Nodo(numero, cor)
        # Se a lista estiver vazia, a head da lista aponta para o nodo criado
        if self.head is None:
            self.head = nodo
        # Se a cor for verde, insere sem prioridade
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        # Se a cor for amarela, insere com prioridade
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        # Imprime todos os cartões da lista de espera.
        atual = self.head
        resultado = "Lista ->"
        while atual:
            resultado += f" [{atual.cor}, {atual.numero}]"
            atual = atual.proximo
        print(resultado)

    # Função para chamar paciente
    def atenderPaciente(self):
        # Remove o primeiro paciente da fila e imprime uma mensagem de atendimento
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(f"Atendendo o paciente cartão cor {self.head.cor} e número {self.head.numero}")
            self.head = self.head.proximo

# Função para exibição de menu de atendimento
def menu():
    lista = ListaEncadeada()
    while True:
        # Exibe o menu e solicita uma opção ao usuário
        print("\nMenu:")
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair\n")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            lista.inserir()
        elif opcao == '2':
            lista.imprimirListaEspera()
        elif opcao == '3':
            lista.atenderPaciente()
        elif opcao == '4':
            print('Encerrando o programa...')
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu para interagir com o usuário
menu()
