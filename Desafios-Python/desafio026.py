""" Faça um programa que leia uma frase pelo teclado e
    mostre quantas vezes aparece a letra “A”,
    em que posição ela aparece a primeira vez e
    em que posição ela aparece a última vez."""

frase = input('Digite uma frase: ').upper().strip()
frase_end = frase.replace(' ', '')
print(f'A letra "A" aparece {frase.count("A")} vezes.')
print(f'A primeira letra "A" apareceu na posição {frase_end.find("A")+1}.')
print(f'A última letra "A" apareceu na posição {frase_end.rfind("A")+1}.')
