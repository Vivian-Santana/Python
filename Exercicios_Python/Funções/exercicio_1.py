'''
aula 5 tema 2
Escreva uma função que calcule o fatorial de um número recebido como parâmetro e
retorne o seu resultado. Faça uma validação dos dados por meio de uma outra função,
permitindo que somente valores positivos sejam aceitos. Crie o help da sua função 
(exercício da apostila - aula 5)
'''

def validar_numero(numero):
    '''Valida se o número fornecido é positivo.
    
    Parâmetros:
        numero (int): O número a ser validado.
        
    Retorna:
        bool: True se o número for positivo, False caso contrário.
    '''
    if numero < 0:
        print("Erro: O número deve ser positivo.")
        return False
    return True


def calcular_fatorial(numero):
    '''Calcula o fatorial de um número.
    
    Parâmetros:
        numero (int): O número para o qual o fatorial será calculado.
        
    Retorna:
        int: O fatorial do número fornecido.

        Se a função validar_numero retornar False, ou seja, se o número não for positivo, 
        o bloco de código dentro desse if será executado. Isso significa que a validação 
        falhou e, portanto, retornamos None, indicando um valor inválido.
    '''
    if not validar_numero(numero): #not nega a função validar_numero, ele inverte o valor de verdade de uma expressão booleana.
        return None # se o num for negativo retorna "None".
    
    resultado = 1 # Inicializa-se a variável resultado com 1, pq o fatorial de qualquer número é sempre iniciado com 1.
    for i in range(1, numero + 1): # o loop for itera de 1 até o número fornecido. Isso permite multiplicar todos os números de 1 até o número fornecido para calcular o fatorial.
        resultado *= i # Dentro do loop, multiplica-se o valor atual de resultado pelo valor de i. Isso é feito repetidamente em cada iteração do loop, o que calcula o fatorial.
    return resultado # Após o loop, retorna-se o valor final de resultado, que é o fatorial do número fornecido.

# Teste
print(calcular_fatorial(5))  # Saída esperada: 120
print(calcular_fatorial(0))  # Saída esperada: 1
print(calcular_fatorial(-3)) # Saída esperada: None
