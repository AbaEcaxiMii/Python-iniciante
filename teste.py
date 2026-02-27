import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

n=int(input())
total=0
total_c=0
total_r=0
total_s=0
for i in range(n):
    x = input().split()
    a = int(x[0])
    b = x[1]
    
    total+=a
    
    if b=="C":
        total_c+=a
    elif b=="R":
        total_r+=a
    elif b=="S":
        total_s+=a

por_c=(total_c/total)*100
por_r=(total_r/total)*100
por_s=(total_s/total)*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_c}")
print(f"Total de ratos: {total_r}")
print(f"Total de sapos: {total_s}")
print(f"Percentual de coelhos: {por_c}")
print(f"Percentual de ratos: {por_r}")
print(f"Percentual de sapos: {por_s}")