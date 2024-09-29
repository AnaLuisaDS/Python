import random
count = 1
comp = random.randint(0,3)
print('\033[35mO computador irá escolher de forma aleatória um número entre 0 e 10.\n'
      '---- TENTE ADVINHAR! ----\033[m')
jogador = int(input("Faça a sua escolha: "))
while jogador != comp:
    print("Tente outra vez!")
    jogador = int(input("\033[36mQuem sabe dessa vez você acerta ;)\033[m : "))
    count += 1
print(f'\033[34mPARABÈNS! Você acertou!\033[m Números de Tentativas = {count}')