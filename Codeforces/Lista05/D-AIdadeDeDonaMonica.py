M = int(input())
A = int(input())
B = int(input())

C = M - A - B

mais_velho = A

if B > mais_velho:
    mais_velho = B

if C > mais_velho:
    mais_velho = C

print(mais_velho)