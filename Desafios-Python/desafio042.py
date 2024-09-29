s1 = float(input('Escreva o primeiro segmento:'))
s2 = float(input('Escreva o segundo segmento:'))
s3 = float(input('Escreva o terceiro segmento:'))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print(f'Os segmentos fornecidos \033[4:32m PODEM \033[m formar um triângulo')
    if s2 == s1 == s3:
        print('Será um triângulo \033[33mEQUILÁTERO!\033[m')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('Será um triângulo \033[33mISÓSCELES!\033[m')
    else:
        print('Será um triângulo \033[33mESCALENO!\033[m')
else:
    print(f'Os segmentos fornecidos \033[4:31m NÃO PODEM \033[m formar um triângulo.')

