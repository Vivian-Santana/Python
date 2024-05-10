'''
Um aluno para passar de ano precisa ser aprovado em todas as matérias que está cursando
assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não
'''

materia1 = float (input('Digite a nota da 1ª matéria: '))
materia2 = float (input('Digite a nota da 2ª matéria: '))
materia3 = float (input('Digite a nota da 3ª matéria: '))

if (materia1 >= 7 and materia2 >= 7 and materia3 >=7):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')