def valores (qtdA: int, qtdB: int) -> list:
    Sa = list(map(int, input().split()))
    Sb = list(map(int, input().split()))
    return Sa, Sb

def processamento_dados(Sa: list, Sb: list) -> tuple:
    Subseq = []
    copia_sb = Sb[:]
    for i in range(0, len(Sa)):  
        if len(copia_sb) > 0 and Sa[i] == copia_sb[0]:
            copia_sb = copia_sb[1:]

    if len(copia_sb) == 0:
        return "S"
    return []

def validacao_dados(subseq: list) -> str:
    if len(subseq) > 0:
        return "S"
    
    return "N"


a, b = map(int, input().split())
lista1, lista2 = valores(a, b)

print(validacao_dados(processamento_dados(lista1, lista2)))