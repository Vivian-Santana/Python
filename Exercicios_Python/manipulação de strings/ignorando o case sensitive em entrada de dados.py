'''
o programa solicita ao usuário uma entrada em letras minúsculas, mas 
é capaz de lidar com entradas em letras maiúsculas sem gerar erros:
'''

entrada = input("Digite uma palavra em letras minúsculas: ")
entrada_min = entrada.lower()  # Converte a entrada para minúsculas

# Verifica se a entrada está em minúsculas
if entrada == entrada_min:
    print("Entrada correta:", entrada)
else:
    print("Entrada convertida para minúsculas:", entrada_min)

'''
Neste exemplo, o programa solicita ao usuário uma palavra em letras minúsculas. Em seguida, a entrada é convertida para minúsculas usando o método lower(). 
Depois disso, é feita uma verificação para determinar se a entrada original é igual à versão convertida para minúsculas.
Se o usuário digitar a entrada em letras minúsculas, o programa imprimirá "Entrada correta" junto com a entrada original. 
Caso o usuário digite a entrada em letras maiúsculas, o programa imprimirá "Entrada convertida para minúsculas" seguido da versão convertida em minúsculas da entrada.
Dessa forma, o programa consegue lidar com entradas em diferentes casos sem gerar erros e permite que você compare as entradas ignorando o case sensitive.
'''

#Agora veja o contrário
entrada = input("Digite uma palavra em letras mainúsculas: ")
entrada_mai = entrada.upper()  # Converte a entrada para mainúsculas

# Verifica se a entrada está em mainúsculas
if entrada == entrada_mai:
    print("Entrada correta:", entrada)
else:
    print("Entrada convertida para minúsculas:", entrada_mai)

# uma forma de fazer é colocar após o parâmetro de entrada ex.
tamanho = input('Digite o tamanho da pizza desejada (M | G): \n').upper() # mesmo se o usuári digitar letra minuscula o upper vai ignorar.

# outra forma é declarar a variável como upper ou lower exemplo
tamanho = tamanho.upper()