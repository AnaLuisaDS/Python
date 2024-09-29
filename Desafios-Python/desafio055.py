"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0

for p in range(1,3):
    peso = float(input('Informe o seu peso atual: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}')
print(f'O menor peso lido foi {menor}')
