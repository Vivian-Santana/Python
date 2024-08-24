#Bubble sort - ordenando array de forma decrescente

def algoritmo(dados):
    tam = len(dados)
    for v in range(0, tam, 1): # Inicia um loop for que percorre a lista inteira. A variável v vai de 0 até tam  1 (não inclusivo). 
                            # Este loop controla o número de passadas que a função fará sobre a lista.

        flag = 0 # variável é usada para verificar se ocorreu alguma troca de elementos na iteração atual do loop interno.
        for i in range(0, tam - 1, 1): # Inicia um segundo loop for, que também percorre a lista. A variável i vai de 0 até tam - 2 (não inclusivo).
                                            # Este loop é responsável por comparar pares adjacentes de elementos na lista.
            if dados[i] < dados[i + 1]:   
                aux = dados[i]
                dados[i] = dados[i + 1] # Esta operação troca a posição dos dois elementos, movendo o maior elemento para a frente.
                dados[i + 1] = aux
                flag = 1
        if flag == 0:
            return dados

# Exemplo de vetor
dados = [5, 2, 9, 1, 5, 6]

# Chamando o algoritmo e imprimindo a saída
resultado = algoritmo(dados)
print("Vetor ordenado:", resultado)

# saída Vetor ordenado: [9, 6, 5, 5, 2, 1]