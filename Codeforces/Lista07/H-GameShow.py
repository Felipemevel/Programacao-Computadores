n = int(input())
saldo = 100
max_saldo = saldo

for i in range(n):
    v = int(input())
    saldo += v
    max_saldo = max(max_saldo, saldo)

print(max_saldo)