L, D = map(int, input().split())
K, P = map(int, input().split())
     
num_pedagios = L // D
valor_pedagios = num_pedagios * P
valor_km = L * K
total = valor_km + valor_pedagios
     
print(total)