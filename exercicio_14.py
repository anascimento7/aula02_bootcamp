# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = str(input("Insira uma data no formato dd/mm/aaaa: "))
data_lista = data.split('/')
dia = data_lista[0]
mes = data_lista[1]
ano = data_lista[2]

print(f"{dia} do {mes} de {ano}")