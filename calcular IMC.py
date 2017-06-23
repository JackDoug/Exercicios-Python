apos calcular o IMC informe, o de acordo com o sexo informe a situação de acordo com a tabela a seguir:



sexo=input("Digite 'f' caso seu sexo seja feminino ou digite 'm' caso seu sexo seja masculino: ")
peso=int(input("Informe seu peso: "))
altura=float(input("Informe sua altura: "))


imc= peso/ (altura ** 2)
print("O seu indíce de massa corporal é ", imc)
if sexo == "f":
    if imc < 19.1:
        print("Você está abaixo do peso")
    if imc >= 19.1 and imc < 25.8:
        print("Você está no seu peso normal")
    if imc >= 25.8 and imc < 27.3:
        print("Você está marginalmente acima do seu peso")
    if imc >= 27.3 and imc < 32.3:
        print("Você está acima do seu peso ideal")

if sexo == "m":
    if imc < 20.7:
        print("Você está abaixo do peso")
    if imc >= 20.7 and imc < 26.4:
        print("Você está no seu peso normal")
    if imc >= 26.4 and imc < 27.8:
        print("Você está marginalmente acima do seu peso")
    if imc >= 27.8 and imc < 31:
        print("Você está acima do seu peso ideal")
