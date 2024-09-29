print("="*30)
print("\033[7:30:45m10 TERMOS DE UMA PA - (WHILE)\033[m")
print("="*30)
termo = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da progressão: "))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        termo += r
        print(termo, end=" -> ")
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos PA você quer saber mais? '))
print(f'PROGRAMA FINALIZADO! Contabilizados {total} PA.')