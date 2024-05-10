'''
Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
Armazene os dados em um dicionário com listas. Ao encerrar o cadastro, apresente:
O total de cadastros efetuados;
A média das idades das pessoas;
Uma lista de mulheres com menos de 30 anos;
Uma lista de homens com idade acima da média.
'''
import datetime

print('Entre com seus dados pessoais:')
    # Dicionário para armazenar os dados das pessoas
cadastro = {
    'nomes':[], 
    'ano_nascimento': [],
    'sexo': []
}

# Função para calcular a idade com base no ano de nascimento
def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# Loop para realizar o cadastro das pessoas
while True:
    nome = input("\nNome completo (ou '0' para encerrar): ")
    
    if nome == '0':
        break
    ano_nascimento = int(input("Ano de nascimento: "))
    sexo = input("sexo (M para masculino, F para feminino, NB para não binário): ").lower()
    
    cadastro['nomes'].append(nome)
    cadastro['ano_nascimento'].append(ano_nascimento)
    cadastro['sexo'].append(sexo)

# Total de cadastros efetuados
total_cadastros = len(cadastro['nomes'])
print("\nTotal de cadastros efetuados:", total_cadastros)

# Cálculo da média das idades
idades = [calcular_idade(ano) for ano in cadastro['ano_nascimento']]
media_idades = sum(idades) / len(idades)
print("Média das idades das pessoas:", media_idades)

'''
Lista de mulheres com menos de 30 anos
mulheres_menos_30 = [nome for nome, ano, sexo in zip(cadastro['nomes'], cadastro['ano_nascimento'], cadastro['sexo']) if sexo == 'F' and calcular_idade(ano) < 30]
print("Lista de mulheres com menos de 30 anos:", mulheres_menos_30)# lista não está retornando
'''

mulheres_menos_30 = [cadastro['nomes'][i] for i in range(len(cadastro['nomes'])) if cadastro['sexo'][i] == 'F' and calcular_idade(cadastro['anos_nascimento'][i]) < 30]
print("Lista de mulheres com menos de 30 anos:", mulheres_menos_30)

'''
Lista de homens com idade acima da média
homens_acima_media = [nome for nome, ano, sexo in zip(cadastro['nomes'], cadastro['ano_nascimento'], cadastro['sexo']) if sexo == 'M' and calcular_idade(ano) > media_idades]
print("Lista de homens com idade acima da média:", homens_acima_media) # lista não está retornando
'''

homens_acima_media = [cadastro['nomes'][i] for i in range(len(cadastro['nomes'])) if cadastro['sexo'][i] == 'M' and calcular_idade(cadastro['anos_nascimento'][i]) > media_idades]
print("Lista de homens com idade acima da média:", homens_acima_media)

'''
Neste código, utilizei a biblioteca datetime para obter o ano atual e calcular a idade com base no 
ano de nascimento. Os dados das pessoas são armazenados em um dicionário chamado cadastros, onde cada 
chave representa um campo (nomes, anos_nascimento, sexos) e o valor associado a cada chave é uma lista 
que armazena os respectivos dados. 
Durante o cadastro das pessoas, você pode digitar "0" como nome para encerrar o cadastro.
No final do programa, são apresentados o total de cadastros efetuados, a média das idades das pessoas, 
uma lista de mulheres com menos de 30 anos e uma lista de homens com idade acima da média.
'''