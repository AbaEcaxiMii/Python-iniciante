import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

#val=input().split()
#
#for i in range(len(val)):
#    val[i]=int(val[i])
#
#val.sort(reverse=False)
#print(f"Crescente: {val}")
#
#val.sort(reverse=True)
#print(f"Decrescente: {val}")
#
#lista_nova=sorted(val, reverse=True)
#
#lista=[1, 2, 3]



def main():
    a= int(input("Digite um numero inteiro: "))
    if a!=0:
        if a%2==0:
            print(f"{a} eh par")
        elif a%2==1:
            print(f"{a} eh impar")
    else:
        print("0 não é nem par ou impar")

main()
