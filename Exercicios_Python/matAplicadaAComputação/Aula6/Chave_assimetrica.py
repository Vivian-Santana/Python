import rsa

chavepublica,chaveprivada=rsa.newkeys(512)
m= input('Digite a mensagem: ')
mc= rsa.encrypt(m.encode(),chavepublica)
print("Mensagem original:", m)
print("Mensagem criptografada:", mc)
md= rsa.decrypt(mc,chaveprivada).decode()
print("Mensagem descriptografada:", md)
