A = int(input())
B = int(input())
C = int(input())

distancia_BA = B - A
distancia_CB = C - B

if distancia_BA < distancia_CB:
    print(1)
else:
    if distancia_BA > distancia_CB:
        print(-1)
    else:
        print(0)