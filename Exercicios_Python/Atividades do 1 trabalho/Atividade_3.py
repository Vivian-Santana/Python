# função que pede as medidas do objeto, faz o calculo do volume e de quanto o usuário vai pagar pelo volume.
def dimensoes_objeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto (em cm): '))
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))

            volume = altura * largura * comprimento
            print('O volume do objeto é de: {:.2f} cm³\n'.format(volume))

            if volume < 1000:
                return 10.00
            elif volume < 10000:
                return 20.00
            elif volume < 30000:
                return 30.00
            elif volume < 100000:
                return 50.00
            else:
                print('Volume fora do limite aceitável!\n'+
                      'Digite as dimensões novamente.')
        except ValueError:
            print('Valor inválido! Digite apenas valores numéricos.') # caso o usuário digite um valor não numérico, cai na exceção e volta para o início do laço.
        continue

# função que pede o peso do objeto e faz o calculo de quanto o usuário vai pagar pelo peso.
def peso_objeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): ' ))
            
            if peso <= 0.1:
                return 1.00
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2.00
            elif peso < 30:
                return 3.00
            else:
                print('Limite de peso excedido! Digite o peso novamente.')
        except ValueError:
            print('Valor inválido! Digite um valor numérico válido.')

# função que pede a rota do objeto e faz o calculo de quanto o usuário vai pagar pela rota.
def rota_objeto():
    while True:      # menu de opções de rotas
        rota = input('\nDigite a rota do objeto (RS, SR, BS, SB, BR, RB):\n'+
                     'RS - Rio de Janeiro -> São Paulo\n' +
                     'SR - São Paulo -> Rio de Janeiro\n' +
                     'BS - Brasília -> São Paulo\n' +
                     'SB - São Paulo -> Brasília\n' +
                     'BR - Brasília -> Rio de Janeiro\n'+
                     'RB - Rio de Janeiro -> Brasília\n'+
                     '>> ').upper().strip() # upper() # se o usuário digitar minuscula transforma em maiúscula.
                                            # strip() # elimina espaços digitados, entre caracteres, sem querer pelo usuário.
        
        if rota == 'RS' or rota == 'SR':
            return 1.00
        elif rota == 'BS' or rota == 'SB':
            return 1.2
        elif rota == 'BR' or rota == 'RB':
            return 1.5
        else:
            print('Rota inválida! Digite uma rota válida.') # tratamento de erro se o usuário digitar uma rota inexistente.
        
# Programa principal
print(f'Programa de empresa de logística de Vivian de Sousa Santana')

print('------------ Bem vindo a Companhia de logistica! ------------')

# Chama todas as funções e faz o calculo de todo o custo de envio 
dimensoes = dimensoes_objeto()
peso = peso_objeto()
rota = rota_objeto()
total = dimensoes * peso * rota
# output do valor total e de como o calculo é feito. 
print('Total a ser pago: R$ {:.2f} (dimensoes: {:.2f} x peso: {:.2f} x rota: {:.2f})'.format(total,dimensoes, peso, rota))
