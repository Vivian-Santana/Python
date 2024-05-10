# função
def comida():
    print(ovos)

# classe principal (de execução)
ovos = 12 # variavel de escopo global
comida() # função

print('------------------------')

def comida2():
    ovos2 = 12 # variavel ovos2 é local
    bacon()
    print(ovos)

def bacon():
    ovos2 = 6 # diferente da variável ovos2 de cima. Tanto que o print que esta sendo feito é da variável ovos2 de cima.

# classe principal
comida2()

print('------------------------')

def comida3():
    chocolate = '2° print: variável local de comida' # quando criamos uma variavel local com o mesmo nome de uma variável global o q passa a valer dentro do escopo dessa primeira é a variável local.
    print(chocolate)

def sorvete():
    chocolate = '1° print: variável local de sorvete' # 1° print
    print(chocolate)
    comida3()
    print(chocolate) # print 3°de chocolate dentro da função sorvete a variável q vale é a q está dentro da função sorvete q vai printar a string 1°.

# Classe principal
chocolate = '4° print: Variável global' # print 4°
sorvete()
print(chocolate)
print('-----------------------')
'''
Instrução global
força o programa a não criar uma variável de mesmo 
nome e manipular somente a global dentro de uma função
'''
def comida4():
    global batata_frita # alterando a vairável batata frita "dizendo" q ela é global daí eu altero tbm o valor da variável da classe principal. 
    '''
    Global passa a receber o valor da string q está sendo passada aqui localmente.
    a única maneira de alterar uma variável global, sem criar uma nova vairável de mesmo nome no escopo local, 
    é usar a palavra global antes da variável q quero alterar o valor.
    '''
    batata_frita = 'foi alterado o valor da variável' # a vairável local só pode ser alterada localmente.

# Classe main
batata_frita = 'é uma variável global' # a variável global pode ser alterada no escopo de uma função escopo local
comida4()
print(batata_frita)
