import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

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