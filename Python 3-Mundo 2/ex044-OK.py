#EU FIZ:toda a parte de cima do if/elif/else
# a parte do if/elif/else peguei do professor,pois eu tinha feito de um jeito mas ....
# eu nao estava perguntando na opcao 3/4 quantas vezes ia querer PARCELAR,e o valor final com juros quanto ia ficar com base na Qtd.Parcelas que a pessoa escolheu.
# peguei o if/elif/else do professor e coloquei cor depois.
#
#
#JEITO QUE FIZ O LOJA DO VITAO:COM COR JUNTO
#print('\033[4;35m='*15,'LOJA DO VITAO','='*16)
#
#JEITO QUE O PROFESSOR FEZ O LOJA DO VITAO:MAIS SIMPLIFICADO
print(f'{' LOJAS VITOR ':=^40}')
# o sinal ^ significa CENTRALIZAR algo !!!!!
#
v=float(input('\033[m\033[1;32mQual o valor do produto?\033[m'))
print('''\033[m\033[4;31mOPÇÕES DE PAGAMENTOS:\033[m
\033[1;31m[ 1 ]\033[m\033[1;32m Á vista dinheiro/cheque com 10% desconto.
\033[1;31m[ 2 ]\033[m\033[1;32m Á vista no cartao com 5% desconto.
\033[1;31m[ 3 ]\033[m\033[1;32m Em até 2x no cartão.
\033[1;31m[ 4 ]\033[m\033[1;32m Em 3x ou mais no cartao c/20% juros.\033[m''')
#
#
#FIZ ISSO EM BAIXO AQUI DE op1/op2 que ensina como calcula tambem, mas ....
#O PROFESSOR FEZ DE OUTRO JEITO QUE CONSEGUI ENTENDER MAIS FACIL E MELHOR O if/elif/else:
# op1=v*0.9
# para calcular 10 de desconto é só multiplicar(*) o valor por 0.9 (100%-10%=90%==0.9)
#
# op2= v*0.95
# para calcular 5 de desconto é só multiplicar(*) o valor por 0.95 (100%-5%=95%==0.95)
#
#
opc=int(input('\033[4;31mQual sua opção?\033[m'))
if opc == 1:
    total= v - ( v * 10/100)
elif opc == 2:
    total= v - (v * 5/100)
elif opc == 3:
    total= v
    parcela = total / 2
    print(f'\033[1;34mSua compra será parcelada em \033[4m2x\033[m\033[1;34m de \033[7;40mR${parcela}\033[m\033[1;34m SEM JUROS.\033[m')
elif opc == 4:
    total= v + (v * 20/100)
    totparc=int(input('\033[4;31mQuantas parcelas?\033[m'))
    parcela= total / totparc
    print(f'\033[1;34mSua compra será parcelada em \033[4m{totparc}x de R${parcela:.2f} COM JUROS.\033[m')
else:
    total= v
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente !!')
print(f'\033[1;34mSua compra de \033[7;40mR${v:.2f}\033[m\033[1;34m vai custar \033[7;40mR${total:.2f}\033[m\033[1;34m no final.')
