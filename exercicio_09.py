# Faça um programa que converta a temperatura de Celsius para Fahrenheit. (0 °C × 9/5) + 32 = 32 °F

CONSTANTE_FAHRENHEIT = 32
celsius = float(input('Digite a temperatura em Celsius: '))

temp_fahrenheit = (celsius * (9 / 5)) + CONSTANTE_FAHRENHEIT

print(f"{celsius}°C é igual a {temp_fahrenheit}°F")


