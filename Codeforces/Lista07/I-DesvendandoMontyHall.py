N = int(input())
vitorias = 0
for _ in range(N):
    porta_do_carro = int(input())
    if porta_do_carro != 1:
        vitorias += 1

print(vitorias)