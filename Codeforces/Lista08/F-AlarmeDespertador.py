while True:
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == M1 == H2 == M2 == 0:
        break

    t1 = H1 * 60 + M1
    t2 = H2 * 60 + M2

    if t2 < t1:
        t2 += 24 * 60

    print(t2 - t1)