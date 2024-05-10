'''
Exercicios da aula prática 3

Escreva as seguintes expressões booleanas:
a) o somatório de 2 com 2 é menor do que 4;
b) o valor 7 // 3 é igual a 1 + 1;
c) a soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25;
d) a soma de 2, 4 e 6 é maior do que 12;
e) 1387 é divisível por 19;
f) 31 é par;
g) o menor valor entre: 34, 29 e 31 é menor do que 30.
'''

print('a)', 2 + 2 < 4 ,'\n')

print('b)', 7 // 3 == 1 + 1 ,'\n')

print('c)', 3 ** 2 + 4 ** 2 == 25 ,'\n')

print('d)', 2 + 4 + 6 > 12 ,'\n')

print('e)', 1387 % 19 == 0 ,'\n')

print('f)', 31 % 2 == 0 ,'\n')

print('g)', min (34, 29, 31) < 30, '\n')

'''
Traduza as afirmações a seguir para condicionais:

a) Se idade é maior que 60, escreva: "Você tem direito aos benefícios";
b) Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto";
c) se pelo menos uma das variáveia booleanas norte, sul, leste e oeste resultarem em "true", escreva: "Você escapou" 
'''

print('*** Condicionais simples ***\n')

idade = int(input('a) Digite sua idade: '))
if idade > 60:
    print('Você tem direito aos benefícios.')
else:
    print('Você não tem direito aos benefícios.')

print('---------------------------------------------------------------------------')

dano = int(input('b) Digite o valor do dano: '))
escudo = int(input('Digite o valor do escudo: '))
if (dano > 10) and (escudo == 0):
    print('☠️ Você está morto!')

print('---------------------------------------------------------------------------')

coordenada = input('Digite sua coordenada: ')
if('norte' or 'sul' or 'leste' or 'oeste'):
    print('🫡Você escapou!🎉')

print('---------------------------------------------------------------------------')

print('*** Condicional composta ***\n')

'''
Traduza as afirmações a seguir para condicionais em python:

a) se ano é divisível por 4, escreva: "Pode ser um ano bissexto". 
Caso contrário, escreva: "Definitivamente não é um ano bissexto".

b) se ambas as variáveis booleanas "cima" e "baixo" forem True, escreva: "Decida-se!"
caso contrário, escreva:"Você escolheu um caminho!"
'''
16
ano = int(input('Digite um ano: '))
if(ano % 4 == 0):
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto')

print('---------------------------------------------------------------------------')

cima = input("Você quer ir para cima? (Digite 'sim' ou 'não'): ").lower() == 'sim'  # convertemos a entrada para minúsculas usando o método lower() e comparamos com a 
baixo = input("Você quer ir para baixo? (Digite 'sim' ou 'não'): ").lower() == 'sim' # string "sim" para atribuir os valores booleanos às variáveis cima e baixo.

if cima and baixo:
    print("Decida-se!")
else:
    print("Você escolheu um caminho!")
