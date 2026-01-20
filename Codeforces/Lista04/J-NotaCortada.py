lados = list(map(int, input().split()))
lados.sort()

a, b, c = lados[0], lados[1], lados[2]

if a + b <= c:
    print('n')
else:
    if (a**2 + b**2) > c**2:
        print('a')
    elif (a**2 + b**2) == c**2:
        print('r')
    else:
        print('o')