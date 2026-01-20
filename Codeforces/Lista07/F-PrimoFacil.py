n = int(input())
divisores = []

for i in range(1, n+1):
    if n%i == 0:
        divisores.append(i)
        
if len(divisores) != 2:
    print("nao")
else:
    print("sim")