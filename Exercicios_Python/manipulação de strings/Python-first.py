'''
As funções incorporadas, ao contrário das funções definidas pelo usuário, estão sempre disponíveis e não precisam ser importadas.
Para chamar uma função (este processo é conhecido como chamada de função ou invocação de função), você precisa usar o nome da função seguido de parênteses. 
Você pode passar argumentos para uma função colocando-os dentro dos parênteses. Você deve separar os argumentos com uma vírgula, por exemplo, print("Olá,", "world!").
Um print() vazio imprime uma linha vazia na tela. 
O Python 3.8 vem com 69 funções integradas. Você pode encontrar a lista completa fornecida em ordem alfabética na Python Standard Library.
Strings no Python são delimitadas por aspas, por exemplo, "eu sou um barbante" (aspas duplas), ou 'eu sou um barbante, demasiado' (aspas simples).
Em Strings do Python a barra invertida (\) é um caracter especial que anuncia que o próximo caracter terá um significado diferente, por exemplo, 
\n (o caracter de nova linha) inicia uma nova linha de saída.
Argumentos posicionais são aqueles cujo significado é ditado por sua posição, por exemplo, o segundo argumento é gerado após o primeiro, o terceiro é gerado após o segundo, etc.
Argumentos de palavras-chave são aqueles cujo significado não é ditado por sua localização, mas por uma palavra especial (palavra-chave) usada para identificá-los.
Os parâmetros end e sep podem ser utilizadas para formatar a saída do print(). O parâmetro sep especifica o separador entre os argumentos de saída, por exemplo, 
print("H", "E", "L", "L", "O", sep="-"), enquanto o parâmetro end especifica o que imprimir no final da impressão.
'''

print("Hello world!")
print()
print("A pequenina aranha escalou a tromba d'água.")
print("Caiu a chuva e lavou a aranha.")
print()

print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")
print()

print("A aranha pequenininha\nsubiu a tromba d'água.\n")
print("abaixo veio a chuva\ne lavou a aranha.")
print()

print("A aranha pequenininha" , "subiu" , "a tromba d'água.")
print()

print("Meu nome é", "Python.")
print("Monty Python.")
print()

print("Meu nome é", "Python.", end=" ")
print("Monty Python.")
print()

print("Meu nome é ", end="")
print("Monty Python.")
print()

print("Meu", "nome", "é", "Monty", "Python.", sep="-")
print("Meu", "nome", "é", "Monty", "Python.", sep="❤️")
print()

print("Meu", "nome", "é", "Monty", "Python.", sep="-")
print()

print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print()

print("Programação","Essenciais","em", sep="***", end="...")
print("Python")

print("🤩" *2)
print ("aprendendo python \n" *2)
print()

print('oi')
print(" *")
print(" * *")
print(" * *")
print(" * *")
print("*** ***")
print(" * *")
print(" * *")
print(" *****")

print()

print("Meu\nnome\né\nBond.", end=" ")
print("James Bond.")
 
print()

print("peixe", "salgadinhos", sep="\t&\t")#Lembre-se: Os argumentos de palavras-chave devem ser passados após quaisquer argumentos posicionais obrigatórios.

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
#print('"Greg's book."') #A linha 5 gerará SyntaxError, porque o símbolo ' no Greg's book. string requer um caractere de escape.
print("\nliterais em Python.")

'''
Tomemos, por exemplo, o número onze milhões cento e onze mil cento e onze. Se você pegasse um lápis na mão agora, 
escreveria o número assim: 11,111,111, ou assim: 11.111.111, ou até mesmo assim: 11 111 111.

É claro que essa disposição facilita a leitura, especialmente quando o número consiste em muitos dígitos. 
No entanto, o Python não aceita coisas como essas. É proibido. O que o Python permite, porém, é o uso de sublinhados em literais numéricos.*

Portanto, você pode escrever este número da seguinte forma: 11111111 ou desta forma: 11_111_111.

Observação     *O Python 3.6 introduziu sublinhados em literais numéricos, permitindo a colocação de 
sublinhamentos únicos entre dígitos e especificadores de base para melhorar a legibilidade. 
Esse recurso não está disponível em versões mais antigas do Python.

E como codificamos números negativos em Python? Como de costume - adicionando um sinal de menos. 
Você pode escrever: -11111111 ou -11_111_111.

Os números positivos não precisam ser precedidos pelo sinal de mais, mas é permitido, se você quiser fazer isso. 
As seguintes linhas descrevem o mesmo número: +11111111 e 11111111.
 
Números octais e hexadecimais:
Há duas convenções adicionais em Python que são desconhecidas para o mundo da matemática. 
A primeira nos permite usar números em uma representação octal.

Se um número inteiro for precedido por um prefixo 0O ou 0o (zero-o), ele será tratado como um valor octal. 
Isso significa que o número deve conter dígitos retirados apenas do intervalo [0..7].

0o123 é um número octal com um valor (decimal) igual a 83.
'''

# A função print() faz a conversão automaticamente. Tente isto:
print(0o123)

print()
'''
A segunda convenção nos permite usar números hexadecimais. Esses números devem ser precedidos pelo prefixo 0x ou 0X (zero-x).
0x123 é um número hexadecimal com um valor (decimal) igual a 291. A função print() também pode gerenciar esses valores. Tente isto:
'''
print(0x123)
print("\nPonto flutuante")
'''
Nota: dois e meio parecem normais quando você o escreve em um programa, embora se o seu idioma nativo preferir usar vírgula 
em vez de um ponto no número, você deve garantir que seu número não contenha nenhuma vírgula.

O Python não aceitará isso, ou (em casos muito raros, mas possíveis) pode interpretar mal suas intenções, 
pois a própria vírgula tem seu próprio significado reservado em Python.
'''
print(2.5)
print()
'''
# Por outro lado, não são apenas os pontos que fazem um float. Você também pode usar a letra e.

# Quando você quiser usar números muito grandes ou muito pequenos, use notação científica.

# Veja, por exemplo, a velocidade da luz, expressa em metros por segundo. Escrito diretamente, ficaria assim: 300000000.

# Para evitar escrever tantos zeros, os livros de física usam uma forma abreviada, que você provavelmente já viu: 3 x 108.

# Diz: Três vezes dez à potência de oito.

# Em Python, o mesmo efeito é obtido de uma maneira ligeiramente diferente - veja:

# 3E8

# A letra E (você também pode usar a letra minúscula e - vem da palavra expoente) é um registro conciso da frase vezes dez à potência de.
'''

'''
# Nota:
# o expoente (o valor após o E) tem que ser um número inteiro;
# a base (o valor na frente do E) pode ser um número inteiro ou um valor flutuante.
'''
print(3e8)
print()
'''
Codificação de flutuantes
Vamos ver como essa convenção é usada para registrar números muito pequenos (no sentido de seu valor absoluto, que é próximo de zero).

Uma constante física chamada constante de Planck (e indicada como h), de acordo com os livros didáticos, tem o valor de: 6,62607 x 10-34.

Se você gostaria de usá-lo em um programa, escreva desta forma:

6.62607E-34

Nota: o fato de você ter escolhido uma das formas possíveis de codificação de valores flutuantes não significa que o Python a apresentará da mesma forma.

Às vezes, o Python pode escolher uma notação diferente da sua.

Por exemplo, digamos que você decidiu usar o seguinte literal de flutuação:

0.0000000000000000000001

Quando você executa esse literal pelo Python:
'''
print(0.0000000000000000000001)

'''
Output
esse é o resultado:
1e-22
Output
O Python sempre escolhe a forma mais econômica de apresentação do número, e você deve levar isso em consideração ao criar literais.
'''
print()
#ADS aula 2 tema 4: manipulação avançada com strings
print('*** Manipulação de strings ***')
print('Concatenando strings:')
s1 = 'Logica de programação'
s1 = s1 + ' e Algoritmos'
print(s1)

print()

string = 'A' + '-' * 10 + 'B' # multiplicar a '-' por 10 vai imorimir - dez vezes.
print(string)
print()

print('Composição = juntar string com variáveis:')
nota = 8.5
s3 = 'Voce tirou %f na disciplina de Algoritmos' % nota
print(s3)

#limitando as casas decimais q aparecem depois do 5
nota = 8.5
s4 = 'Voce tirou %.2f na disciplina de Algoritmos' % nota
print(s4)

print()

print('concatenação com várias variáveis:')
nota = 8.5
disciplina = 'Algoritmos'
s5 = 'Voce tirou %.1f na disciplina de %s' % (nota, disciplina)
print(s5)

print()

print ('composição moderna:')
nota = 8.5
disciplina = 'Algoritmos'
s6 = 'Voce tirou {} na disciplina de {}' .format(nota, disciplina)
print(s6)

print()

print('Fatiamento de string:')
s7 = 'Lógica de programação e algoritmos'
print(s7[0:6])# essa delimitação pega do caractere 0 até o 5.
print(s7[24:34])
print(s7[:6]) # se não colocar um delimitador antes dos : ele vai pegar td a partir do início até onde delimitei o fim.

print()

print('Tamanho (length):') # saber o tamanho da string
s8 = 'Lógica de programação e algoritmos'
tamanho = len(s8)
print(tamanho)

'''
tema 5: Função de entrada e fluxo de execução do programa
idade = input('Qual sua idade?')
print(idade)

print()

nome = input('Qual é o seu nome?')
print('Olá {}, seja bem-vindo(a)!'.format(nome))

print()
print('Convertendo dados de entrada:')
nota2 = float(input('Qual nota você recebeu na disciplina? '))
print('Você tirou a nota {}.' .format(nota2))
'''
print()
#Exercicio
x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
print('\n Maneira clássica:')
res = 'O resultado da soma de %i com %i é %i.' % (x, y, x+y)
print(res)

print()
print('Maneira moderna:')
res = 'O resultado da soma de {} com {} é {}.' .format(x, y, x+y)
print(res)

print()
