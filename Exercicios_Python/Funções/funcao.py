'''
Aula 05 tema 1

sintaxe da função
def realce():
    corpo da função
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')

invocando a função (executando da classe principal)
realce()
print('         MENU')
realce()
'''

# Parâmetros e passagem de parâmetros
def realce_01(s1):
    #corpo da função
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
    print(s1)
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
print('------------------------')    
# invocando a função  por passagem de parâmetro
realce_01 ('        Vivian') # a string entra em s1

# passando mais de um parâmetro
def sub2(x, y):
    res = x -y
    print(res)

# invocação da função
sub2(5, 7)

sub2 (y = 5, x = 7) # explicitando q cada variável vai receber o valor q eu quero ao invés de seguir o padrão da ordem dos dados dentro do parâmetro.

print('------') 
# parâmetros opcionais.
def soma3(x,y,z):
    res = x + y + z
    print(res)
# invocação da função
def soma3(x = 0, y = 0, z = 0): # cabeçalho da função
    res = x + y + z
    print(res)

# exemplos
soma3(1,2,3)
soma3(1,2) # z foi omitido
soma3(1)   # y e z foram omitidos
soma3()    # x, y e z foram omitidos

def borda(s1):
    tam = len(s1) # pegando o tamanho da string com len()
    # só imprime caso exista algum caractere
    if tam: # Truthy/True: qualquer valor q for inteiro, númérico e não for 0 pode ser tratado como true.
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+','-' * tam, '+')

# classe de execução do programa
borda('Olá, Mundo!')
borda('Lógica de programação e Algoritmos')