def valores (qtd: int) -> list:
    nums = []
    for i in range(qtd):
        nums.append(int(input()))
    return nums

def imperial(qtd: int, nums: list) -> int:
    contador = 1
    for i in range(qtd):
        for j in range(i+1, qtd):
            if nums[j] == nums[i]:
                continue
            n_atual = nums[i]
            n_prox = nums[j]
            contador_temp = 2
            for v in range(j+1, qtd):
                if nums[v] == n_atual:
                    contador_temp += 1
                    n_atual, n_prox = n_prox, n_atual
            if contador_temp > contador:
             contador = contador_temp
    return contador

quantidade = int(input())
print(imperial(quantidade, valores(quantidade)))