import random
def buscaBinaria (inicio, fim, dados, buscado): # bucado é o num digitado no input
    while(inicio <= fim):
        meio = int((inicio + fim) /2)

        if(buscado > dados[meio]):
            inicio = meio + 1
        elif(buscado < dados[meio]):
            fim = meio - 1
        else:
            return meio
    return -1

# main - gerando 10 valores dentro de um intervalo de 0 a 9

dados = random.sample(range(10), 10)
dados.sort() # ordena os dados
print(dados)
buscado = int(input('Digite o valor que deseja buscar: '))
achou = buscaBinaria(0, len(dados), dados, buscado)
if(achou == -1):
    print('valor não encontrado.')
else:
    print('valor encontrado na posição {}'.format(achou))

