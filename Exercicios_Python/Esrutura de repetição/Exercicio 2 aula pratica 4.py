'''
Leia um valor e imprima a quantidadde de células necessárias para pagar esse mesmo valor.
Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, 50, 20, 10, 5 e 1.
'''

print('Caixa eletrônico')
valor = int(input('Digite um valor em R$ '))

while True:
    if valor >= 100:
        cedulas100 = valor //100 # divisão pegando só a parte intiera
        valor -= cedulas100 * 100
        print('Cedulas de 100:{}'.format(cedulas100))
        if not valor: # caso digite 500 a variável valor ao sair da linha vai receber o valor 0,
            break       # o if vai dar verdadeiro e o break encerra o laço. sendo desnecessário os outros ifs serem executados.
    if valor >= 50:
        cedulas50 = valor //50 # divisão pegando só a parte intiera
        valor -= cedulas50 * 50
        print('Cedulas de 50:{}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor //20 # divisão pegando só a parte intiera
        valor -= cedulas20 * 20
        print('Cedulas de 20:{}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor //10 # divisão pegando só a parte intiera
        valor -= cedulas10 * 10
        print('Cedulas de 10:{}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor //5 # divisão pegando só a parte intiera
        valor -= cedulas5 * 5
        print('Cedulas de 5:{}'.format(cedulas5))
        if not valor:
            break
    if valor:
        cedulas1 = valor
        print('Cedulas de 1:{}'.format(cedulas1))
        break