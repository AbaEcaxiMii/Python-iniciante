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

notas = [100, 50, 20, 10, 5, 2, 1]

print(N)

for nota in notas:
    quantidade = N // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    N = N % nota  # Atualiza o N pras outras divisões (é o resto)

##1019
N = int(input())

horas = N // 3600           # 1 hora = 3600 segundos
resto = N % 3600            # O que "sobra" das horas
minutos = resto // 60       # 1 minuto = 60 segundos
segundos = resto % 60       # O que "sobra" dos minutos

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

# Converter para centavos para evitar problemas com float
centavos = int(round(valor * 100))

# Notas e moedas em ->centavos<-
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
a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

check=0

if (b>c) and (d>a) and (c+d>a+b) and (c>0) and (d>0) and (a%2==0): check=1

if check:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

##1036
a, b, c=input().split()
a=float(a)
b=float(b)
c=float(c)

from math import sqrt

delta=(b**2)-4*a*c

if a==0 or delta<0:
    print(f"Impossivel calcular")
else:

    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")


##1037

a = float(input())

if a >= 0 and a <= 25:
    print("Intervalo [0,25]")
elif a > 25 and a <= 50:
    print("Intervalo (25,50]")
elif a > 50 and a <= 75:
    print("Intervalo (50,75]")
elif a > 75 and a <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

##1038
lista=[0, 4, 4.5, 5, 2, 1.5]
lista_valores=[float(i) for i in lista]

a, b= input().split()
a=int(a)
b=int(b)

total= lista_valores[a]*b 

print(f"Total: R$ {total:.2f}")

##1040
n1, n2, n3, n4 = map(float, input().split())
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
exame=0

print(f"Media: {media:.1f}")
if media>=7:
    print("Aluno aprovado.")
elif media<5:
    print("Aluno reprovado.")
elif media>=5 and media<7:
    print("Aluno em exame.")
    nota_exame=float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media= (nota_exame+media)/2
    if media>=5:
        print("Aluno aprovado.")
    elif media<5:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")

##1041
x,y= map(float, input().split())

res="Origem"

if x ==0 and y == 0:
    res="Origem"
elif x==0:
    res="Eixo Y"
elif y==0:
    res="Eixo X"
elif x>0 and y>0:
    res="Q1"
elif x<0 and y>0:
    res="Q2"
elif x<0 and y<0:
    res="Q3"
elif x>0 and y<0:
    res="Q4"

print(res)

##1042
entrada=input()
lista=[int(i) for i in entrada.split()]
lista_nova= sorted(lista)

for i in lista_nova:
    print(i)

print()

for i in lista:
    print(i)

##1043
def eh_triangulo(a, b, c):
    # Condição de existência de um triângulo
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


a, b, c= map(float, input().split())

if eh_triangulo(a, b, c):
    res=a+b+c
    print(f"Perimetro = {res:.1f}")
else:
    res=((a+b)*c)/2
    print(f"Area = {res:.1f}")


##1044

a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

##1045

a, b, c = map(float, input().split())
lista=[a,b,c]
lista_nova=sorted(lista, reverse=True)
a=lista_nova[0]
b=lista_nova[1]
c=lista_nova[2]

if a>=b+c:
    print("NAO FORMA TRIANGULO")
elif a**2==b**2+c**2:
    print("TRIANGULO RETANGULO")
elif a**2>b**2+c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2<b**2+c**2:
    print("TRIANGULO ACUTANGULO")

if a==b==c:
    print("TRIANGULO EQUILATERO")
elif a==b!=c or a==c!=b or b==c!=a:
    print("TRIANGULO ISOSCELES")

##1046

a, b= map(int,input().split())

if a < b:
    horas = b - a #a está dentro do b, então é só tirar essa parte
else:
    horas = (24 - a) + b ##Resto do dia passado mais as horas do novo dia
    
print(f"O JOGO DUROU {horas} HORA(S)")

##1047
hora_i, min_i, hora_f, min_f= map(int,input().split())

horas=0
minutos=0
#converte tudo em minutos
inicio = hora_i * 60 + min_i
fim = hora_f * 60 + min_f

if fim > inicio:
    duracao = fim - inicio 
elif fim < inicio:
    duracao = (24 * 60 - inicio) + fim
else:
    duracao = 24 * 60 #passou exatamente um dia

horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

##1048
sala=float(input())
per=0

if 400>=sala>0:
    per=15
elif 800>=sala>400:
    per=12
elif 1200>=sala>800:
    per=10
elif 2000>=sala>1200:
    per=7
elif sala>2000:
    per=4

sala_novo= sala+(sala*per/100)
reajuste= sala_novo-sala

print(f"Novo salario: {sala_novo:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {per} %")

##1049
a=input()
b=input()
c=input()
animal="0"
if a=="vertebrado":
    if b=="ave":
        if c=="carnivoro":
            animal="aguia"
        else:
            animal="pomba"
    elif b=="mamifero":
        if c=="onivoro":
            animal="homem"
        else:
            animal="vaca"

elif a=="invertebrado":
    if b=="inseto":
        if c=="hematofago":
            animal="pulga"
        else:
            animal="lagarta"
    elif b=="anelideo":
        if c=="hematofago":
            animal="sanguessuga"
        else:
            animal="minhoca"
            
print(animal)

##1050
a=int(input())
name="DDD nao cadastrado"
match a:
    case 61:
        name="Brasilia"
    case 71:
        name="Salvador"
    case 11:
        name="Sao Paulo"
    case 21:
        name="Rio de Janeiro"
    case 32:
        name="Juiz de Fora"
    case 19:
        name="Campinas"
    case 27:
        name="Vitoria"
    case 31:
        name="Belo Horizonte"

print(f"{name}")

##1051

salario = float(input())

if salario <= 2000:
    print("Isento")
else:
    imposto = 0
    if salario > 2000:
        faixa8 = min(salario, 3000) - 2000.00 #resto, exemplo: mim(2002,3000) -> 2002-2000=2
        if faixa8 > 0: #Não tem como cobrar imposto se não tem resto
            imposto += faixa8 * 0.08
    
    if salario > 3000:
        faixa18 = min(salario, 4500) - 3000
        if faixa18 > 0:
            imposto += faixa18 * 0.18
    
    if salario > 4500:
        faixa28 = salario - 4500
        imposto += faixa28 * 0.28
    
    print(f"R$ {imposto:.2f}")

##1052
##1060
##1061
##1064
##1065
##1066
##1067
##1070
##1071
##1072
##1073



