#JEITO QUE FIZ:ESTA CERTO TAMBEM!
# n1=float(input('\033[1;34mDigite a primeira nota:'))
# n2=float(input('Digite a segunda nota:\033[m'))
# m=(n1+n2) /2
# if m < 5:
#     print(f'\033[4;31mREPROVADO\033[m \033[31m- SUA MÉDIA FOI {m}')
# elif m >= 7:
#     print(f'\033[4;32mAPROVADO\033[m \033[1;32m- SUA MÉDIA FOI {m}')
# else:
#     print(f'\033[4;33mRECUPERAÇÂO\033[m \033[1;33m- SUA MÉDIA FOI {m}')
#
#JEITO QUE O PROFESSOR FEZ:
#Adicionei cores(do jeito q fiz,para esse do professor)
#
nota1=float(input('\033[1;36mPrimeira nota:'))
nota2=float(input('Segunda nota:\033[m'))
media= (nota1 + nota2) / 2
print(f'\033[1;34mTirando {nota1:.1f} e {nota2:.1f}, a MÉDIA do aluno é \033[4m{media:.1f}\033[m')
#esse jeito é o normal(maior tambem):
#if média >=5 and média < 7:
#esse jeito abaixo é mais simplificado(e mais curto)
if 7> media >=5:
    print('\033[1;33mO aluno está em \033[4mRECUPERAÇÃO.\033[m')
elif media < 5:
    print('\033[1;31mO aluno está \033[4mREPROVADO.\033[m')
#elif media >=7 (pode usar assim tambem,+1 elif no lugar de else)
else:
    print('\033[1;32mO aluno está \033[4mAPROVADO.\033[m')