# Variávies globais
lista_peca = []
codigo_peca = 0

# função para cadastrar peças
def cadastrar_peca(codigo):
    print('\n*** Menu de cadastro de peças ***')
    print('Codigo da peça: {}'.format(codigo))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    preco = float(input('Digite o preço(R$) da peça: '))

    # dicionário das variáveis
    dicionario_peca = {'codigo'       : codigo,
                        'nome'        : nome,
                        'fabricante'  : fabricante,
                        'preço'       : preco}
    lista_peca.append(dicionario_peca.copy()) # inserindo o dicionário na lista
    print('Peça cadastrada com sucesso!\n')

# função para consultar peças do estoque
def consultar_peca():
    print('\n*** Menu de consulta de peças ***\n')
    while True:
         # menu secundario (de consulta de peças)
        opcao_consultar = input('Escolha a opção desejada:\n'+
                                '1-Consultar todas as peças\n'+
                                '2-Consultar peça por código\n'+
                                '3-Consultar peça por fabricante\n'+
                                '4-Retornar\n'+
                                '>> ')
        
        # condição para consultar todas as peças que existem no estoque
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar todas as peças.')
            # percorrendo a lista de peças, a variável peça é o iterador
            for peca in lista_peca: # peca vai varrer toda a lista de peças
                print('-' * 25)
                # percorrendo um dicionário usando a chave e valor
                for key, value in peca.items(): # varre todos os conjuntos chave e valor do dicionário de peças.
                    print('{} : {}'.format(key, value))
                print('-' * 25)
        
        # condição para consultar peça por código
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar peça por código.')
            # acessar uma peça específica
            valor_desejado = int(input('Digite o código desejado: '))

            # exceção para validar se o código da peça que usuário digitou existe
            try:
                peca_encontrada = next(peca for peca in lista_peca if peca['codigo'] == valor_desejado)
                print('-' * 25)
                for key, value in peca_encontrada.items():
                    print('{} : {}'.format(key, value))
                print('-' * 25)
            except StopIteration: # Se nenhuma peça for encontrada entra na exceção StopIteration, printando a mensagem "Peça não encontrada".
                print('Peça não encontrada!\n'+
                      'Ou a peça não existe ou foi removida.\n')
        # condição para consultar peças pelo fabricante
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar peça por fabricante.')
            valor_desejado = input('Digite o nome do fabricante desejado: ').lower().strip()

        # condição que valida se existe peças de determinado fabricante
            pecas_encontradas = [peca for peca in lista_peca if peca['fabricante'] == valor_desejado]
            if pecas_encontradas:
                for peca in pecas_encontradas:
                    print('-' * 25)
                    for key, value in peca.items():
                        print('{} : {}'.format(key, value))
                    print('-' * 25)
            else:
                print('Não foi encontrada nenhuma peça deste fabricante.\n')

        elif opcao_consultar == '4':
            return # volta para o menu principal.
        else:
            print('Opção inválida! tente novamente.')
            continue

# função para remover peças
def remover_peca():
    valor_desejado = int(input('Digite o código da peça que deseja remover: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:
            lista_peca.remove(peca)
            print('Peça removida com sucesso!\n')
 
# programa principal (main)
print('--------------- Bem vindo(a) ao controle de estoque da bicicletaria! ---------------\n')

print(f'Vivian de Sousa Santana')

while True:
    # menu principal
    opcao_principal = input('Escolha a opção desejada:\n'+
                            '1-Cadastrar peça\n'+
                            '2-Consultar peça\n'+
                            '3-Remover peça\n'+
                            '4-Sair\n'+
                            '>> ')
    if opcao_principal == '1':
        print('\nVocê escolheu a opção cadastrar peça.')
        codigo_peca = codigo_peca +1
        cadastrar_peca(codigo_peca) # sempre que cadastrar_peca for invocada ela gera o código novo para a peça (como um contador).
    elif opcao_principal == '2':
        print('\nVocê escolheu a opção consultar peça.')
        consultar_peca()
    elif opcao_principal == '3':
        print('\nVocê escolheu a opção remover peça.')
        remover_peca()
    elif opcao_principal == '4':
        print('Encerrando sistema...')
        break
    else:
        print('Opção inválida! tente novamente.') # condição se o usuário digitar uma opção que não existe no menu.
        continue