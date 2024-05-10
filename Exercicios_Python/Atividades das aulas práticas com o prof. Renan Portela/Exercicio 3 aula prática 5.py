'''
Atividade prática com o prof Renan Portela Jorge - aula prática 5
Restaurante que serve feijoada.
'''

# funções
def volume_feijoada():
    print('---------------------- Menu 1 de 3 - Volume Feijoada -----------------------')
    while True:
        try:
            volume_f = int(input('Digite a quantidade desejada (ml): '))
            if (volume_f >= 300) and (volume_f <= 5000): # segunda maneira if 300 <= volume_f <= 5000:(notação permitida em poucas linguagens).
                return volume_f * 0.08 #porta de saída da função para o programa principal.
            else:
                print('Digite apenas valores a partir de 300 ou acima de 5000.')
        except ValueError: # Caso o usuário digite algum valor diferente do que foi pedido.
            print('Digite apenas valores inteiros!')

def opção_feijoada():
    print('----------------------- Menu 2 de 3 - Opção Feijoada -----------------------')
    while True:
        opcao_f = input('Digite a opção de feijoada desejada\n'+
                        'b - Básica (Feijão + paiol + costelinha)\n'+
                        'p - Premium (Feijão + paiol + costelinha + partes de porco)\n'+
                        's - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)\n'+
                        '>> ')
        opcao_f = opcao_f.lower()
        opcao_f = opcao_f.strip() # elimina espaços digitados, entre caracteres, sem querer pelo usuário
        if opcao_f == 'b':
            return 1.00
        elif opcao_f == 'p':
            return 1.25
        elif opcao_f == 's':
            return 1.50
        else:
            print('Opção inválida! Para continuar digite uma das opções: b | p | s')
            continue # se cair nessa condição, volta para o início do laço.

def acompanhamento_feijoada():
    print('------------------- Menu 3 de 3 - Acompanhamento Feijoada ------------------\n')
    acumulador = 0
    while True:
        acompanhamento_f = input('Deseja um acompanhamento?\n'+
                                 '0 - Não (encerrar pedido)\n'+
                                 '1 - 200g de arroz\n'+
                                 '2 - 150g de farofa especial\n'+
                                 '3 - 100g de couve cozida\n'+
                                 '4 - 1 laranja descascada\n'+
                                 '>> ')
        if acompanhamento_f =='0':
            return acumulador
        elif acompanhamento_f == '1':
            acumulador += 5
            continue
        elif acompanhamento_f == '2':
            acumulador += 6
            continue
        elif acompanhamento_f == '3':
            acumulador += 7
            continue
        elif acompanhamento_f == '4':
            acumulador += 3
            continue
        else:
            print('Digite uma opção válida!')
# início do programa principal (main)
print('-------------------- Bem vindo ao programa de feijoada! --------------------')
volume = volume_feijoada() # recebe o retorno de volume_feijoada.
opcao = opção_feijoada()
acompanhamento = acompanhamento_feijoada()
# soma do total do pedido e print da saída.
total = (volume * opcao) + acompanhamento
print('O total ficou: R$ {:.2f},(Volume: R${:.2f}, Opção: {:.2f}, Acompanhamento: R$ {:.2f}) '.format(total,volume,opcao,acompanhamento))