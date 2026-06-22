#JEITO QUE FIZ:FUNCIONA IGUAL !!!
p=float(input('\033[1;34mQual seu peso?(Kg)'))
a=float(input('Qual sua altura?(m)\033[m'))
imc= p/(a**2)
if imc < 18.5:
    print(f'\033[36mSeu IMC é \033[m\033[36;40m{imc:.1f}\033[m \033[36me seu status é:\033[m\033[1;31m ABAIXO DO PESO')
elif imc <25:
    print(f'\033[36mSeu IMC é \033[m\033[36;40m{imc:.1f}\033[m \033[36me seu status é:\033[m\033[1;32m PESO IDEAL')
elif imc <30:
    print(f'\033[36mSeu IMC é \033[m\033[36;40m{imc:.1f}\033[m \033[36me seu status é:\033[m\033[1;33m SOBREPESO')
elif imc <40:
    print(f'\033[36mSeu IMC é \033[m\033[36;40m{imc:.1f}\033[m \033[36me seu status é:\033[m\033[1;31m OBESIDADE')
elif imc >40:
    print(f'\033[36mSeu IMC é \033[m\033[36;40m{imc:.1f}\033[m \033[36me seu status é:\033[m\033[1;31m OBESIDADE MÓRBIDA')
#
#JEITO QUE O PROFESSOR FEZ:
# peso=float(input('Qual é seu peso?(Kg)'))
# altura=float(input('Qual é sua altura?(m)'))
# imc=peso / (altura ** 2)
# print(f'O IMC dessa pessoa é de {imc:.1f}')
# if imc < 18.5:
#     print('Voçê esta ABAIXO DO PESO normal')
# elif 18.5 <= imc < 25:
#     print('PARABÉNS, voçê está na faixa de PESO NORMAL')
# elif 25 <= imc < 30:
#     print('Voçê está em SOBREPESO')
# elif 30 <= imc < 40:
#     print('Voçê está em OBESIDADE')
# elif imc >= 40:
#     print('Voçê está em OBESIDADE MÓRBIDA, cuidado!')
#JEITO QUE FIZ == IGUAL ESSE DO PROFESSOR