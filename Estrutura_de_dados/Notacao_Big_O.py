'''
A notação Big-O é usada para mostrar como a complexidade de tempo e 
de espaço cresce à medida que a entrada também cresce.
Para representar a complexidade com Big-O, precisamos especificar 
somente a ordem de grandesa da função.
'''

# Exercício 1  o loop é executando n/2 temos notação O(n)

def Exercicio1 (dados):
    for i in range(0, len(dados)/2, 1):
        dados[i]= i * 2

#print (Exercicio1) 

# Exercício 2 (propriedade de adição) O(n)
def Exercicio2 (dados_2):
    for i in range(0, len(dados_2), 1):
        dados[i] = i + 1
    for i in range(0, len(dados_2), 1):
        dados_2[i] = i - 1

# Exercício 3 PA constante porque o laço interno vai ser executado um número constante de vezes notação O(n²)
def Exercicio3 (dados_3):
    for i in range(0, len(dados_3), 1):
        for j in range(0, len(dados_3), 1):
            dados_3[i] - dados_3[j] + 1

# Exercício 4 PA de -1 progreção aritmética (não constante) subtrai de um em um, notação O(n²)
def Exercicio3 (dados_4):
    for i in range(0, len(dados_4), 1):
        for j in range(i, len(dados_4), 1):
            dados_4[i] = dados_4[j] + 1

# Exercício 5 , notação O(n²)
def Exercicio5 (dados_5):
    for i in range(0, len(dados_5), 1):
        for j in range(0, len(dados_5), 1):
            for k in range(0, 9000000, 1): # 9 milhões é a constante
             dados_5[i] = dados_5[j] + 1

