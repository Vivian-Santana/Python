'''
Exercici 4 aula 1
Para a liberação de um financiamento imobiliário, uma construtora exige que a
renda mensal líquida mínima seja maior ou igual a R$ 8.500,00 e que o total de
comprometimento com outros financiamentos ou empréstimos não ultrapasse 20%
da renda mensal líquida. Utilizando o Python, faça um programa que informe se o
financiamento será liberado ou não com base na renda mensal líquida e no total de
outros financiamentos ou empréstimos por parte do cliente.
'''
renda_mensal_liquida = float(input('Digite a renda mensal líquida: '))
total_financiamentos = float(input('Digite o total de comprometimento com outros financiamentos ou empréstimos: '))

# calculo de 20% da renda 
vinte_porcento = renda_mensal_liquida * 0.20

if renda_mensal_liquida >= 8500 and total_financiamentos <= vinte_porcento:
    print('Financiamento liberado!')
else:
    print('Financiamento negado.')

# ou
'''
R=float(input('Renda mensal líquida: '))
F=float(input('Financiamentos ou empréstimos: '))

if R>=8500 and F<=0.2*R: # o calculo de 20% da renda pode ser feito dentro da condicional (na segunda proposição) sem precisar ser armazenado em uma variável.
    print('Financiamento aprovado')
else:
    print('Financiamento não aprovado')
'''