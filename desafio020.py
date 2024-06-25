from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)      #Não precisa de variável, pois é grupo de respostas. #Está exercendo função de atribuição
print(lista)