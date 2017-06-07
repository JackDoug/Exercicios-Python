op=int(input("Selecione uma das opções =  Soma  [1] -  Maior  [2] -  Menor  [3] -  Media  [4]: "))

n1=lerNumero()
n2=lerNumero()
n3=lerNumero()

if op==1:
    x=soma(n1,n2,n3)
    print("A soma dos 3 números é: ",x)
if op==2:
    x=(maior(n1,n2,n3))
    print ("O maior número é: ",x)
if op==3:
    x=(menor(n1,n2,n3))
    print ("O menor número é: ",x)
if op==4:
    x=(media(n1,n2,n3))
    print(" A média é",x)

