'''
aula 5 tema 5
tratamento de excessões:
exemplo de excessão
100 * (2/0) # excessão de ZeroDivisionError = erro de divisão por zero

while True:
     try:
         x = int(input('Por favor digite um número:'))
         break
     except ValueError:
         print('Oops! número inválido. Tente novamente...')
'''

print()

def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')

# programa principal
print(div ())