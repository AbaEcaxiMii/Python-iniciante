##1005
a=float(input())
b=float(input())
media=(a*3.5+b*7.5)/11
print(f"MEDIA = {media:.5f}")
##1006
a=float(input())
b=float(input())
c=float(input())
media=(a*2+b*3+c*5)/10
print(f"MEDIA = {media:.1f}")
##1007
a=int(input())
b=int(input())
c=int(input())
d=int(input())
dif=(a*b-c*d)
print(f"DIFERENCA = {dif}")
##1008
number=int(input())
hora=int(input())
porhora=float(input())
salary= hora*porhora
print(f"NUMBER = {number}")
print(f"SALARY = U$ {salary:.2f}")
##1009
nome=input()
sala_fixo=float(input())
vendas=float(input())
total=sala_fixo+(vendas*0.15)
print(f"TOTAL = R$ {total:.2f}")
##1010
cod1, quant1, valor1 = input().split()
cod1 = int(cod1)
quant1 = int(quant1)
valor1 = float(valor1)

cod2, quant2, valor2 = input().split()
cod2 = int(cod2)
quant2 = int(quant2)
valor2 = float(valor2)

total= (quant1*valor1)+(quant2*valor2)
print(f"VALOR A PAGAR: R$ {total:.2f}")
##1011
pi=3.14159
raio=float(input())
vol=(4/3)*pi*raio**3
print(f"VOLUME = {vol:.3f}")
##1012
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)

pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
##1013
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

ab=int((a+b+abs(a-b))/2)
maior=ab
if ab<c:
    maior=c

print(f"{maior} eh o maior")
    
##1014
x=int(input())
y=float(input())
total=x/y
print(f"{total:.3f} km/l")
##1015
from math import sqrt

x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

dis = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{dis:.4f}")
##1016
dis=int(input())

# 1 km -> 2 minutos
# d km -> x minutos
# x = d * 2
tempo = dis * 2

print(f"{tempo} minutos")
##1017
tempo = int(input())
vel = int(input())

dis = tempo * vel

#1L -> 12 km
#xL -> dis km
#x * 12 = dis
litros = dis / 12

print(f"{litros:.3f}")

##1018

N = int(input())

valor = N

notas = [100, 50, 20, 10, 5, 2, 1]

# Mostrar o valor lido
print(valor)

for nota in notas:
    quantidade = N // nota  # Divisão com todos no grupo
    print(f"{quantidade} nota(s) de R$ {nota},00")
    N = N % nota  # Atualiza o N pras outras divisões

##1019
N = int(input())

horas = N // 3600           # 1 hora = 3600 segundos
resto = N % 3600            # O que sobra após tirar as horas
minutos = resto // 60       # 1 minuto = 60 segundos
segundos = resto % 60       # O que sobra após tirar os minutos

print(f"{horas}:{minutos}:{segundos}")

##1020
N=int(input())

anos=N//365
resto=N%365
mes=resto//30
dias=resto%30

print(f"{anos} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")

##1021

valor = float(input())

# Converter para centavos para evitar problemas com ponto flutuante
centavos = int(round(valor * 100))

# Notas e moedas em centavos
notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
nomes = [
    "nota(s) de R$ 100.00",
    "nota(s) de R$ 50.00", 
    "nota(s) de R$ 20.00",
    "nota(s) de R$ 10.00",
    "nota(s) de R$ 5.00",
    "nota(s) de R$ 2.00",
    "moeda(s) de R$ 1.00",
    "moeda(s) de R$ 0.50",
    "moeda(s) de R$ 0.25",
    "moeda(s) de R$ 0.10",
    "moeda(s) de R$ 0.05",
    "moeda(s) de R$ 0.01"
]

print("NOTAS:")
for i in range(6):  # Primeiras 6 são notas
    quantidade = centavos // notas_moedas[i]
    print(f"{quantidade} {nomes[i]}")
    centavos = centavos % notas_moedas[i]

print("MOEDAS:")
for i in range(6, 12):  # Últimas 6 são moedas
    quantidade = centavos // notas_moedas[i]
    print(f"{quantidade} {nomes[i]}")
    centavos = centavos % notas_moedas[i]

##1035
##1036
##1037
##1038

##1040