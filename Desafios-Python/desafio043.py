kg = float(input('Digite, em quilos, o seu peso atual (Ex: 50.5): '))
alt = float(input('Digite, em metros, sua altura atual (Ex: 1.60): '))
imc = kg / (alt ** 2)
print(f'O seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso - \033[31mCuidado!\033[m')
elif 18.5 <= imc < 25:
    print('\033[34mPeso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso!\033[m')
elif 30 <= imc < 40:
    print('Obesidade - \033[31mCuidado!\033[m')
else:
    print('Obesidade \033[31mMorbida!\033[m')


