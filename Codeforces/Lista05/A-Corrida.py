N1, D1, V1 = map(int, input().split())
N2, D2, V2 = map(int, input().split())

tempo1_relativo = D1 * V2
tempo2_relativo = D2 * V1

if tempo1_relativo < tempo2_relativo:
    print(N1)
else:
    print(N2)