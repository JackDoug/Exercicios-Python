n1=int(input("Digite primeiro número "))
n2=int(input("digite segundo numero "))
n3=int(input("digite terceiro número "))
op=int(input("selecione uma das opcões= Soma {1} - Maior {2} - Menor {3} média {4}" ))
r=(n1+n2+n3)
med=r/3


if  n1>n2 and n1>n3:
    M=n1
if  n2>n1 and n2>n3:
    M=n2
if n3>n1 and n3>n2:
    M=n3


if  n1<n2 and n1<n3:
    n=n1
if  n2<n1 and n2<n3:
    n=n2
if n3<n1 and n3<n2:
    n=n3

if op==1:
    print("A soma dos 3 números é: ",r)
if op==2:
    print ("O maior número é: ",M)
if op==3:
    print ("O menor número é: ",n)
if op==4:
    print(" A média é",med)



