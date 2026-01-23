def valores (qtd: int) -> list:
    lista = list(map(int, input().split()))
    return lista

def fita_colorida(lista: list) -> list:
    resposta = []
    idx_zero = []
    for i in range(0, len(lista)):
        if lista[i] == 0:
            idx_zero.append(i)
    for j in range(0, len(lista)):
        idx_atual = j
        v_escolhido = 0
        for v in range(0, len(idx_zero)):
            if v+1 < len(idx_zero):
                if abs(idx_zero[v] - idx_atual) >= abs(idx_zero[v+1] - idx_atual):
                    v_escolhido = v + 1
                    continue
        v = v_escolhido
        if idx_zero[v] > idx_atual:
            distancia = (idx_zero[v] - idx_atual)
        else:
            distancia = (idx_atual - idx_zero[v])

        if distancia > 9:
            distancia = 9
        resposta.append(distancia)
    return print(*resposta)

    

fita_colorida(valores(int(input())))