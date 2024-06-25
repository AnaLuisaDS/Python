import random

n1 = input('Escreva o nome do primeiro aluno:')
n2 = input('Escreva o nome do segundo aluno:')
n3 = input('Escreva o nome do terceiro aluno:')
n4 = input('Escreva o nome do quarto aluno:')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')