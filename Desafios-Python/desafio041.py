from datetime import date
nasc = int(input('Digite o f ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('Você é classificado como \033[36mMIRIM\033[m')
elif idade <= 14:
    print('Você é classificado como \033[35mINFANTIL\033[m')
elif idade <= 19:
    print('Você é classificado como \033[34mJÚNIOR\033[m')
elif idade <= 25:
    print('Você é classificado como \033[33mSÊNIOR\033[m')
else:
    print('Você é classificado como \033[34mMASTER\033[m')

