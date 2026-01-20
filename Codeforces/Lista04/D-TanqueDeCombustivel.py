C = int(input())
D = int(input())
T = int(input())

litros_necessarios = D / C
litros_a_comprar = litros_necessarios - T

if litros_a_comprar < 0:
    litros_a_comprar = 0

print(f"{litros_a_comprar:.1f}")