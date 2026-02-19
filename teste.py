import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

# Leitura do valor
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