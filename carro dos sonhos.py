
a=int(input("Digite o Valor final do seu carro dos sonhos: "))

custo= a * 0.27
imposto= a * 0.45
distribuidor= a * 0.28

print("O Custo de fábrica do seu carro foi: ","%0.2f"%custo)

print("A Percentagem do distribuidor do seu carro foi: ","%2.3f"% distribuidor)

print("O Imposto aplicado em cima do seu carro foi: ","%d"% imposto)
# 0 %d , ele vai mostrar o o numero sem virgula, só a parte inteira
