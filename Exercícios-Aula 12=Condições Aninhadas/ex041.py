#JEITO Q FIZ: ESTA CERTO TAMBEM!
#COLOQUEI O ANO 2026 DIRETO == N USEI PEGANDO O ANO DO SISTEMA
#
# i=int(input('\033[35mEm que ano voçê nasceu?\033[m'))
# c=(2026-i)
# if c <= 9:
#     print('Sua categoria é: \033[1;34mMIRIM')
# elif c <= 14:
#     print('Sua categoria é: \033[1;34mINFANTIL')
# elif c <= 19:
#     print('Sua categoria é: \033[1;34mJUNIOR')
# elif c == 20:
#     print('Sua categoria é: \033[1;34mSÊNIOR')
# else:
#     print('Sua categoria é: \033[1;34mMASTER')
#
#JEITO QUE O PROFESSOR FEZ:
from datetime import date
atual= date.today().year
nasc=int(input('Ano de Nascimento:'))
idade= atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <=9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação:INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
