import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

a, b= map(int, input().split())

if a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")





    a, b= map(int, input().split())

if a % b == 0  A % B == 0 or B % A == 0:
    print("Nao sao Multiplos")
else:
    print("Nao Sao Multiplos")
