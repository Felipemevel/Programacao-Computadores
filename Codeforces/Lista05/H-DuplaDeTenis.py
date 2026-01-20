A = int(input())
B = int(input())
C = int(input())
D = int(input())

diff1 = (A + D) - (B + C)
if diff1 < 0:
    diff1 = -diff1

diff2 = (A + C) - (B + D)
if diff2 < 0:
    diff2 = -diff2

diff3 = (A + B) - (C + D)
if diff3 < 0:
    diff3 = -diff3

menor = diff1

if diff2 < menor:
    menor = diff2

if diff3 < menor:
    menor = diff3

print(menor)