D = int(input())
V = int(input())
     
horas = D // V
minutos = int(((D / V) - horas) * 60)
     
print(f"{horas:02d}:{minutos:02d}")