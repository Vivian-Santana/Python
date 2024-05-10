'''
aula 5 tema 5
função como parâmetro de função:
permite a criação de rotinas bastante genéricas.
'''

def imprime_com_condicao(num,fcond):
    if fcond(num): # substituindo a palavra fcond pelo nome da função q passei como parâmetro 
        print(num)

def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

# Programa principal
imprime_com_condicao(5, impar)