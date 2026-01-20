def media_ponderada(v1, p1, v2, p2):
    res = ((p1 * v1) + (p2 * v2)) / (p1 + p2)
    return float(f"{res:.6f}")