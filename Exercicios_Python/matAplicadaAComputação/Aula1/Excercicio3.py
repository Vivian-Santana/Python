'''
Exercicio 3 aula 1
Em uma empresa, a entrada em um determinado setor é liberada após o
funcionário digitar uma determinada senha. Sabendo que a senha é 705080, faça
um programa em Python onde o usuário digita uma senha. Se a senha estiver
correta, aparece a mensagem que a entrada está liberada. Caso contrário, a
mensagem é de que a entrada não está autorizada.
'''
senha = int(input ('Digite a senha: '))

if senha == 705080:
    print('A entrada está liberada!')
else:
    print('Entrada não autorizada.')