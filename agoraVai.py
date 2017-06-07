nc=6
n1=int(input("acerte o numero "))
x=0

while (n1!=nc):
    print (x)
    x=x+1
    if n1==nc:
        print("voce acertou")
    elif n1>nc:
        print("maior que número certo")
    elif n1<nc:
        print("menor que numero certo")
    else:
        print("tente outra vez")
