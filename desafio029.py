""" Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite."""

v = float(input('Qual foi a velocidade do carro?'))
multa = v * 7.00
if v > 80:
    print(f'Caramba, você ultrapassou o limite estabelecido. \n'
          f'Você deve uma multa de R${multa:.2f}.')
else:
    print('Fique tranquilo, você não foi multado! :)')

