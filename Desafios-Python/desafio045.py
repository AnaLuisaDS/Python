import random
from time import sleep
name = input('Qual é o seu nome?')
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
itens =  ['PEDRA' , 'PAPEL' , 'TESOURA']
comp = random.randint(0,2)
user = int(input('Qual é a sua jogada ;) ?  : '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(f'O Computador jogou {itens[comp]}')
print(f'O {name} jogou {itens[user]}')
if comp == user:
      print('\033[36mEMPATE!\033[m')
elif (comp == 0 and user == 2) or (comp == 1 and user == 0) or (comp == 2 and user == 1):
      print('\033[36mCOMPUTADOR VENCEU!\033[m')
elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
      print(f'\033[36m{name} VENCEU!\033[m')
else:
      print('\033[31mOPÇÃO INVÁLIDA! Tente novamente.\033[m')

