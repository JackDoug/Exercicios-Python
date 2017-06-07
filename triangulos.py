l1=int(input("Ditite lado 1  "))
l2=int(input("Digite lado 2  "))
l3=int(input("Digite lado 3  "))
if l1==l2==l3:
    print("equilatero")
elif (l1==l2)!=l3:
    print("isosceles")
elif (l1!=l2)==l3:
    print("isosceles")
elif(l1==l3)!=l2:
    print("isosceles")
elif(l1!=l3)==l2:
     print("isosceles")
else:
    print("escaleno")

