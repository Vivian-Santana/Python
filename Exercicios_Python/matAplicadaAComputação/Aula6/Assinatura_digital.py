'''
from hashlib import sha256
from random import Random
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

semente=Random.new().read
chaves=RSA.generate(1024,semente)
publica=chaves.publickey()
texto1='Estudo Java'
texto2='Estudo Python'

hash1=SHA256.new(texto1.encode('utf-8')).digest()
assinatura=chaves.sign(hash1, '')
print('Hash 1: '+repr(hash1))
print('Assinatura Digital: '+repr(assinatura))

# criação do hash
hash2=SHA256.new(texto1.encode('utf-8')).digest()
hash3=sha256.new(texto2.encode('utf-8')).digest()
print('Hash 2: '+repr(hash3))
print('Hash 3: '+repr(hash3))

# verificação da assinatura
if(publica.verify(hash, assinatura)):
    print('Texto verdadeiro: '+texto1)
elif(publica.verify(hash3,assinatura)):
    print('Texto verdadeiro: '+texto2)
'''

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
# from Crypto.Hash import SHA256

#Gerar as chaves pública e privada nos arquivos "destinatario.pem" e "chavePrivada.pem", respectivamente:
chaves = RSA.generate(1024)
chavePrivada = chaves.export_key()
arquivoDeSaida=open("chavePrivada.pem", "wb")
arquivoDeSaida.write(chavePrivada)
arquivoDeSaida.close()

chavePublica= chaves.publickey().export_key()
arquivoDeSaida=open("destinatario.pem", "wb")
arquivoDeSaida.write(chavePublica)
arquivoDeSaida.close()

#Cifrar o texto "Estudo Python." utilizando chave da sessão cifrada com chave pública RSA:
texto = 'Estudo Python'.encode('utf-8')
arquivoDeSaida=open("textoCifrado.bin", "wb")

chaveDoDestinatario=RSA.import_key(open("destinatario.pem").read())
chaveDaSessao=get_random_bytes(16)

#Cifrar a chave da sessão com a chave pública RSA
cifraRSA=PKCS1_OAEP.new(chaveDoDestinatario)
chaveEncaminhadaDaSessao=cifraRSA.encrypt(chaveDaSessao)

#Cifrar o texto com a chave da sessão:
cifraAES=AES.new(chaveDaSessao, AES.MODE_EAX)
textoCifrado, tag = cifraAES.encrypt_and_digest(texto)
[arquivoDeSaida.write(x) for x in (chaveEncaminhadaDaSessao, cifraAES.nonce, tag, textoCifrado)]
arquivoDeSaida.close()

#Destinatário possui a chave privada RSA para ler o texto:
arquivoDeEntrada=open("textoCifrado.bin", "rb")

chavePrivada=RSA.import_key(open("chavePrivada.pem").read())

chaveEncaminhadaDaSessao, nonce, tag, textoCifrado = \
[arquivoDeEntrada.read(x) for x in (chavePrivada.size_in_bytes(), 16, 16, -1)]
arquivoDeEntrada.close()

#Decodificar a chave da sessão com a chave privada RSA:
cifraRSA=PKCS1_OAEP.new(chavePrivada)
chaveDaSessao=cifraRSA.decrypt(chaveEncaminhadaDaSessao)

#Decodificar o texto com a chave da sessão:
cifraAES=AES.new(chaveDaSessao, AES.MODE_EAX, nonce)
texto=cifraAES.decrypt_and_verify(textoCifrado, tag)
print(texto.decode("utf-8"))
