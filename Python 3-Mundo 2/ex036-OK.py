# como fiz: mesmo resultado do professor
vc=float(input('Qual o valor da casa?'))
sl=float(input('Qual seu salário?'))
qa=int(input('Em quantos anos quer pagar a casa?'))
pm=vc/(qa*12)
lmt=sl * (30/100)
print(f'\033[34mO valor da casa é: \033[36mR${vc} ')
print(f'\033[34mVocê recebe: \033[36mR${sl} \033[34mde sálario')
print(f'\033[34mQuer pagar a casa em:\033[36m{qa} anos')
print(f'\033[34mO valor da prestação mensal seria de:\033[36mR${pm:.2f}')
if pm > lmt:
  print('\033[1;31mVoçê não está liberado a fazer o empréstimo!')
else :
  print('\033[1;32mVocê pode fazer o empréstimo,parabéns !')

## como professor fez:
# casa=float(input('Valor da casa:R$'))
# salário= float(input('Salário do comprador:R$:'))
# anos=int(input('Quantos anos de financiamento?'))
# prestação = casa / (anos * 12)
# mínimo= salário * 30 / 100
# print(f'Para pagar uma casa de R${casa:.2f} em {anos}anos',end='')
# print(f' a prestação será de R${prestação:.2f}')
# if prestação <= mínimo:
#   print('Empréstimo pode ser CONCEDIDO')
# else:
#   print('Empréstimo NEGADO')