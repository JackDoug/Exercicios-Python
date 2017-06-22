## média com função ##

def LerNúmero():
    a=int(input("Digite um número Inteiro: "))
    return(a)

def soma(a,b,c):
    return (a+b+c)

def media(a,b,c):
    return (soma(a,b,c)/3)

def maior(a,b,c):
    if a>b and a>c:
        M=a
    if b>a and b>c:
        M=B
    if c>a and c>b:
        M=c
    return(M)

n1=LerNúmero()
n2=LerNúmero()
n3=LerNúmero()
print(media(n1,n2,n3))
print(maior(n1,n2,n3))
