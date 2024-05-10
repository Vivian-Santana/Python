'''
2. Um dos primeiros algoritmos destinados à criptografia de mensagens foi a Cifra
de César. É um algoritmo simples baseado na substituição de letras por outras a
partir de uma troca de posições. Utilizando uma troca pela letra que está quatro
posições à frente, temos que a letra “a” é substituída pela letra “e”, a letra “b” é
substituída pela letra “f” e assim por diante. Considerando a mensagem “MAIS
AMOR”, por meio do Python, qual é a respectiva forma criptografada utilizando a
Cifra de César com a substituição descrita acima?
'''
from string import ascii_uppercase
# algoritmo de codificação
a= list(ascii_uppercase) # a recebe a lista com tds os codigos da tabela asc A esta associado a 65, b -> 66, c -> 67 ...
m= input('Digite a mensagem: ') # m recebe a mensagem
m= m.upper() # converte a msg para maúscula
mc= "" # recebe a msg cifrada
for l in m: # l serve como contador
 i=ord(l)-65 # i recebe o código em asc e subtrai 65, pq o primeiro valor é o 65 associado a letra A convertendo tbm as letras seguintes. 
 if l in a: # se as letras na variávrl "l" estão no conjunto "a"
   mc += a[(i+4)%26] # a mc (msg cifrada) recebe o valor associado a "a" e faz a mudança do num associado a letra + 4. divide por % de 26 q é a quant. de letras do alfabeto.
else:
 l   # se tiver um caracter na msg q não esteja na tabela asc mantemos o caracter q foi colocado na msg.
print(f'Mensagem criptografada: {mc}')

'''
4. Um dos primeiros algoritmos destinados à criptografia de mensagens foi a Cifra
de César. É um algoritmo simples baseado na substituição de letras por outras a
partir de uma troca de posições. Utilizando uma troca pela letra que está quatro
posições à frente, temos que a letra “a” é substituída pela letra “e”, a letra “b” é
substituída pela letra “f” e assim por diante. Considerando a mensagem
criptografada “IRXIRHMQIRXS”, utilizando o Python, qual é a mensagem original
utilizando a Cifra de César com a substituição descrita acima?
'''
from string import ascii_uppercase
a= list(ascii_uppercase)
mc= input('Digite a mensagem criptografada: ') # IRXIRHMQRXS
mc= mc.upper()
m=""
for l in mc:
  i=ord(l)-65
  if l in a:
    m+=a[(i-4)%26]
else:
 l
print(f'Mensagem original: {m}')

'''
7. Na criptografia RSA (Rivest-Shamir-Adleman), as letras são substituídas por
números de dois dígitos. O Python possui uma biblioteca destinada à criptografia
RSA. Uma possibilidade de sequência de comandos para cifrar e decifrar uma
mensagem utilizando a criptografia RSA por meio do Python é:
'''
import rsa

# codificação
chavepublica,chaveprivada=rsa.newkeys(512)
m=input('Digite a mensagem: ')
mc=rsa.encrypt(m.encode(),chavepublica)
print("Mensagem original:", m)
print("Mensagem criptografada:", mc)

# decodificação
md=rsa.decrypt(mc,chaveprivada).decode()
print("Mensagem descriptografada:", md)
chavepublica,chaveprivada=rsa.newkeys(512)
m=input('Digite a mensagem: ')
mc=rsa.encrypt(m.encode(),chavepublica)
print("Mensagem original:", m)
print("Mensagem criptografada:", mc)
