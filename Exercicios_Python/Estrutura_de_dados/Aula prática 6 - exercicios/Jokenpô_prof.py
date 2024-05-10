# função para validar os dados de entrada da jogada
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
        return x
    
def vencedor(jogador1, jogador2):
    global empate, vencedor1, vencedor2 
    if jogador1 == 1: # pedra
        if jogador2 == 1: # pedra
            empate += 1
        elif jogador2 == 2: # papel
            vencedor += 1
        elif jogador2 == 3: # tesoura
            vencedor += 1
    elif jogador1 == 2: # papel
        if jogador2 == 1: # pedra
            vencedor += 1
        elif jogador2 == 2: # papel
            empate += 1
        elif jogador2 == 3: # tesoura
            vencedor += 1
    elif jogador1 == 3: # tesoura
        if jogador2 == 1: # pedra
            vencedor2 += 1
        elif jogador2 == 2: # papel
            vencedor1 += 1
        elif jogador2 == 3: # tesoura
            empate += 1
    resultados = [vencedor1, vencedor2, empate] # índice 0 = vencedor 1; indice 1 = vencedor 2; indeice 2 = empate.
    return resultados

# programa principal
print('JOKENPÔ')
print("Escolha sua opção:")
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")

resultados = []
jogadas = []
vencedor1 = 0
vencedor2 = 0
empate = 0

# jogador1: humnano; jogador2: computador
while True:
    jogador1 = valida_int('Escolha sua jogada: ', 0 , 3)
    if not jogador1: # mesmo que: if j1 == 0
        break
    jogador2 = random.randint(1,3)
    jogadas.append([jogador1, jogador2]) # add um item no final da lista
    resultados = vencedor (jogador1, jogador2) # resultados calculados

# todas as jogadas
    # for jogada in jogadas:
    #     for dado in jogada:
    #         print(dado, end=' ')
    #         print()

# output
print('Numero de vitórias do jogador 1: {}'.format(resultados[0])) # índice 0 = vencedor 1; indice 1 = vencedor 2; indeice 2 = empate.
print('Numero de vitórias do jogador 2: {}'.format(resultados[1]))
print('Numero de empates: {}'.format(resultados[2]))