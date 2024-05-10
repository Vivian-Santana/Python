'''
Crie um jogo de pedra, papel ou tesoura (Jokenpô). 
Você deverá jogar contra o computador. 
Você irá sempre escolher uma das opções: 1- pedra, 2 – papel, 3 – tesoura
O computador irá sempre sortear um número de 1 até 3 para jogar.
Armazene todos os resultados em uma lista e no final apresente o vencedor
Encerre o programa ao digitar zero.
'''

import random
# as opções válidas (pedra, papel, tesoura) são armazenadas na lista opções
opcoes = ['pedra', 'papel', 'tesoura']
resultados = []
print('JOKENPÔ')
# A cada iteração do loop, o usuário fa uma escolha digitando o número correspondente
while True:
    print("Escolha sua opção:")
    print("1 - pedra")
    print("2 - papel")
    print("3 - tesoura")
    print("0 - encerrar o jogo")
    
    escolha = int(input("Digite sua escolha: "))
    
    if escolha == 0:
        break
    
    if escolha < 1 or escolha > 3:
        print("Opção inválida. Você só pode escolher um número ente 1 e 3.")
        continue
    
    escolha_usuario = opcoes[escolha - 1]
    
    '''
    o computador escolhe uma opção aleatória usando a função random.choice() do módulo radom, 
    que é o tipo de um "sorteador" em Python que retorna um elemento aleatório de uma sequência.
    no caso aqui da sequência da lista opções passada em seu parâmetro.
    '''

    escolha_computador = random.choice(opcoes)
    
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_computador)
    
    # comparação da escolha do usuário com a do computador e o resultado de quem venceu ou perdeu.
    if escolha_usuario == escolha_computador:
        resultado = 'Empate'
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        resultado = 'Você venceu!'
    else:
        resultado = 'Você perdeu!'
    
    resultados.append(resultado) # Os resultados são armazenados na lista resultados.
    
    print("Resultado:", resultado)
    print()
    
print("Fim de Jogo!")
print("Resultados:", resultados)
 
# O jogo continua até que você digite zero para encerrar.