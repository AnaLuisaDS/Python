"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas."""

d = float(input('Escreva em quilometros a distância da viagem:'))
if d >= 200:
    pvl = d * 0.50
    print(f'Para viagens de {d} quilometros, o preço é R${pvl :.2f}')
else:
    pvc = d * 0.45
    print(f'Para passagens de {d} quilometros, o preço é R${pvc :.2f}')
print("Tenha uma boa vaigem! :)" )

#Aplicaçao de if simplificado
d = float(input('Escreva em quilometros a distância da viagem:'))
p = d * 0.50 if d >= 200 else d * 0.45
print(f'O preço da sua passagem será de R${p :.2f}')
print("Tenha uma boa viagem! :)")