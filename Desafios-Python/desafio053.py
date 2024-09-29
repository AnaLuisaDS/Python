"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

#Método utilizando o Loop 'for'
appear = input('Digite uma frase (Sem acentuação): ').strip().lower()
phrase_end = ''.join(appear)    #Remove os caracteres vazios
box = ''          #Serve para armazenar as letras ao inverso na utilização das condicionais
for l in range(len(phrase_end)-1, -1, -1): #Conta de modo decrescente #O último -1 serve apenas para inverter
    box += phrase_end[l]
if box in phrase_end:
    print(f'A frase "{phrase_end}" é um \033[36mPALÍNDROMO\033[m')
else:
    print(f'A frase "{phrase_end}" \033[31mNÃO É PALÍNDROMO\033[m ')



#Método utilizando somente condição 'if' e 'else'
frase = input('Digite uma frase (Sem acentuação): ').capitalize()
frase_end = frase.replace(' ','').upper()
frase_invertida = frase_end[::-1]
if frase_invertida in frase_end:
    print(f'A frase "{frase}" é um \033[36mPALÍNDROMO.\033[m')
else:
    print(f'A frase "{frase}" \033[36mNÃO É UM PALÍNDROMO.\033[m')

