N = int(input())

tabuleiro = [[0] * 12 for _ in range(12)]
valido = True

for _ in range(N):
    D, L, R, C = map(int, input().split())

    if not valido:
        continue

    if D == 0:
        if C + L - 1 > 10:
            valido = False
        else:
            for i in range(L):
                if tabuleiro[R][C + i] == 1:
                    valido = False
                    break
                tabuleiro[R][C + i] = 1
    else:
        if R + L - 1 > 10:
            valido = False
        else:
            for i in range(L):
                if tabuleiro[R + i][C] == 1:
                    valido = False
                    break
                tabuleiro[R + i][C] = 1

if valido:
    print('Y')
else:
    print('N')