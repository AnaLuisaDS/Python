""" Desafio 007 -  Faça um programa que leia as duas notas de um aluno, depois calcule
e mostre a sua média entre as notas."""

nota1 = float(input('Digite a sua nota do primeiro bimestre:'))
nota2 = float(input('Digite a sua nota do segundo bimestre:'))
media = (nota1+nota2)/2
print('Por enquanto, a sua média conforme os dados fornecidos, é de {} '.format(media))

#Aplicação com menos variáveis.
nota1 = float(input('Digite a sua nota do primeiro bimestre:'))
nota2 = float(input('Digite a sua nota do segundo bimestre:'))
print(f'Por enquanto, a sua média conforme os dados fornecidos, é de {(nota1+nota2)/2}')
