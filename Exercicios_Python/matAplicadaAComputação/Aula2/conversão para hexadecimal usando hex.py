# usando a fução hex
numero=int(input('Digite um número inteiro: '))
print(f'O hexadecimal correspondete é: {hex(numero)}') # saída 0x indica a sequência hexadecimal
print(f'O hexadecimal correspondete é: {hex(numero)[2:]}')

# convesão contrária Convertendo um hexadecimal em decimal

# input do número hexadecimal
numero_hex = input('\nDigite um número hexadecimal: ')

# Use a função int() com base 2 para converter de hex para decimal
numero_decimal = int(numero_hex, 2)

# output do resultado
print(f'O número binário {numero_hex} em decimal é: {numero_decimal}')