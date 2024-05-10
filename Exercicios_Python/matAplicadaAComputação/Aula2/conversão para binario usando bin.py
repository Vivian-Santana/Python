# usando a fução bin
numero=int(input('Digite um número inteiro: '))
print(f'O binário correspondete é: {bin(numero)}') # 0b na saída indica a sequência binária
print(f'O binário correspondete é: {bin(numero)[2:]}') # forma formatada sem aparecer o 0b

# convesão contrária Convertendo um Hexadecimal em Decimal

# input do número binário
numero_binario = input('\nDigite um número binário: ')

# Use a função int() com base 16 para converter de binário para decimal
numero_decimal = int(numero_binario, 16)

# output do resultado
print(f'O número binário {numero_binario} em decimal é: {numero_decimal}')
