#JEITO QUE FIZ:NAO ESTA COM TODAS AS INFORMAÇÕES COMPLETAS EM CADA RESPOSTA.
# a=int(input('\033[4;33mEm que ano voçê nasceu?\033[m:'))
# al=(2026-a)
# f=(18-al)
# f1=(al-18)
# if al < 18:
#     print(f'\033[1;34mVoçê precisa se alistar daqui\033[m \033[4;31m{f} anos\033[m\033[1;34m,no alistamento militar.')
# elif al == 18:
#     print(f'\033[1;32mEstá na hora de se alistar ao serviço militar.')
# else :
#     print(f'\033[1;31mJá passou do prazo de se alistar ao serviço militar em \033[4m{f1} anos.')
#
#
#JEITO QUE O PROFESSOR FEZ:
#Pega o ano direto do sistema.{aula 8-sobre módulos-1' mundo python}
from datetime import date
atual= date.today().year
nasc=int(input('Ano de nascimento:'))
idade= atual -nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Voçê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo= 18- idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano= atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Voçê já deveria ter se alistado há {saldo} anos.')
    ano=atual - saldo
    print(f'Seu alistamento foi em {ano}.')
