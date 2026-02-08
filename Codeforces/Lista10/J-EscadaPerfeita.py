n = int(input())
pilhas = list(map(int, input().split()))

soma_total = sum(pilhas)
soma_escada = (n * (n - 1)) // 2
resto = soma_total - soma_escada

if resto < 0 or resto % n != 0:
    print("-1")
else:
    base = resto // n
    movimentos = 0
    for i in range(n):
        altura_ideal = base + i
        if pilhas[i] > altura_ideal:
            movimentos += pilhas[i] - altura_ideal
    print(movimentos)