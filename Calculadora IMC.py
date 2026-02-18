##Calculadora IMC

res1=input("Agora vamos calcular o seu IMC, por favor, digite ''1'' para prosseguir: ")
if res1=="1":
    peso=float(input("Digite seu peso: "))
    alt=float(input("Digite sua altura: "))
    imc=peso/(alt*alt)
    print(f"Seu IMC é: {imc}%")
else:
    print("Algo deu errado, por favor, reinicie o programa")