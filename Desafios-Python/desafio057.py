""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = input("Informe seu sexo [M/F]: ").upper().strip()[0]
while sexo not in 'MF':
    print("\033[34mInforme corretamente!\033[m\n"
          "RELEMBRANDO: \033[31mM = Masculino  F = Feminino\033[m")
    sexo = input("Informe novamente o seu sexo [M/F]: ").upper().strip()[0]
print(f'\033[32mSexo {sexo} registrado com sucesso!\033[m')
print("Até o próximo!")