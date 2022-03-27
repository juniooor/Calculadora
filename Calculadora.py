#Criando calculadora no Python sem interface grafica
from modulo import Calculador as cal
from verifica import isnum


while True:
    n1=input('Digite o numero que irá realizar a operação: ')
    if isnum(n1)==False:
        print(f'ERROR:{n1}, não é um numero')
    else:
        if isnum(n1)==True:
            if isnum(n1)==int():
                n1=int(n1)
                break
            else:
                n1=float(n1)
                break    
while True:
    oper=str(input('digite a operação:[+][-][/][*] ')).strip()[0]
    if oper not in '+-/*':
        print('ERROR: operação invalida')
    else:
        break
while True:
    n2=input('Digite o numero que irá realizar a operação: ')
    if isnum(n2)==False:
        print(f'ERROR: {n2}, não é um numero')
    else:
        if isnum(n2)==True:
            if isnum(n2)==int():
                n2=int(n2)
                break
            else:
                n2=float(n2)
                break  

if oper=='+':
    print(f'Resultado da soma: \n {cal.soma(n1,n2)}')
elif oper=='-':
    print(f'Resultado da subtração: \n {cal.subtrair(n1,n2)}')
elif oper=='/':
    print(f'Resultado da divisão: \n {cal.dividir(n1,n2)}')
else:
    print(f'Resultado da Multiplicação: \n {cal.multiplicar(n1,n2)}')





