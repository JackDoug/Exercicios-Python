na=int(input("informe o número aleartório de 1 a 10 "))
nc=int(input("acerte o número  " ))
x=0
while (x!=nc):
    print (x)
    x=x+1
    if na==nc:
        print("acertou")
    elif na>nc:
        print("menor que número certo")
    elif na<nc:
        print("maior que número certo")
else:
        print("tente novamente")

