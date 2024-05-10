'''
Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
Armazene os dados em um dicionário com listas. Ao encerrar o cadastro, apresente:
O total de cadastros efetuados;
A média das idades das pessoas;
Uma lista de mulheres com menos de 30 anos;
Uma lista de homens com idade acima da média.
''' 

# Dicionário para armazenar os dados das pessoas
cadastro = {'nome':[],'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastrar uma pessoa? (S | N): ').upper()
    if terminar in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite "S" para sim ou "N" para Não')

    nome = input('\nQual é o seu nome? ')
    sexo = input('Qual é o seu sexo? ')
    ano = int(input('Qual é o seu ano de nascimento? '))
    # apêndice
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)
    continue
print(cadastro)

