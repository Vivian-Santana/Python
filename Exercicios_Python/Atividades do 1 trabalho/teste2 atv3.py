def dimensoesObjeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto (em cm): '))
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
        except:
            print('O valor não é numérico')
            continue
        else:
            volume = altura * largura * comprimento
            if volume >= 100000:
                print('Infelizmente não poderemos enviar seu objeto porque o volume excede o limite aceitável.')

                repetir = input('Deseja enviar outro objeto? (s|n)\n'+
                                '>>')

                if repetir.lower() == 's':
                    continue
                else:
                    print('Encherrando atendimento...')
                    exit()
            else:
                break
    print ('o volume do seu objeto é: {:.2f} cm³'.format(volume))

    if volume < 1000:
        return 10.00
    elif volume < 10000:
        return 20.00
    elif volume < 30000:
        return 30.00
    elif volume <100000:
        return 50.00

def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg):' ))
          
        except ValueError:
            print('Valor inválido! Digite um valor numérico válido.')
            continue
        else:
            if peso <= 0:
                print('Peso inválido! O peso deve ser maior que zero.')
                continue
            else:
                break
      
    if peso >= 30:
        resposta = input('Infelizmente não poderemos enviar seu objeto porque ele ultrapassa o limite de peso aceitável. Deseja fazer outro envio? (s/n): \n')
        if resposta.lower() != 's' :
            print('Encherrando atendimento...')
            exit()
        else:
            return dimensoesObjeto()
    else:    
        if peso <= 0.1:
            return 1.00
        elif peso < 1:
            return 1.5
        elif peso < 10:
            return 2.00
        else:
            return 3

def rotaObjeto():
    while True:
        rota = input('Digite a rota do objeto (RS, SR, BS, SB, BR, RB): '+
                     'RS - Rio de Janeiro -> São Paulo\n' +
                     'SR - São Paulo -> Rio de Janeiro\n' +
                     'BS - Brasília -> São Paulo\n' +
                     'SB - São Paulo -> Brasília\n' +
                     'BR - Brasília -> Rio de Janeiro\n'+
                     'RB - Rio de Janeiro -> Brasília\n'+
                     '>> ').upper().strip()
        
        if rota == 'RS' or rota == 'SR':
            return 1.00
        elif rota == 'BS' or rota == 'SB':
            return 1.2
        elif rota == 'BR' or rota == 'RB':
            return 1.5
        else:
            print('Rota inválida! Digite uma rota válida.')
        rota = rota.upper() # se o usuário digitar minuscula transforma em maiúscula.
        rota = rota.strip() # elimina espaços digitados, entre caracteres, sem querer pelo usuário.

# programa principal que chama as funções: dimesoes, peso e rotaOjeto

print('--------------------------- Bem vindo a Companhia de logistica! ---------------------------')

dimensoes = dimensoesObjeto()
print()
peso = pesoObjeto()
print()
rota = rotaObjeto()
print()
total = dimensoes * peso * rota
    
print('Total a ser pago: R$ {:.2f} (dimensoes: {:.2f} x peso: {:.2f} x rota: {:.2f})'.format(total,dimensoes, peso, rota))
