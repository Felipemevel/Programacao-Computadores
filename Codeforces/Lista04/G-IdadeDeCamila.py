a = int(input())
b = int(input())
c = int(input())

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

camila = (a + b + c) - maior - menor

print(camila)