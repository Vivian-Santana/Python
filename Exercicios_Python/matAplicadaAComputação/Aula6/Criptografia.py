from string import ascii_uppercase
# algoritmo de codificação
# CIFRA DE CÉSAR
a= list(ascii_uppercase)
m= input('Digite a mensagem: ')
m= m.upper()
mc= ""
for l in m:
 i=ord(l)-65
 if l in a:
   mc += a[(i+3)%26]
else:
 l
print(f'Mensagem criptografada: {mc}')

# algoritmo de decodificação

a= list(ascii_uppercase)
mc= input('Digite a mensagem criptografada: ')
mc= mc.upper()
m= ""
for l in mc:
 i=ord(l)-65
 if l in a:
   m+=a[(i-3)%26]
else:
 l
print(f'Mensagem original: {m}')