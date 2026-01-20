def dia_da_semana (h, d):
    dias = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    dia_hoje = dias.index(h)
    data_evento = (dia_hoje + d) % 7
    return dias[data_evento]