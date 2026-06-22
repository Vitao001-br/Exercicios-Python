#NAO ENTENDI MUITO COMO FAZER ESSE EXERCICIO
#FUI VENDO A AULA E FAZENDO,E CORRIGINDO DEPOIS JUNTO COM O PROFESSOR
#EU QUE ADICIONEI CORES
#
from random import randint   #importar um numero inteiro random
from time import sleep       #importar uma pausa entre frases, por exemplo no JO KEN PO
itens=('pedra','papel','tesoura')                                  #linha 13 a 17
pc=randint(0,2) #from random import randint
print('''\033[35mSuas opções:\033[m
\033[1;31m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opc=int(input('Qual é a sua jogada?\033[m'))
print('\033[1;35mJO')
sleep(1)       #from time import sleep
print('KEN')
sleep(1)       #from time import sleep
print('PO!!!\033[m')
print('\033[44m-=\033[m'*20)
print(f'\033[34mComputador jogou \033[4m{itens[pc]}\033[m \n\033[34mJogador jogou \033[4m{itens[opc]}\033[m')
print('\033[44m-=\033[m'*20)
if pc == 0:  # pc jogou PEDRA
    if opc == 0:
        print('\033[1;32mEMPATE')
    elif opc == 1:
        print('\033[1;32mJOGADOR VENCE')
    elif opc == 2:
        print('\033[1;32mCOMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')
elif pc == 1:  # pc jogou PAPEL
    if opc == 0:
        print('\033[1;32mCOMPUTADOR VENCE')
    elif opc == 1:
        print('\033[1;32mEMPATE')
    elif opc == 2:
        print('\033[1;32mJOGADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')
elif pc == 2:  # pc jogou TESOURA
    if opc == 0:
        print('\033[1;32mJOGADOR VENCE')
    elif opc == 1:
        print('\033[1;32mCOMPUTADOR VENCE')
    elif opc == 2:
        print('\033[1;32mEMPATE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')
