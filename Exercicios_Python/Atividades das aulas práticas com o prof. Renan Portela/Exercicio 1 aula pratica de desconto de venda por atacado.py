# atividade prática com o prof Renan Portela Jorge - aula prática 1.

print('Bem vindo a loja da Vivi!') # não esquecer desse identificador.

valor_produto = float(input('Digite o valor desejado: '))
qtd_produto = int(input('Digite a quantidade desejada: '))
desconto_produto = 0

# teste em cima da variável quantidade
if qtd_produto <= 4:
    desconto_produto = 0.00 # sem desconto
elif (qtd_produto >= 5) and (qtd_produto < 20):
    desconto_produto = 0.03 # desconto de 3%

elif (qtd_produto >= 20) and (qtd_produto < 100):
    desconto_produto = 0.06 # desconto de 6%
else:
    desconto_produto = 0.10 # desconto de 10%
print(desconto_produto)

total_sem_desconto = valor_produto * qtd_produto
print('O valor total sem desconto é de: R$ {:.2f}' .format(total_sem_desconto))
# print(f'O valor toal sem desconto é de: R$ {total_sem_desconto}') # fstring maneira mais nova de fazer mas não tem nas versões mais antigas de python.
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total com desconto é de: R$ {:.2f}' .format(total_com_desconto))
