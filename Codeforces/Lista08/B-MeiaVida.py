s, mi = map(int, input().split())
tempo = 0

while(mi >= 0.5):
    tempo += s
    mi = mi/2

dias = tempo//86400
horas = (tempo%86400)//3600
minutos = (tempo%3600)//60
segundos = tempo%60

print(f"{dias} dias {horas:02}:{minutos:02}:{segundos:02}")