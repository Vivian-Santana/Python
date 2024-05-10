'''
11. A criptografia é uma técnica de codificar e decodificar mensagens de modo a
dificultar o acesso ao conteúdo da mensagem por pessoas não autorizadas. Uma
cifra bastante famosa e que foi criada há séculos é a Cifra de César. Considerando
a substituição de cada letra do alfabeto original por outra letra três posições à frente
(substituir a letra A pela letra D, a letra B pela letra E e assim por diante) obtenha a
respectiva forma criptografada da mensagem: “ENTENDIDO”.
'''

from string import ascii_uppercase
a=list(ascii_uppercase)
m=input('Digite a mensagem: ')
m=m.upper()
mc=""
for l in m:
 i=ord(l)-65
 if l in a:
   mc+=a[(i+3)%26]
 else:
  l
print(f'\n11) Mensagem criptografada: {mc}')
