contador = 0
qtd = int(input())
n = []


for i in range(1, qtd + 1):
    new_n = int(input())
    n.append(new_n)

p = int(input())

for j in range(p):
    new_pedido = int(input()) - 1
    if n[new_pedido] != 0:
        contador += 1
        n[new_pedido] -= 1

print(contador)
