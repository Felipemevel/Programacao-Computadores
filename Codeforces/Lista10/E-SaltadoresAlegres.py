def processar_valores() -> list:
    while True:
        try:
            lista = input().split()
            if not lista: break

            nums = list(map(int, lista))

            saltadores_alegres(nums)
        except EOFError:
            break

def saltadores_alegres(lista: list):
    n = lista[0]
    resto_lista = lista[1:]
    valores_encontrados = []

    if n == 1:
        resposta.append("Alegre")
        return

    for i in range(1, len(resto_lista)):
        res = abs(resto_lista[i-1]-resto_lista[i]) 
        if 1 <= res <= n - 1 and res not in valores_encontrados:
            valores_encontrados.append(res)

    if len(valores_encontrados) == n - 1:
        resposta.append("Alegre")
    else:
        resposta.append("Não alegre")
        
resposta = []

processar_valores()

for resposta in resposta:
    print(resposta)