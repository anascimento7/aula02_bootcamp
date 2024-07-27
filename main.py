# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# CONSTANTE_FAHRENHEIT = 32

# try:
#     celsius = float(input('Digite a temperatura em Celsius: '))

#     temp_fahrenheit = (celsius * (9 / 5)) + CONSTANTE_FAHRENHEIT

#     print(f"{celsius}°C é igual a {temp_fahrenheit}°F")
# except ValueError:
#     print("Erro: Digite uma temperatura válida")
# except EOFError:
#     print("Você está saindo do programa")


# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
# import string

# texto = input('Digite algum texto: ')

# if isinstance(texto, str):
#     texto_sem_pontuacao = texto.translate(str.maketrans('','', string.punctuation))
#     texto_reverso = texto_sem_pontuacao[::-1]
#     if texto_sem_pontuacao.lower() == texto_reverso.lower():
#         print("É um palindromo")
#     else:
#         print("Não é um palindromo")
# else:
#     print("Você não digitou uma string")
    

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     num_1 = float(input('Digite um número: '))
#     num_2 = float(input('Digite outro número: '))
#     operador = input('Digite a operação que deseja realizar (+, -, *, /): ')

#     if operador == '+':
#         print(f"{num_1} + {num_2} = {num_1 + num_2}")
#     elif operador == '-':
#         print(f"{num_1} - {num_2} = {num_1 - num_1}")
#     elif operador == '*':
#         print(f"{num_1} * {num_2} = {num_1 * num_1}")
#     elif operador == '/':
#         print(f"{num_1} / {num_2} = {num_1 / num_1}")
#     else:
#         print("Digite um operador válido")
# except ZeroDivisionError:
#     print("Não é possível dividir 0 por outro número")
# except ValueError:
#     print("Digite um número válido")
# except EOFError:
#     print("Você está saindo do programa")

# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica 
# E utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     numero = int(input('Digite um número: '))
#     if numero > 0:
#         print("Número positivo")
#     elif numero == 0:
#         print("Número neutro")
#     else:
#         print("Número negativo")
#     if numero % 2 == 0:
#         print("Número par")
#     else:
#         print("Número ímpar")
# except ValueError:
#     print("Digite um número válido")
# except EOFError:
#     print("Você está saindo do programa")


# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

# lista_principal = []

# try:
#     lista_stage = input("Digite uma lista de números separados por vírgula: ")
#     lista_silver = lista_stage.split(',')
#     for num in lista_silver:
#         lista_principal.append(int(num.strip()))
#         print(num)
# except ValueError:
#     print("Digite apenas números e separados por vírgula")






