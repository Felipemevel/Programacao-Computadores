n = int(input())
     
print(n)
     
for nota in[100, 50, 20, 10, 5, 2, 1]:
    qtd = n // nota
    print(f"{qtd} nota(s) de R$ {nota},00")
    n %= nota