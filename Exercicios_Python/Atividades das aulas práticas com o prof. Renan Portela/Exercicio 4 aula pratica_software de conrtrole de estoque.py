# Atividade prática com o prof Renan Portela Jorge - aula prática 6

# Início das variávies globais
lista_produto = []
codigo_produto = 0
# fim das variávies globais

# funções
def cadastrar_produto(codigo):
    print('Bem-vindo ao menu de cadastro de produtos!')
    print('Codigo do produto: {}'.format(codigo))
    nome = input('Digite o nome do produto: ')
    fabricante = input('Digite o fabricante do produto: ')
    preco = float(input('Digite o preço(R$) do produto: '))

    # dicionário das variáveis
    dicionario_produto = {'codigo'      : codigo,
                          'nome'        : nome,
                          'fabricante'  : fabricante,
                          'preço'       : preco}
    lista_produto.append(dicionario_produto.copy()) # inserindo o dicionário na lista

def consultar_produto():
    print('Bem-vindo ao menu de consulta de produtos!\n')
    while True:
        opcao_consultar = input('Escolha a opção desejada:\n'+
                                '1-Consultar todos os produtos\n'+
                                '2-Consultar produto por código\n'+
                                '3-Consultar produto(s) por fabricante\n'+
                                '4-Retornar\n'+
                                '>> ')
        # CONDIÇÃO CONSULTAR TODOS OS PRODUTOS
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar todos os produtos')
            # percorrendo a lista de produtos a variável produto é o iterador
            for produto in lista_produto: # produto vai varrer toda a lista de produtos
                print('-' * 20)
                # percorrendo um dicionário usando a chave e valor
                for key, value in produto.items(): # varrer todos os conjuntos chave e valor do dicionário produto.
                    print('{} : {}'.format(key, value))
                print('-' * 20)
        # CONDIÇÃO CONSULTAR POR CÓDIGO
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar produto por código')
            # acessar um produto específico
            valor_desejado = int(input('Digite o código desejado: '))
            # exceção para validar se o código existe
            try:
                produto_encontrado = next(produto for produto in lista_produto if produto['codigo'] == valor_desejado)
                print('-' * 20)
                for key, value in produto_encontrado.items():
                    print('{} : {}'.format(key, value))
                print('-' * 20)
            except StopIteration:
                print('Produto não encontrado!\n'+
                      'Ou o produto não existe ou foi removido.\n')
            
        # CONDIÇÃO CONSULTAR POR FABRICANTE
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar produto(s) por fabricante')
            valor_desejado = input('Digite o nome do fabricante desejado: ')
            
            produtos_encontrados = [produto for produto in lista_produto if produto['fabricante'] == valor_desejado]
        # condição que valida se o fabricante existe 
            if produtos_encontrados:
                for produto in produtos_encontrados:
                    print('-' * 20)
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('-' * 20)
            else:
                print('Nenhum produto encontrado para o fabricante especificado.\n')

        elif opcao_consultar == '4':
            return # sai da função consultar produto e volta para a main
        else:
            print('Opção inválida! tente novamente.')
            continue
#  FUNÇÃO REMOVER PRODUTO
def remover_produto():
    print('Bem-vindo ao menu de remoção de produtos!')
    valor_desejado = int(input('Digite o código do produto que deseja remover: '))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado:
            lista_produto.remove(produto)
            print('Produto removido com sucesso!')
 
# programa principal (main)
print('Bem vindo(a) a Mercearia!')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'+
                            '1-Cadastrar produto\n'+
                            '2-Consultar produto(s)\n'+
                            '3-Remover produto\n'+
                            '4-Sair\n'+
                            '>> ')
    if opcao_principal == '1':
        codigo_produto = codigo_produto +1
        cadastrar_produto(codigo_produto) # sempre que cadastrar_produto for invocada ela gera o código novo do produto (como um contador)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida! tente novamente.')
        continue