nome = str(input())
salario = float(input())
bonus = float(input())
     
total_vendas = salario + (bonus * 0.15)
     
print(f"{nome}\nR$ {total_vendas:.2f}")