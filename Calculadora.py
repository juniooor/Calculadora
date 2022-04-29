#Criando calculadora no Python sem interface grafica
from time import sleep
from modulo import Calculador as cal
from verifica import isnum
red='\033[91m'
branco='\033[m'
resultado=[]
while True:
    while True:
        n1=input('Digite o numero que irá realizar a operação: ')
        if isnum(n1)==False:
            print(f'{red}ERROR:{n1}, não é um numero{branco}')
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
            print(f'{red}ERROR: operação invalida{branco}')
        else:
            break
    while True:
        n2=input('Digite o numero que irá realizar a operação: ')
        if isnum(n2)==False:
            print(f'{red}ERROR: {n2}, não é um numero{branco}')
        else:
            if isnum(n2)==True:
                if isnum(n2)==int():
                    n2=int(n2)
                    break
                else:
                    n2=float(n2)
                    break  
    if oper=='+':
        result=cal.soma(n1,n2)
        resultado.append(result)
        print(f'Resultado da soma: \n {result}')
    elif oper=='-':
        result=cal.subtrair(n1,n2)
        resultado.append(result)
        print(f'Resultado da subtração: \n {result}')
    elif oper=='/':
        result=cal.dividir(n1,n2)
        resultado.append(result)
        print(f'Resultado da divisão: \n {result}')
    else:
        result=cal.multiplicar(n1,n2)
        resultado.append(result)
        print(f'Resultado da Multiplicação: \n {result}')

    exibir=str(input('Deseja exibir todos os resultados?[S]sim / [N]não: ')).upper().strip()[0]
    if exibir=='S':
        for i in resultado:
            print(i)
    else:
        pass

    final=str(input('Deseja fazer mais algum calculo? [S]Sim / [N]Não:  ')).upper().strip()[0]

    if final=='N':
        print(f'finalizando o programa',end='')
        print('.',end='')
        print('.',end='')
        print('.')
        break
    else:
        pass


