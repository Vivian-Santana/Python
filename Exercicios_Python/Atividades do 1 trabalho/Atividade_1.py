print(f'Programa de cálculo de desconto de Vivian de Sousa Santana')

print('-------------------------------------------------------------------------')

# Entrada do valor unitário do produto
valor_produto = float(input('Digite o valor do produto: '))

# Entrada da quantidade do produto
quantidade_produto = int(input('Digite a quantidade do produto: '))
desconto_produto = 0

# Desconto de acordo com a quantidade
if quantidade_produto <= 9:
    desconto_produto = 0.00
    porcentagem_desconto = '0%'
elif (quantidade_produto >= 10) and (quantidade_produto <= 99):
    desconto_produto = 0.05
    porcentagem_desconto = '5%'
elif (quantidade_produto >= 100) and (quantidade_produto <= 999):
    desconto_produto = 0.10
    porcentagem_desconto = '10%'
else:
    desconto_produto = 0.15 # desconto a partir de 1000 unidades
    porcentagem_desconto = '15%'

# Cálculo do valor total sem desconto
total_sem_desconto = valor_produto * quantidade_produto
print('Valor total SEM desconto: R$ {:.2f}' .format(total_sem_desconto))

# Cálculo do valor total com desconto
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto_produto)
print('Valor total COM desconto: R$ {:.2f} ({} de desconto)' .format(total_com_desconto, porcentagem_desconto))
