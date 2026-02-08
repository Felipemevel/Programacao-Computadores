def valores (qtdA: int, qtdB: int) -> list:
    Sa = list(map(int, input().split()))
    Sb = list(map(int, input().split()))
    return Sa, Sb

def processamento_dados(Sa: list, Sb: list) -> str:
    for i in range(0, len(Sa)):  
        if len(Sb) > 0 and Sa[i] == Sb[0]:
            Sb.pop(0)

        if len(Sb) == 0:
            return "S"    
    return "N"


a, b = map(int, input().split())
lista1, lista2 = valores(a, b)

print((processamento_dados(lista1, lista2)))