#JEITO Q FIZ: FALTOU O ELIF/else DE 'NAO PODE FORMAR TRIANGULO'.
# print('\033[35m-='*20)
# print('Analisador de triângulos')
# print('-='*20)
# r1=float(input('\033[m\033[1;34mPrimeiro segmento:'))
# r2=float(input('Segundo segmento:'))
# r3=float(input('Terceito segmento:\033[m'))
# if r1==r2==r3:
#     print('\033[33mÉ um triângulo\033[m\033[4;33m Equílatero')
# elif r1==r2 or r1==r3  or r2==r3:
#     print('\033[33mÉ um triângulo\033[m\033[4;33m Ísosceles')
# else :
#     print('\033[33mÉ um triângulo\033[m\033[4;33m Escaleno')
#
#JEITO QUE O PROFESSOR FEZ:
#PEGOU O EXERCICIO 35 E APRIMOROU ELE:
r1= float(input('Primeiro segmento:'))
r2= float(input('Segundo segmento:'))
r3= float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
#jeito padrao: if r1 == r2 and r2 == r3
#esse jeito abaixo o python deixa fazer:
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
# coloco != r1 no final porque é diferença,se fosse os 3 igual,n precisaria
        print('ESCALENO!')
# pode ser if ainda,colocou elif só para diferençiar um pouco.
    else:
        print('ISÓSCELES')
#ficou IF/ELIF/ELSE == TODOS DENTRO DE UM MESMO IF DO COMEÇO.
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')