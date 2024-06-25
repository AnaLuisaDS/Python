"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo sem considerar espaços.

– Quantas letras tem o primeiro nome."""



name = input('Escreva seu nome completo:')
print(f'Seu nome completo em maiúsculo é {name.upper()}')
print(f'Seu nome completo em minúsculo é {name.lower()}')
print(f'Seu nome completo tem {len(name.replace(' ','' ))} letras.')
Separar = name.split()
print(f'Seu primeiro nome é {Separar[0]} e tem {len(Separar[0])} letras.')


#Outro modo de aplicação
name = input('Escreva seu nome completo:').strip()
print(f'Seu nome completo em maiúsculo é {name.upper()}')
print(f'Seu nome completo em minúsculo é {name.lower()}')
print(f'Seu nome tem {len(name) - name.count(" ")} letras.')
print(f'Seu primeiro nome tem {name.find(" ")} letras. ')