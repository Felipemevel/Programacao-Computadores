j, r = map(int, input().split())
jogadas = list(map(int, input().split()))

pontuacao = [0] * j

for i in range(len(jogadas)):
    pontuacao[i % j] += jogadas[i]

maior_pontuacao = max(pontuacao)

for i in range(j - 1, -1, -1):
    if pontuacao[i] == maior_pontuacao:
        print(i + 1)
        break