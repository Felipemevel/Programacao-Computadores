C = int(input())
A = int(input())

capacidade_alunos_por_viagem = C - 1

numero_de_viagens = (A - 1) // capacidade_alunos_por_viagem + 1

print(numero_de_viagens)