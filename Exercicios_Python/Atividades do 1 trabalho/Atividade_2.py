print(f'Programa app de vendas para uma lanchonete de Vivian de Sousa Santana')

print('___________________ Cardápio ______________________')
print('|  código   |      Descrição        |  Valor (R$) |')
print('|-------------------------------------------------|')
print('|    100    |    Cachorro-Quente    |   R$ 9,00   |')
print('|    101    | Cachorro-Quente Duplo |   R$ 11,00  |')
print('|    102    |         X-Egg         |   R$ 12,00  |')
print('|    103    |        X-Salada       |   R$ 13,00  |')
print('|    104    |        X-Bacon        |   R$ 14,00  |')
print('|    105    |        X-Tudo         |   R$ 17,00  |')
print('|    200    |   Refrigerante Lata   |   R$ 5,00   |')
print('|    201    |      Chá Gelado       |   R$ 4,00   |')
print('|___________|_______________________|_____________|\n')

acumulador = 0 # variável que tem a função de iterar valores

while True:
    # Entrando com o pedido
    codigo = input('Digite o código do item que deseja pedir: ')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Opção inválida! Para continuar digite um código válido.\n')
        continue # se o usuário digitar algo inválido volta para o início do while.
    
    # opções de pedidos
    elif codigo == '100':
        print('Cachorro-Quente - R$ 9,00 adicionado a seu pedido.')
        acumulador += 9.00
    
    elif codigo == '101':
        print('Cachorro-Quente duplo - R$ 11,00 adicionado a seu pedido.')
        acumulador += 11.00

    elif codigo == '102':
        print('X-Egg - R$ 12,00 adicionado a seu pedido.')
        acumulador += 12.00

    elif codigo == '103':
        print('X-Salada - R$ 13,00 adicionado a seu pedido.')
        acumulador += 13.00

    elif codigo == '104':
        print('X-Bacon - R$ 14,00 adicionado a seu pedido.')
        acumulador += 14.00

    elif codigo == '105':
        print('X-Tudo - R$ 17,00 adicionado a seu pedido.')
        acumulador += 17.00

    elif codigo == '200':
        print('Refrigerante Lata - R$ 5,00  adicionado a seu pedido.')
        acumulador += 5.00

    elif codigo == '201':
        print('Chá Gelado - R$ 4,00 adicionado a seu pedido.')
        acumulador += 4.00

    continuar_pedindo = input('\nDeseja algo mais? (S | N) ').upper()
    if continuar_pedindo == 'S':
        print()
        continue
    # valor total do pedido
    else:
        print('\nTotal a pagar: R$ {:.2f}'.format(acumulador))
        print('\nSeu pedido está sendo preparado, você será avisado quando estiver a caminho.','\nAgradecemos pela preferência! volte sempre!')
        break
