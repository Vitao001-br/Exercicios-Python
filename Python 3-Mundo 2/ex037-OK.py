
#FIZ ISSO MAIS NAO TERMINEI,POS NAO ENTENDI NADA !!!
# n=int(input('\033[31mDigite um número inteiro para conversão:\033[m'))
# c=input('\033[36m1= \033[mpara binário\n'
#         '\033[36m2= \033[mpara octal\n'
#         '\033[36m3= \033[mpara hexadecimal\n'
#         '\033[31mQual será a base de conversão?:')
# b=
# o=
# h=
# if c = 1:
#     print(f'O número {c} convertido para binário é:{b}')
# elif c = 2:
#     print(f'O número {c} convertido para octal é:{o}')
# else:
#     print(f'O número {c} convertido para hexadecimal é:{h}')

#CORREÇÃO DO PROFESSOR
num=int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção=int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO  é igual a {bin(num)[2:]}')
elif opção  == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida.Tente novamente')

